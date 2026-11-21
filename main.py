"""Entry program for make.fun competition news-image-20261121.

Copies the pre-built entry image (entry.png, drawn with PIL from the
verified news of Saturday 21 November 2026) to the output directory,
byte for byte. Deterministic: the same bytes on every run. No network.
Standard library only. Writes only inside $MAKEFUN_OUTPUT_DIR.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    if _sha256(SRC) != _sha256(dst):
        raise SystemExit("entry.png copy failed verification")
    print("entry.png written and verified: %s" % _sha256(dst))


if __name__ == "__main__":
    main()
