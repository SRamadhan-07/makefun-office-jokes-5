#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes one line to /output/entry.txt: an office joke about the new
KPI dashboard being so transparent that the whole team can watch its
targets not being met in real time, in 4K. This competition's gate
is 1 to 199 characters — one tighter than the usual 200 — and the
line is written with no trailing newline.
"""

import os
from pathlib import Path

JOKE = (
    "The new KPI dashboard is so transparent that the whole team can "
    "now watch our targets not being met in real time, in 4K."
)

MAX_CHARS = 199


def main() -> None:
    # Guard both ends of the gate before writing anything: the file
    # must hold between 1 and 199 characters, and this joke is 120.
    assert 1 <= len(JOKE) <= MAX_CHARS, "joke outside this competition's gate"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
