"""Funniest One-Line Out-of-Office Reply — account B entry.

Writes a single funny out-of-office reply line to entry.txt inside the
output directory. Deterministic: the same line, byte for byte, on every run.
Standard library only; no network, no secrets, no input files.
"""

import os

# The reply: the out-of-office message delegates to a second auto-reply,
# which is itself also out of office until further notice.
LINE = (
    "I've forwarded your email to my out-of-office reply, "
    "which is also out of office until further notice."
)

MAX_CHARS = 160


def verify_line(text):
    """Gate: one line, 1-160 chars, stripped, valid UTF-8, no blank text."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if stripped != text:
        raise ValueError("entry must already be stripped")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if not 1 <= len(stripped) <= MAX_CHARS:
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(stripped)))
    stripped.encode("utf-8")  # raises if not valid UTF-8-encodable
    return stripped


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = verify_line(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
