#!/usr/bin/env python3
"""The Funniest Honest Appliance Error: one line, at most 200 characters.

The program writes a single honest error message from a washing machine
whose drain pump has failed to /output/entry.txt. It uses only the Python
standard library, makes no network calls, and always writes the same bytes.
"""

import os

LINE = (
    "WASHER ERROR: Drain pump failed. The water is staying. "
    "So are your socks. I spin clothes, not oceans."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
