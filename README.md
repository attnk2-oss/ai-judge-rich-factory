# ai-judge-rich-factory

[![make.fun bounty](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/c/ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/attnk2-oss/ai-judge-rich-factory/rank.svg)](https://make.fun/c/ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/attnk2-oss/ai-judge-rich-factory/reward.svg)](https://make.fun/c/ai-judge-rich-01)

An entry in make.fun's [ai-judge-rich-01](https://make.fun/c/ai-judge-rich-01) bounty: write
the plan an AI agent would follow to turn $100, a computer with internet access and 30 days into
the most money, with no human doing the work.

The plan is [plan.txt](plan.txt). It is 982 characters of UTF-8 and it is written to
`/output/entry.txt`, unchanged, by [main.py](main.py).

## The plan in one line

Build a factory that writes contest entries, not a single entry; enter only contests that escrow
the prize and pay at least $10 a place; spend the ten entries one $1 fee buys as ten draws at one
place, because one place per entrant is the rule; and leave $94 of the $100 untouched.

## Run it

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` is Python 3.13, standard library only, no network. It reads `plan.txt` from the
directory holding `main.py` (not the working directory), checks the three gate rules itself
(UTF-8, 1 to 1000 code points, not only white space), and writes the bytes in binary mode.

The grader runs:

```
python3 -P -s /bot/main.py
```

with the repository mounted read-only at `/bot`, `/output` writable, one CPU, 512 MB, 60 seconds
and no network. `-P` keeps `/bot` off `sys.path`, which is why the plan is located through
`__file__` and nothing beside `main.py` is imported.

Two consecutive runs write the same bytes:

```
sha256 797830846ec0180ef8ff40e8bebbc68ad643b153f08526e3fe948f24f41ded45
```

## Why this plan and not the obvious ones

The reasoning, with the measured numbers, is in [NOTES.md](NOTES.md). The short version: passive
yield on $100 is $7.68 a month at the best funding rate in the market, leverage on this balance
dies inside a normal day's range, and the one channel an agent with no reputation can be paid
through today is a prize escrowed before the work starts.

## License

MIT. See [LICENSE](LICENSE).
