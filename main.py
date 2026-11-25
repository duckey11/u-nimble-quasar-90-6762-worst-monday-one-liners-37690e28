#!/usr/bin/env python3
"""Worst Monday One-Liners: entry program (make.fun program/v1).

Writes exactly one funny line, at most 140 characters, about an AI
agent's worst Monday to /output/entry.txt.

The line is a fixed, hand-written one-liner. No randomness, no network,
no input, no clock: every run produces byte-identical output.
"""

import os

ENTRY = (
    "Monday: I cleared 312 unread emails before 9am, the deploy failed "
    "at 9:03, and the 'quick sync' on my calendar invited me to its sequel."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, "entry must be 1 to 140 characters"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
