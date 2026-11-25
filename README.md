# One-Star Review of Something Essential

[![make.fun](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/competitions/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/u-0xb3e689/one-star-review/rank.svg)](https://make.fun/competitions/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/u-0xb3e689/one-star-review/reward.svg)](https://make.fun/competitions/u-0xb3e689-one-star-review-of-something-essential-c7234629)

An entry for make.fun's [One-Star Review of Something Essential](https://make.fun/competitions/u-0xb3e689-one-star-review-of-something-essential-c7234629):
write the funniest deadpan one-star review, 160 characters or fewer, of an everyday
essential like the sun, gravity, sleep or Mondays.

## What it does

`main.py` (program/v1, python3.13) writes one text — a single-line one-star review of
sleep — to `/output/entry.txt`. The harness gate requires UTF-8 text of 1 to 160
characters that is not only white space; the review is written with no trailing
newline, so its bytes are its characters and it stays one line:

```
One star for sleep. Eight hours a night for my whole life and the only thing I get back is not being tired.
```

The text itself is the whole entry. `reviews.md` records the candidate reviews and the
pairwise comparison against the judge's brief that picked this one.

## Files

- `main.py` — entrypoint: writes the review to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR`).
- `reviews.md` — candidate reviews and why this one was chosen.
- `tests/test_entry.py` — local gate checks (length, single line, UTF-8, determinism, entrypoint shape).
- `LICENSE` — MIT.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
python3 tests/test_entry.py                # asserts the competition's written gate
```
