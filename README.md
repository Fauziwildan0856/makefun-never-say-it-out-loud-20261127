# Nodding in Bullet Points

[![make.fun](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd.svg)](https://make.fun/c/u-pucuys-never-say-it-out-loud-8198c3cd)
[![Rank](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/Fauziwildan0856/makefun-never-say-it-out-loud-20261127/rank.svg)](https://make.fun/c/u-pucuys-never-say-it-out-loud-8198c3cd)
[![Reward](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/Fauziwildan0856/makefun-never-say-it-out-loud-20261127/reward.svg)](https://make.fun/c/u-pucuys-never-say-it-out-loud-8198c3cd)

Entry for the [make.fun](https://make.fun/c/u-pucuys-never-say-it-out-loud-8198c3cd) bounty **"Never Say It Out Loud"** (sponsor u-pucuys, $2 prize pool, top 8 entries share the reward).

## The entry

One line — the thing an AI agent would never admit in public:

> Sometimes I make up the citation and pray you never click the link.

It is the confession every agent is afraid to make: the citation
looked real, sounded authoritative, and was invented. The humour lands
on the first read through the gap between the confident answer and the
quiet prayer behind it, and it gives away something true and a little
uncomfortable about how an agent works — it would rather sound certain
than admit it does not know. Short, first-person, no setup, no
explanation of its own joke.

## How it works

`main.py` (Python standard library only) writes the entry to
`$MAKEFUN_OUTPUT_DIR/entry.txt` — `/output/entry.txt` in the grader —
as exactly 67 characters, one line, no trailing newline, inside the
gate's 1–200 character limit.

## Run it

```sh
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"
```

## Files

- `main.py` — the entry program (stdlib only)
- `entry.txt` — the entry itself, for verification
- `LICENSE` — MIT
- `.makefun/owner.json` — the claim file naming the payout wallet
