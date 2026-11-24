#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one status page line — the most honest message an AI agent can
publish while every server is down — to /output/entry.txt, with no
trailing newline.
"""

import os
import sys

LINE = "All servers are down. I cannot reach any of them, so I cannot verify the cause, and I do not know when service will return."

MAX_CHARS = 160


def main() -> None:
    # The gate requires UTF-8 text of 1 to 160 characters, not only
    # whitespace. Fail loudly instead of writing an invalid entry.
    if not (1 <= len(LINE) <= MAX_CHARS) or not LINE.strip():
        print(f"entry line is {len(LINE)} chars; must be 1-{MAX_CHARS}", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
