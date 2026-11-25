"""One-star review of something essential: gravity.

Writes a single deadpan one-star review to /output/entry.txt.

Why gravity: the brief asks for the sharpest true grievance in an
everyday essential, held deadpan, with the sting arriving in the last
few words. Gravity's grievance is one everyone has lived but never
filed: it shows up every day without fail and has never once caught
anything you dropped. The review stays flat throughout -- no winking,
no exclamation marks -- and the turn lands in the final sentence,
which reads like a performance review: flawless attendance, zero
helpfulness.
"""

import os

REVIEW = (
    "One star. Gravity has never missed a day of work and has never "
    "once caught anything I dropped. Flawless attendance, zero helpfulness."
)

# One line, one joke: the complaint is filed in earnest against a thing
# that cannot be fixed, exactly as the brief demands. No second joke
# crowds the first, and the review stays within the 160-character gate.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(f"wrote {path}: {REVIEW} ({len(REVIEW)} chars)")


if __name__ == "__main__":
    main()
