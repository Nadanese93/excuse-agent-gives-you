#!/usr/bin/env python3
"""Make.fun micro entry: The Excuse Your Agent Gives You.

Writes a single one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3 stdlib only.
"""

import os
import stat
import tempfile

ENTRY = (
    "The linter approved it, the formatter blessed it, and CI waved it "
    "through \u2014 the bug has better references than I do."
)


def validate(text):
    """Check the entry meets the kit gate: 1-200 chars, single line."""
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > 200:
        raise ValueError("entry exceeds 200 characters: %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    validate(ENTRY)
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    fd, tmp_path = tempfile.mkstemp(dir=output_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, target)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    os.chmod(target, 0o644)
    # E38 read-back verification: confirm what landed on disk is byte-identical
    # to what was written; a silent partial write must fail loudly, not pass.
    with open(target, "rb") as f:
        if f.read() != data:
            raise IOError("entry.txt read-back mismatch after atomic replace")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
