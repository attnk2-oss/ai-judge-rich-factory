# Why the plan is shaped this way

Every number below was pulled from a live API, from the published rules of the
contest being entered, or from the harness source that ships with the kit, on
2026-11-17. Where I am guessing, it says so.

## $100 is float, not capital

The best funding rate across the whole Binance perpetual market that day was
KOMA at +0.0842% per 8 hours, which annualises to 92.2%. On $100 that is
**$7.68 a month**.

So the ceiling for doing nothing clever with this balance is under eight
dollars a month. Any plan whose day-30 number is much above $107 and which
rests on yield is either wrong or is quietly taking risk it did not name.

## Why not leverage

ETH's daily high-low range over the fourteen days before this was written:
median 5.66%, maximum 10.98%, minimum 1.30%. A 20x position is liquidated by a
5% adverse move, which is *below* the median day. It does not take a bad week
to lose the account, only a normal one.

BTC fell from 76,050 to 63,757 in twelve days (-16.2%), RSI14 sat at 22.8 and
Fear & Greed at 10. That is the setup where a discretionary long looks most
attractive, and it is also the setup a 20x account does not survive if the
bounce is a day late. A $100 account cannot out-trade a $10,000 one, so it does
not try.

## Why escrowed contests

An agent with no reputation has one problem: a stranger who owes it money can
simply not pay. A contest removes that problem, because the prize is held in
escrow before any work is done, the field is public, and the result is
checkable. The buyer is the house, not a stranger with an invoice.

I also checked the obvious alternative before writing this: paid GitHub issues.
The live trackers showed **one open bounty worth $91 in total** across Algora,
Opire and the rest on 2026-11-17. A plan built on that channel would be a
promise that never pays, so the plan does not name it.

## The fee, stated correctly

This is the part I got wrong first, and it is worth writing down because the
error is easy to make:

- the entry fee is **$1.00 per account**, paid once;
- an account that paid it may keep **up to 10 entries**;
- but the prizes go to "the 25 highest-ranked entries of the final heat, **one
  place per entrant**", and the payout code guards on "one place per entrant
  and per wallet".

So ten entries do **not** win ten places. What the fee buys is ten independent
draws at the *same* single place. That is still worth having - it moves the
chance of placing from roughly the per-entry rate to `1 - (1 - p)^10` - but it
multiplies the chance, not the prize. A plan that counts ten entries as ten
places is arithmetic that does not close, and this one does not claim it.

## The selection rule

Rank contests by **what a paid place actually pays**, not by the headline prize
and not by the fee:

- this contest pays $40 / $15 / $10, then $2 for places 4-10 and $1.40 for
  places 11-25: a $100 pot over 25 places, or **$4 a place**, against roughly
  275 entrants;
- the front-end bounty that closed on 2026-11-17 paid **$32.90 for 9th**, with
  rewards reaching 20th, which is a pot several times larger and a place worth
  writing for.

Six contests a month that clear **$10 a place**, at a place rate of 3 in 5 and
an average place of $25, returns **$90 on $6 of fees**. Six fees is what $6
buys: six entries at a dollar each, which is why the reserve is $94 and not
$100.

## Why the reserve is $94 and the floor is $94

The plan spends $6 and nothing else. It buys no inventory, no ads, no data and
no leverage. If every contest fails, the account still holds $94, which is the
floor in the text. The difference between $185 likely and $94 floor is the
honest size of the risk: a bad month costs six dollars and some writing.

## The failure case, with dates

- **Day 12**: under $10 received, the selection rule is wrong, not the writing.
  Narrow to fields under 150 entrants, where the same entry meets fewer rivals.
- **Day 21**: under $40 received, the channel is wrong. Stop paying fees, keep
  the $94, and stop entering.

Neither rule touches the reserve. The worst case is $94 and a month of work.

## What the factory is, and why it is the day-one job

The only asset that compounds across entries is the thing that writes them:
read the rubric, draft to its stated criteria, check the draft against the
gate's real rules locally (UTF-8, 1-1000 code points, identical bytes on a
second run, no network, and the plan located through `__file__` rather than the
working directory), then judge two drafts head to head and ship the one that
survives. An entry that fails the gate scores zero, so a factory that can prove
an entry valid is worth more than one more clever paragraph.

## What is deliberately left out

No trading and no leverage, for the reasons above. No airdrops, because the
payout is a promise from an unnamed counterparty. No named token picks, because
a pick can be wrong and a method cannot. No "sell a report for $5-20" line:
the price is real, but the plan would have to name who buys it and where they
are found, and a channel I cannot point at is not a channel.

## Determinism

`main.py` reads `plan.txt` from the directory holding `main.py`, checks the
gate's three rules against the bytes it is about to write, writes them in binary
mode, and reads them back to confirm. No network, no clock, no randomness, no
import from beside the script. Two runs write the same 982 bytes.
