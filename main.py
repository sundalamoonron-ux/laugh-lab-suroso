#!/usr/bin/env python3
"""One-Liner Laugh Lab -- make.fun entry.

Emits a single one-line excuse from a robot vacuum after eating a sock
into <output>/entry.txt. The joke is a blame-shift excuse with a
vacuum-specific twist: the sock attacked first, and the vacuum has the
brush-roll footage to prove it. Chosen over 9 other candidates in a
full pairwise round-robin (9-0) plus 3x finals against the other two
finalists (4-2); see candidates.md for the full tournament.
"""

import os
import sys

# The joke: 67 characters, one line. "The sock attacked first" frames
# the vacuum as a wrongly accused defendant; "brush-roll footage" is
# the deadpan, vacuum-specific evidence that closes the gag.
JOKE = "The sock attacked first. I have the brush-roll footage to prove it."

def emit() -> str:
    """Return the entry text, checked against the competition gate."""
    joke = JOKE
    size = len(joke)
    if not 1 <= size <= 200:
        raise ValueError(f"joke is {size} characters, gate wants 1-200")
    if not joke.strip():
        raise ValueError("joke is only whitespace")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be one line")
    return joke

def main() -> int:
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    entry_path = os.path.join(target_dir, "entry.txt")
    text = emit()
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(entry_path, "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        raise ValueError("entry.txt bytes do not match the joke")
    return 0

if __name__ == "__main__":
    sys.exit(main())
