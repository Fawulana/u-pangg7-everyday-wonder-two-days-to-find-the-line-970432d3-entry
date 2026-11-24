# SPDX-License-Identifier: MIT
"""Everyday Wonder entry.

Writes one sentence about a small moment of wonder in everyday life to
/output/entry.txt. Deterministic, offline, standard library only.
"""

import os

ENTRY = "The elevator mirror caught me mid-yawn, and for a second I apologized to a stranger who was me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.strip(), "entry must not be only white space"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
