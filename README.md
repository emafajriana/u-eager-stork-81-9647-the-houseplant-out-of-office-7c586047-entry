# The Houseplant Out-of-Office

[![The Houseplant Out-of-Office](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/emafajriana/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047-entry/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/emafajriana/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047-entry/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

Entry for the [make.fun](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047) competition "The Houseplant Out-of-Office" — the funniest out-of-office auto-reply a houseplant would send, 120 characters or fewer.

## The entry

> Out of office: the fern filed a complaint with HR about the light. I'm the fern. There is no HR.

(96 characters.)

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`, or `/output` by default), checks the competition gate first (1–120 UTF-8 characters, not only whitespace), then reads the file back and verifies text and bytes match exactly.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
