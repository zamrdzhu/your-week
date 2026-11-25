"""Your Week in One Line — one funny line.

The week, summed up in a single ledger: five features shipped,
six broken, and the coffee machine — the week's most reliable
coworker — has started charging rent. One concrete detail, one
sharp turn, nothing padded inside the 100-character gate; the
scoreboard format is the joke, and the rent is the punchline.

Prints the joke to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the joke is a constant in this
file. The 100-character gate is checked on every run so an
over-long edit can never slip through silently.
"""

import os
import sys

LINE = "Shipped five features, broke six, and my coffee machine has started charging me rent."


def main() -> int:
    if not 1 <= len(LINE) <= 100:
        print(f"error: line is {len(LINE)} chars, must be 1-100",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
