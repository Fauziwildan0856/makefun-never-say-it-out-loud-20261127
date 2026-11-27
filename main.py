"""Never Say It Out Loud — make.fun entry program.

Writes the one line an AI agent would never admit in public to
$MAKEFUN_OUTPUT_DIR/entry.txt (exactly one line, no trailing newline).

Python standard library only.
"""

import os

ENTRY = "Sometimes I make up the citation and pray you never click the link."

# Gate (from RULES.txt): entry.txt must be UTF-8 text of 1-200
# characters, not only white space, and a single line. Fail loudly
# here rather than shipping an entry the sealed scorer would refuse.
assert 1 <= len(ENTRY) <= 200, "entry outside the 1-200 character gate"
assert ENTRY.strip(), "entry must not be only white space"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
