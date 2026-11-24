"""Dog-ate-my-homework excuse entry.

Writes one line -- the excuse a dog gives after being caught eating
the homework -- to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

The line is the duel-tested winner of eight drafts: the dog turned
the homework in early, inside himself, two minutes before it was due.
"""

import os

# Duel winner (8 drafts, 28 pairs x 2 orders): deadpan dog logic --
# eating the homework before the deadline counts as turning it in.
EXCUSE = "It was due at 8. It's inside me at 7:58. Technically early."


def validate(text: str) -> None:
    """Self-check: the gate wants UTF-8 text, 1-200 chars, one line."""
    assert 1 <= len(text) <= 200, "excuse must be 1-200 characters"
    assert text == text.strip(), "no leading or trailing whitespace"
    assert "\n" not in text and "\r" not in text, "exactly one line"
    assert text.strip(), "not whitespace only"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    validate(EXCUSE)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
