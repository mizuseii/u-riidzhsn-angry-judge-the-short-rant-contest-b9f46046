#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry generator.

Writes the rant (exactly 203 chars, no trailing newline) to /output/entry.txt.

The joke's structure: a CAPTCHA rant built as a three-beat escalation.
1. The setup is specific and relatable — failing traffic-light CAPTCHAs
   three times in one day, a concrete everyday annoyance everyone knows.
2. The middle beat reframes the speaker as a fully credentialed adult
   ("a mortgage, a bad back, and strong opinions about the weather") —
   the absurd contrast between real-life competence and failing a test
   meant for robots.
3. The punchline inverts the premise: the robot passed on the first try,
   so the test that exists to keep robots out is better at admitting them
   than the human. Sharp, economical, one fresh angle: the gatekeeper
   works backwards.
"""

import os

ENTRY = (
    "Every website makes me prove I'm human by clicking traffic lights, "
    "and I failed three times today. I have a mortgage, a bad back, and "
    "strong opinions about the weather. The robot passed on the first try."
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    # Gate guard: /output/entry.txt must be UTF-8 text, 1-400 chars,
    # not only whitespace.
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= 400, f"entry length {len(text)} outside 1-400"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {OUT_PATH} ({len(text)} chars)")


if __name__ == "__main__":
    main()
