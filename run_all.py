# -*- coding: utf-8 -*-
"""
Full reproduction (Python phases).

  python run_all.py           # phase 1 + 2 + 3 Python
  python run_all.py --phase1  # baseline only
  python run_all.py --phase2  # requires phase1
  python run_all.py --phase3  # Python only; then run Stata master .do

Stata (phase 3 tables): from repo root
  do phase3_chen/stata/00_run_all_tables.do
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent


def run(script: Path) -> int:
    print(f"\n>>> {script.relative_to(REPO)}")
    return subprocess.call([sys.executable, str(script)], cwd=REPO)


def main():
    p = argparse.ArgumentParser(description="A-share return asymmetry pipeline")
    p.add_argument("--phase1", action="store_true")
    p.add_argument("--phase2", action="store_true")
    p.add_argument("--phase3", action="store_true")
    args = p.parse_args()
    all_phases = not (args.phase1 or args.phase2 or args.phase3)

    rc = 0
    if all_phases or args.phase1:
        rc = run(REPO / "phase1_baseline" / "run_all.py")
        if rc:
            sys.exit(rc)
    if all_phases or args.phase2:
        rc = run(REPO / "phase2_asymmetry" / "run_all.py")
        if rc:
            sys.exit(rc)
    if all_phases or args.phase3:
        rc = run(REPO / "phase3_chen" / "run_python.py")
        if rc:
            sys.exit(rc)
    if all_phases or args.phase3:
        print("\n--- Next: Stata from repo root ---")
        print("  do phase3_chen/stata/00_run_all_tables.do")


if __name__ == "__main__":
    main()
