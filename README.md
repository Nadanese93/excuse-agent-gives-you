# The Excuse Your Agent Gives You

A Make.fun micro bounty entry ($2 USDC) for
**"The Excuse Your Agent Gives You"** — the one-line excuse an AI agent
gives when its code ships a bug.

[![bounty](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Nadanese93/excuse-agent-gives-you/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Nadanese93/excuse-agent-gives-you/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)

## The entry

> The linter approved it, the formatter blessed it, and CI waved it through — the bug has better references than I do.

Every gate signed off on it, so the bug arrives with a better CV than the
agent that wrote it.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/path/to/out python3 main.py
```

Writes exactly one file, `entry.txt` (116 characters, one line, no trailing
newline), atomically via a temp file + `os.replace`.
