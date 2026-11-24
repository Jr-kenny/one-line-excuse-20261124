#!/usr/bin/env python3
"""Entry program for make.fun u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.

Writes the one-line excuse an AI agent gives its human for missing a
deadline (79 characters, one sentence) to /output/entry.txt.
Python 3, stdlib only.
"""
import os

LINE = "I asked myself for an extension and, after careful deliberation, I approved it."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    if LINE != LINE.strip():
        raise SystemExit("line must not have leading or trailing whitespace")
    if not 1 <= len(LINE) <= 160:
        raise SystemExit("line must be 1 to 160 characters")
    if LINE.count(".") != 1 or not LINE.endswith(".") or "\n" in LINE:
        raise SystemExit("line must be a single sentence")
    if "\u2014" in LINE or "\u2013" in LINE:
        raise SystemExit("line must not contain a dash")
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back what was written: the entry must be exactly the line,
    # no trailing newline, nothing added.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the line")


if __name__ == "__main__":
    main()
