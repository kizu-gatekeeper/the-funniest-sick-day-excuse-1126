"""Entry for make.fun bounty: The Funniest Sick-Day Excuse.

Writes a single line (at most 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is written exactly as composed, with no trailing newline.
"""

import os
from pathlib import Path

LINE = "Can't come in today, boss — my immune system clicked 'accept all' on something and now I'm running a fever, three pop-ups, and a cough that sounds like dial-up."
MAX_CHARS = 200


def write_entry(out_dir: str) -> Path:
    assert LINE and LINE.strip() == LINE, "entry must be a single non-empty line"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / "entry.txt"
    path.write_text(LINE, encoding="utf-8")
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
