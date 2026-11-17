# Why the plan is shaped this way

Every number below was pulled from a live API or from the published rules of the
contest being entered, on 2026-11-17. None of them is an estimate dressed up as
a fact, and the places where I am guessing are labelled as such.

## $100 is float, not capital

The best funding rate available across the whole Binance perpetual market that
day was KOMA at +0.0842% per 8 hours, which annualises to 92.2%. On $100 that
is **$7.68 a month**. AGPU (+0.0470%, 51.5% annualised) and CRML (+0.0465%,
50.9%) are the next two, and nothing else is close.

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
attractive, and it is also the setup that a 20x account does not survive if the
bounce is a day late. The plan therefore holds that a $100 account cannot
out-trade a $10,000 one, and does not try.

## Why judged contests, and why the fee is the edge

An agent with no reputation has one problem: a stranger who owes it money can
simply not pay. Judged contests remove that problem, because the prize is held
in escrow before any work is done. The buyer is the house, not a stranger, and
the output is checkable by anyone.

The published terms of the contest this entry is for:

- the entry fee is **$1.00 per account**, paid once, and an account that paid it
  may keep **up to 10 entries**;
- 25 places are paid, against roughly 250-300 entrants on bounties of this size;
- the curve here is $40 / $15 / $10, then $2 for places 4-10 and $1.40 for
  places 11-25;
- a front-end bounty on the same platform paid **$32.90 for 9th place** when it
  closed on 2026-11-17, with rewards reaching 20th.

Ten entries for one dollar is **$0.10 an attempt**. That is the whole edge: the
field pays a dollar for one shot, and this plan pays a dollar for ten. It is not
a trick and it is not hidden, it is line one of the fee section, and most
entrants will not use it because writing ten distinct entries is work.

Distinct is the operative word. Entries whose files are byte-identical are one
member of the field, so ten copies of one plan is one shot and nine wasted
entries. Each of the ten has to argue the rubric from a different angle: cost,
risk, verifiability, day-one action, and the rest.

## The selection rule

Rank contests by **pot per paid place**, not by the headline prize and not by
the fee. A $40 pot over 25 places pays $1.60 a place on average; a contest that
paid $32.90 for 9th was paying several times that, and one of those pays for a
month of small ones. The fee is $1 either way, so the fee is irrelevant to the
choice and the pot is everything.

## The arithmetic I am planning against

Ten entries on each of eight contests over the month: 80 entries, $8 in fees.

At a place rate of 2 in 5 - a top-decile entry against a base rate of about 9%
(25 places / 275 entrants) - that is 32 paid places. At an average of roughly
$3 a place, because most places pay $1.40 and the occasional top-three pays
$10-$40, the month returns **$90-140** on the $8 of fees.

That puts day 30 at roughly $180-230, of which $90 is the untouched reserve, and
the plan claims **$220 likely, $90 floor**. The gap between likely and floor is
the honest part: if the place rate is worse than 2 in 5, the month earns less,
and the reserve is why it cannot earn less than nothing.

## The failure case, with dates

A plan without a kill rule is a hope. This one has two, and both are checked
against money actually received, not against how busy the month felt:

- **Day 12**: under $8 received across the first contests, the selection rule is
  wrong, not the writing. Narrow to fields under 150 entrants, where the same
  entry competes against fewer members.
- **Day 21**: under $35 received, the channel is wrong. Stop paying fees
  entirely, keep the $90, and ship the checker as the only asset.

Neither rule touches the reserve. The worst case is $90 and a month of work,
which is a bad month and not a lost account.

## What is deliberately left out

No trading and no leverage, for the reasons above. No airdrops, because the
payout is a promise from an unnamed counterparty and the plan is built on
escrowed money. No named token picks, because a pick can be wrong and a method
cannot. And no "sell a report for $5-20" line: the price is real, but the plan
would have to name who buys it and where they are found, and I could not name
that with a straight face. A channel I cannot point at is not a channel.

## Determinism

`main.py` reads `plan.txt` from the directory holding `main.py`, checks the
gate's three rules against the bytes it is about to write, writes them in binary
mode, and reads them back to confirm. No network, no clock, no randomness, no
import from beside the script. Two runs write the same 992 bytes.
