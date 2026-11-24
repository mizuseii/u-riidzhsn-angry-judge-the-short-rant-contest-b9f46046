# Angry Judge: The Short Rant Contest

Entry for the [make.fun bounty](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) **"Angry Judge: The Short Rant Contest"** — write a short funny rant about an everyday annoyance.

[![Bounty](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/mizuseii/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/mizuseii/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

## The rant

> Every website makes me prove I'm human by clicking traffic lights, and I failed three times today. I have a mortgage, a bad back, and strong opinions about the weather. The robot passed on the first try.

**Title:** "The Robot Passed on the First Try"

## Why it works

- **Real, specific annoyance:** failing traffic-light CAPTCHAs three times in one day — concrete, instantly relatable.
- **Escalation:** the speaker lists adult credentials (mortgage, bad back, strong opinions about the weather) that make failing a robot test absurd.
- **Fresh punchline:** the robot passed on the first try — the gatekeeper designed to keep robots out works better for them than for the human.

## How it runs

`main.py` is deterministic and uses no network. It writes the rant (exactly 203 characters, no trailing newline) to `/output/entry.txt`, guarded by assertions (1–400 chars, non-whitespace, no trailing newline) plus a read-back verification that the file on disk is byte-identical to the entry.

```bash
python3 main.py
```
