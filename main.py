"""One-Star Review of Something Essential — make.fun entry (reviser rewrite).

Reviser version: the entry text is unchanged from the builder version
(121 bytes, one line, no trailing newline). This module builds the entry,
validates it against the known SHA-256 before writing, and writes it
directly to the final path with mode 0644 so the grader can read it.

Pure Python standard library. Deterministic, no network, no dependencies.
"""

import hashlib
import os

# Expected SHA-256 of the exact entry text (121 bytes, no trailing newline).
EXPECTED_SHA256 = "cc850000dfbba528193f0e740103fcb35e8664bbec61bb559ab0bbb1df19bd7c"
EXPECTED_BYTES = 121


def build_entry():
    """Return the single-line one-star review of toothpaste."""
    return (
        "One star. Toothpaste surrenders the first ninety percent freely, "
        "then defends the last ten like it has something to hide."
    )


def validate_entry(text):
    """Check the entry is exactly one line with the expected hash.

    Raises ValueError on any mismatch, so a bad entry is never written.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no newline")
    encoded = text.encode("utf-8")
    if len(encoded) != EXPECTED_BYTES:
        raise ValueError(
            "entry must be %d bytes, got %d" % (EXPECTED_BYTES, len(encoded))
        )
    digest = hashlib.sha256(encoded).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError("entry sha256 mismatch: got %s" % digest)
    return True


def write_entry():
    """Validate the entry, then write it directly to entry.txt.

    Writes straight to the final path with open() and sets mode 0644
    explicitly. No temporary file, no os.replace: the grader reads
    entry.txt as another user, so the mode must be world-readable.
    """
    text = build_entry()
    validate_entry(text)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def main():
    path = write_entry()
    print("Wrote " + path)


if __name__ == "__main__":
    main()
