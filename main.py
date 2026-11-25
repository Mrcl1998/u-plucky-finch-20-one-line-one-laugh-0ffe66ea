#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt.

Pure standard library, deterministic, no network. The line is a fixed
constant: a self-contained one-liner whose punchline lands inside the line.
No trailing newline is written, per the competition gate.
"""

import os

LINE = "I rehearse arguments in the shower and lose every single one to the shampoo bottle."


def main():
    text = LINE
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    out_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
