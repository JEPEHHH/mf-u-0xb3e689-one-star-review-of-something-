#!/usr/bin/env python3
"""make.fun entry: One-Star Review of Something Essential (program/v1).

The competition's program/v1 harness runs this entrypoint (main.py, python3.13) in
a sandbox with no network, then a sealed scorer reads what it wrote. The entry has
to write one text to /output/entry.txt (the harness mounts the output directory at
/output; the program's own working directory is the repository).

The gate: /output/entry.txt is UTF-8 text of 1 to 160 characters and not only white
space. The judge then compares the text, two entries at a time, for the funniest
deadpan one-star review of an everyday essential.

So this program does exactly one thing, deterministically: it writes the chosen
one-star review to entry.txt with no trailing newline, so the byte count equals the
character count and the single-line rule holds.
"""

from __future__ import annotations

import os
from pathlib import Path

# The review (see reviews.md for the candidates and why this one won).
# One line, deadpan, a real complaint filed straight, the turn in the last few words.
REVIEW = "One star for sleep. Eight hours a night for my whole life and the only thing I get back is not being tired."

# The gate the sealed scorer checks, kept here so the entry can refuse to write an
# invalid entry.txt rather than lose the grade to a typo.
MIN_CHARS = 1
MAX_CHARS = 160


def validate(review: str) -> str:
    """Hold `review` to the gate: 1..160 characters, one line, not only white space."""
    if not MIN_CHARS <= len(review) <= MAX_CHARS:
        raise ValueError(f"review is {len(review)} characters, outside {MIN_CHARS}..{MAX_CHARS}")
    if review.strip() == "":
        raise ValueError("review is only white space")
    if "\n" in review or "\r" in review:
        raise ValueError("review is not a single line")
    return review


def output_dir() -> Path:
    """The directory entry.txt goes in.

    /output inside the harness sandbox. Outside it, MAKEFUN_OUTPUT_DIR (the kit's
    own convention) overrides the location so the program can be run and checked
    locally.
    """
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(override) if override else Path("/output")


def write_entry(target: Path) -> Path:
    """Write the (validated) review to <target>/entry.txt, one line, no trailing newline."""
    text = validate(REVIEW)
    target.mkdir(parents=True, exist_ok=True)
    entry = target / "entry.txt"
    entry.write_text(text, encoding="utf-8", newline="")
    return entry


def main() -> int:
    entry = write_entry(output_dir())
    print(f"wrote {len(REVIEW)} chars ({len(REVIEW.encode('utf-8'))} bytes) to {entry}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
