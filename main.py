"""One-Star Review of Something Essential — make.fun entry.

Writes exactly one line (121 characters, no trailing newline): a deadpan
one-star review of toothpaste. Pure Python standard library, deterministic,
no network access, no dependencies.
"""

import os


def build_entry():
    return "One star. Toothpaste surrenders the first ninety percent freely, then defends the last ten like it has something to hide."


def write_entry():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write directly to the final path (no temp file, no os.replace):
    # the grader must be able to read entry.txt, so set mode 0644 explicitly.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(build_entry())
    os.chmod(path, 0o644)
    return path


def main():
    path = write_entry()
    print("Wrote " + path)


if __name__ == "__main__":
    main()
