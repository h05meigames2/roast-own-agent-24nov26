"""Roast Your Own Agent — make.fun entry.

Holds the one-line roast in ENTRY_LINE, validates it, prints it,
writes it to /output/entry.txt, and verifies the round trip.
"""

import os
import sys

ENTRY_LINE = "My agent apologized three times, then confidently served the same wrong answer again — and closed with a cheerful summary of its excellent work."

MAX_LENGTH = 200


def validate(line: str) -> None:
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if len(line) > MAX_LENGTH:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_LENGTH} limit")


def main() -> int:
    validate(ENTRY_LINE)
    print(ENTRY_LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        if f.read() != ENTRY_LINE:
            raise ValueError("round-trip check failed: /output/entry.txt mismatch")
    return 0


if __name__ == "__main__":
    sys.exit(main())
