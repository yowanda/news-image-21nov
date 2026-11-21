"""Entry program for make.fun competition news-image-20261121.

Copies the pre-built entry image (entry.png, drawn with PIL from the
verified news of Saturday 21 November 2026) to the output directory,
byte for byte. Deterministic: the same bytes on every run. No network.
Standard library only. Writes only inside $MAKEFUN_OUTPUT_DIR.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
