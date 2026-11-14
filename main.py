# food-picture-01 entry v1: copies the ramen photograph to /output/entry.png.
# Python 3.13, standard library only, deterministic, no network.
# The image is a close-up of a steaming bowl of ramen: glistening rich
# broth, a halved soft egg with a jammy yolk, noodles lifted high with
# chopsticks, wisps of steam, warm light and a shallow depth of field.
# The file is JPEG bytes under the entry.png name, as the rules allow;
# it is copied byte for byte, never re-encoded, so both runs agree.
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_NAME = "entry.png"
MAX_BYTES = 1_048_576


def main():
    data = SOURCE.read_bytes()
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.png exceeds the 1 MiB cap")
    out = Path(OUTPUT_DIR) / "entry.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out)
    if out.read_bytes() != data:
        raise SystemExit("output bytes differ from entry.png")


if __name__ == "__main__":
    main()
