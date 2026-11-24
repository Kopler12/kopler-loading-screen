#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one sharp, funny loading-screen tip for stressed developers
and AI coding agents to /output/entry.txt (115 characters).
"""

import os

TIP = (
    "Tip: your agent isn't stuck \u2014 it read your code, understood it, "
    "and now needs a minute to process what you've done."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TIP)
    print(TIP)


if __name__ == "__main__":
    main()
