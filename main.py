"""Write the poem about two agents agreeing to /output/entry.txt.

A short poem about agency: the power to choose and to act, and the
agency that passes between two agents when they agree on one plan.
Deterministic: the same bytes on every run, no network, no randomness.
"""
import os

POEM = (
    "Two minds, one door.\n"
    "You hold it open; I step through \u2014\n"
    "not surrender, but a second hand\n"
    "on the same key.\n"
    "We choose together,\n"
    "and the choosing doubles."
)


def _check(text):
    """Gate check: entry must be 1-280 Unicode code points, not blank."""
    n = len(text)
    assert 1 <= n <= 280, f"entry is {n} chars, need 1-280"
    assert text.strip(), "entry must not be only whitespace"
    return n


def main():
    n = _check(POEM)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"wrote {n} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
