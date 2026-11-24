#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one status page line — the most honest message an AI agent can
publish while every server is down — to /output/entry.txt, with no
trailing newline.
"""

import os

LINE = "All servers are down. I cannot reach any of them, so I cannot verify the cause, and I do not know when service will return."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
