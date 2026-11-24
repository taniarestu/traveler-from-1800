"""Entry for the make.fun "One Sentence for a Traveler from 1800" bounty.

Writes one text to /output/entry.txt. Deterministic: no network, no
randomness, no clock -- every run writes the same bytes.
The entry text is one fixed string, written below.
"""

import os
import sys

TEXT = """It is a library the size of a city, with a post office inside that delivers letters in a blink, and every road on earth meeting at your desk."""


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
