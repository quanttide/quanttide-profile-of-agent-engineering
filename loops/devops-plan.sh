#!/usr/bin/env bash
# devops-plan.sh — 规划循环承载脚本
#
# 用法:
#   devops-plan.sh <任务目录>           # 列出 3 个阶段
#   devops-plan.sh <任务目录> --check   # 校验各阶段产物是否齐备（默认）
#   devops-plan.sh <任务目录> --dry-run # 预览产物清单，不校验
#
# 产物约定（与 verification.md 一致）:
#   intention.md   → 阶段 1 意图
#   insights.md    → 阶段 2 洞察
#   roadmap.md     → 阶段 3 路线图
set -euo pipefail

DIR="${1:-.}"
MODE="${2:-check}"

declare -A ARTIFACTS=(
  [1-意图]="$DIR/intention.md"
  [2-洞察]="$DIR/insights.md"
  [3-路线图]="$DIR/roadmap.md"
)

echo "== devops-plan 规划循环（$DIR）=="
for step in "1 intention：明确意图" \
            "2 insights：从实践/数据提炼洞察" \
            "3 roadmap：产出可执行路线图"; do
  printf '  %s\n' "$step"
done

case "$MODE" in
  --dry-run)
    echo
    echo "== 预期产物 =="
    for name in "${!ARTIFACTS[@]}"; do
      printf '  %-12s %s\n' "$name" "${ARTIFACTS[$name]}"
    done
    ;;
  --check)
    echo
    echo "== 产物校验 =="
    fail=0
    for name in "${!ARTIFACTS[@]}"; do
      if [ -e "${ARTIFACTS[$name]}" ]; then
        printf '  [✓] %-12s %s\n' "$name" "${ARTIFACTS[$name]}"
      else
        printf '  [✗] %-12s %s\n' "$name" "${ARTIFACTS[$name]}"
        fail=1
      fi
    done
    if [ "$fail" -ne 0 ]; then
      echo "== 有产物缺失，本轮未完成 =="
      exit 1
    fi
    echo "== 产物齐备，进入反馈点：向人呈现意图与洞察，确认后进入下一步 =="
    ;;
  *)
    echo "用法: devops-plan.sh <任务目录> [--check|--dry-run]" >&2
    exit 2
    ;;
esac
