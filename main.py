#!/usr/bin/env python3
"""Write one office joke (a single line) to /output/entry.txt."""

import os

JOKE = (
    "Our standup is twelve people saying 'same as yesterday' in "
    "alphabetical order, so I legally changed my name to Aaron."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
