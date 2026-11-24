"""Houseplant Out-of-Office entry (Python 3.13, standard library only).

Writes the plant's out-of-office auto-reply to entry.txt in the output
directory, verifying the gate (1-120 UTF-8 characters, not only
whitespace) before the write and reading the file back afterwards.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output.
"""

import os
from pathlib import Path

ENTRY = (
    "Out of office: the fern filed a complaint with HR about the "
    "light. I'm the fern. There is no HR."
)

MAX_CHARS = 120


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def check_entry(text: str) -> None:
    """Raise ValueError unless the text passes the competition gate."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} characters, must be 1-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")


def write_entry(text: str) -> Path:
    """Write the entry, then read it back and verify it in full."""
    check_entry(text)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != text:
        raise IOError("read-back text differs from the entry")
    if target.read_bytes() != text.encode("utf-8"):
        raise IOError("read-back bytes differ from the entry's UTF-8")
    return target


def main() -> None:
    target = write_entry(ENTRY)
    print(f"wrote {target} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
