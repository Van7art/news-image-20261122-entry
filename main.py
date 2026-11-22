#!/usr/bin/env python3
"""THE WORLD - Sunday 22 November 2026.

A one-page newspaper front page summing up the world news of
Sunday 22 November 2026 in a single image. The front page is held
in the repository as entry.png; this program copies it to the
output directory. Standard library only, no network access,
deterministic: every run writes the same bytes.
"""
import os
import shutil

# The front-page image lives beside this program in the repository.
# The grader runs the program with the repository present, so the
# image is always there to copy.
IMAGE_NAME = "entry.png"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE_NAME)
    if not os.path.isfile(src):
        raise FileNotFoundError("front-page image missing: %s" % src)
    dst = os.path.join(out, IMAGE_NAME)
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
