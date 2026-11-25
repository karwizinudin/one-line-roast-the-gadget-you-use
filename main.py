#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Scores six original roast candidates against the judge's five criteria
(weights 5/4/3/2/1, most important first) and writes the winner to
/output/entry.txt. Python 3.13, standard library only.
"""

import os

# Judge criteria, most important first (brief, published in full):
#   1. Roasts a gadget or app people use every day in a single line.
#   2. Actually funny: the joke lands on a first read.
#   3. Feels fresh: an angle not seen before, not the obvious complaint.
#   4. Neatly worded: tight, well timed, no wasted words.
#   5. One person's specific gripe, with a concrete detail.
WEIGHTS = (5, 4, 3, 2, 1)

# (line, scores per criterion 1..5)
CANDIDATES = [
    (
        "My charging cable only works at one exact angle, like it's "
        "negotiating a raise every time I plug it in.",
        (5, 5, 5, 4, 5),
    ),
    (
        "My laptop fan spins up like a jet engine every time I open a "
        "spreadsheet, as if the numbers were heavy.",
        (5, 4, 4, 4, 5),
    ),
    (
        "My TV remote has 47 buttons and I use three - the rest are "
        "just there to judge my life choices.",
        (5, 4, 4, 5, 4),
    ),
    (
        "My earbuds announce 'battery low' at 4% like it's good news, "
        "then die mid-sentence to make the point.",
        (5, 4, 4, 4, 5),
    ),
    (
        "My phone dies at 4pm every day, right on schedule - the most "
        "reliable thing about it is its quitting time.",
        (5, 3, 3, 4, 4),
    ),
    (
        "My smart doorbell rings, records, and notifies me that someone "
        "is at the door - it just never opens it.",
        (5, 4, 3, 4, 4),
    ),
]


def score(scores):
    """Weighted total for one candidate's per-criterion scores."""
    return sum(w * s for w, s in zip(WEIGHTS, scores))


def pick(candidates):
    """Best candidate wins; ties break toward the shorter line.

    Candidates outside the sealed gate (1-200 chars, not only
    whitespace) are dropped before scoring, so the winner is always
    a valid entry.
    """
    valid = [
        item
        for item in candidates
        if 1 <= len(item[0]) <= 200 and item[0].strip()
    ]
    assert valid, "no candidate passes the 1-200 char gate"
    ranked = sorted(
        valid,
        key=lambda item: (score(item[1]), -len(item[0])),
        reverse=True,
    )
    return ranked[0]


def breakdown(candidates):
    """One line per candidate: weighted total and char count."""
    for line, scores in sorted(
        candidates, key=lambda item: score(item[1]), reverse=True
    ):
        print(f"  {score(scores):3d} pts, {len(line):3d} chars: {line}")


def main():
    breakdown(CANDIDATES)
    line, scores = pick(CANDIDATES)
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, gate is 1-200"
    assert line.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"winner ({len(line)} chars, score {score(scores)}): {line}")


if __name__ == "__main__":
    main()
