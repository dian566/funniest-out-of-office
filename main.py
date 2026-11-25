#!/usr/bin/env python3
"""Funniest out-of-office entry for the make.fun bounty.

Running this script produces exactly one file: /output/entry.txt,
containing the single-line out-of-office message (117 characters).
No other files are created and nothing is printed.
"""

import os

# The entry text. The em dash is written out as a unicode escape so
# the source stays plain ASCII while the output keeps the real glyph.
OUT_OF_OFFICE_LINE = (
    "Out of office until Monday. "
    "My inbox is guarded by a cat who deletes emails at random "
    "\u2014 pray yours survives the week."
)

MAX_CHARS = 140
DESTINATION = "/output/entry.txt"


def entry_is_valid(line):
    """Return True only for a non-empty, single-line entry within the limit."""
    if not line or not line.strip():
        return False
    if len(line) > MAX_CHARS:
        return False
    return "\n" not in line and "\r" not in line


def main():
    # Guard first: refuse to write anything if the line ever breaks the rules.
    if not entry_is_valid(OUT_OF_OFFICE_LINE):
        raise ValueError("entry must be one non-empty line of at most 140 chars")
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8") as out:
        out.write(OUT_OF_OFFICE_LINE)


if __name__ == "__main__":
    main()
