"""One-line museum placard for an ordinary office object.

Writes a single placard line (at most 180 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, creating the directory if needed.
Deterministic: the same bytes on every run.
"""

import os

LINE = (
    "Sticky note, paper and adhesive, c. 2011. Found affixed to a monitor, "
    "inscribed 'DO NOT TOUCH' in a hand no employee recognised."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
