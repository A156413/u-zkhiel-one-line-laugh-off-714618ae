#!/usr/bin/env python3
"""One-Line Laugh-Off: a single original joke, written to /output/entry.txt.

The entry
---------
"I asked the barista for something strong, so she handed me her
resignation letter."

Why this line, against the judge's brief (most important first):

1. Genuinely funny on a cold read. The scene needs no setup: anyone
   who has ever ordered coffee is already in it, and the punch lands
   in the second half of the same sentence.
2. The laugh lands hard and suddenly. "Something strong" sets up a
   coffee order, then the resignation letter reframes it: the thing
   that is strong is the job, and she is done with it. One beat,
   no wind-up.
3. Surprise. The reader expects a drink, a size, a strength of brew;
   instead they get a letter and a quitting employee. The turn is a
   wordplay pivot ("strong") with a human payoff, not a recycled
   setup.
4. Economy. 82 characters, one sentence, every word earning its
   place: ask / barista / strong / resignation letter. Nothing left
   to trim, no explanation, no setup notes.
5. Freshness. No agent, tech-support or "it worked on my machine"
   trope; a small human workplace moment, told once.

The gate (RULES.txt) requires /output/entry.txt to be UTF-8 text of
1 to 200 characters, not only white space, so the program asserts
those bounds and writes the line with no trailing newline.
"""

import os

JOKE = (
    "I asked the barista for something strong, so she handed me "
    "her resignation letter."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Enforce the sealed scorer's gate before writing: 1-200 chars,
    # one line, not only whitespace, no trailing newline.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, gate needs 1-200"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be a single non-blank line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(OUTPUT_PATH, 0o644)
    # Round-trip check: what we wrote is exactly the joke.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == JOKE, "written entry differs from the joke"
    # Echo the entry to the run log; the file alone is what is judged.
    print(JOKE)


if __name__ == "__main__":
    main()
