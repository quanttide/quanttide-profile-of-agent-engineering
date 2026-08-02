#!/usr/bin/env bash
# devops-code.sh — 开发循环承载脚本
#
# 用法:
#   devops-code.sh <任务目录>           # 列出 6 个阶段
#   devops-code.sh <任务目录> --check   # 校验各阶段产物是否齐备（默认）
#   devops-code.sh <任务目录> --dry-run # 预览产物清单，不校验
#
# 产物约定（见 README.md 验证章节）:
#   docs/              → 阶段 1 写文档
#   tests/             → 阶段 2 设置测试
#   src/               → 阶段 3/4 设计与实现
#   review.md          → 阶段 5 评审重构记录
#   product-check.md   → 阶段 6 产品视角检查
set -euo pipefail

DIR="${1:-.}"
MODE="${2:-check}"

declare -A ARTIFACTS=(
  [1-文档]="$DIR/docs"
  [2-测试]="$DIR/tests"
  [3-实现]="$DIR/src"
  [5-评审记录]="$DIR/review.md"
  [6-产品视角检查]="$DIR/product-check.md"
)

echo "== devops-code 开发循环（$DIR）=="
for step in "1 先写文档（不必是严格 spec）" \
            "2 设置测试" \
            "3 设计模块和测试实现" \
            "4 测试和代码实现" \
            "5 评审：先按社区规范，再整理重构" \
            "6 回到产品视角，检查偏差"; do
  printf '  %s\n' "$step"
done

case "$MODE" in
  --dry-run)
    echo
    echo "== 预期产物 =="
    for name in "${!ARTIFACTS[@]}"; do
      printf '  %-14s %s\n' "$name" "${ARTIFACTS[$name]}"
    done
    ;;
  --check)
    echo
    echo "== 产物校验 =="
    fail=0
    for name in "${!ARTIFACTS[@]}"; do
      if [ -e "${ARTIFACTS[$name]}" ]; then
        printf '  [✓] %-14s %s\n' "$name" "${ARTIFACTS[$name]}"
      else
        printf '  [✗] %-14s %s\n' "$name" "${ARTIFACTS[$name]}"
        fail=1
      fi
    done
    if [ "$fail" -ne 0 ]; then
      echo "== 有产物缺失，本轮未完成 =="
      exit 1
    fi
    echo "== 产物齐备，进入反馈点：向人呈现结果 =="
    ;;
  *)
    echo "用法: devops-code.sh <任务目录> [--check|--dry-run]" >&2
    exit 2
    ;;
esac
