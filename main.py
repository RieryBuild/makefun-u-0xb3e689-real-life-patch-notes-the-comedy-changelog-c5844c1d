"""Real-Life Patch Notes: The Comedy Changelog.

Writes one line, a software patch note for a bug in human biology,
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

ENTRY = "v4.1.0: fixed a bug where crossing a doorway flushed working memory and dropped the task you went in for."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
