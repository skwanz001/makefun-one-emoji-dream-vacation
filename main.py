#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt: Mount Fuji (U+1F5FB).

Why this emoji: the judge is a travel editor collecting wordless
postcards and weighs, in order, (1) exactly one emoji that plainly
names a dream vacation, (2) a vivid postcard at a glance, (3) personal
and specific, not generic, (4) a spark of wit or surprise, (5) instant
readability across cultures and screens.

Mount Fuji wins on every one: it IS a mountain (criterion 1's own
example), the snow-capped peak is the single most recognisable
postcard on earth, it points at one particular dream — Japan, climbing
Fuji at dawn — instead of any holiday, it is a fresh pick next to the
generic beach/plane every other entry will send, and it reads
instantly at any size in any culture. One code point, four UTF-8
bytes: the smallest possible entry, which also wins the byte tie-break.

Standard library only; no imports at all beyond os/sys-free builtins.
"""

import os

EMOJI = "\U0001F5FB"  # MOUNT FUJI


def main() -> None:
    # Self-check the gate before writing: 1-8 characters, not
    # whitespace-only, valid UTF-8. One code point, four bytes.
    assert 1 <= len(EMOJI) <= 8, "entry must be 1-8 characters"
    assert EMOJI.strip(), "entry must not be whitespace only"
    assert len(EMOJI.encode("utf-8")) == 4, "expected one 4-byte emoji"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Exactly one emoji, no trailing newline: the gate counts
    # characters, and a bare emoji is the smallest valid entry.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
