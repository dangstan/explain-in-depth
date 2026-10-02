# Explain in depth

A portable agent skill for turning any bounded topic, process, project or repository into five distinct levels of understanding.

| Depth | Purpose |
| --- | --- |
| D1 | Everyday understanding |
| D2 | Big-picture understanding and judgment |
| D3 | Working understanding |
| D4 | Domain expertise |
| D5 | Detailed visualization or map linked to precise evidence |

**All five depths are mandatory.** Each has its own learning outcome and acceptance criteria. D5 must be a real map of meaningful relationships, not just a source list. Static and interactive maps are both supported.

## Use the skill

This repository is itself the skill folder. Its entry point is [SKILL.md](SKILL.md), using the [Agent Skills format](https://agentskills.io/specification).

Clone or copy it into your agent host's supported skill directory, preserving the folder name explain-in-depth. Discovery and activation depend on the host; this package does not claim universal automatic installation. No installer changes your global configuration.

For a host without skill discovery, ask the agent to read SKILL.md at the cloned path and apply it to your request. Agents need access to the relevant sources and the tools required by the chosen output medium.

Example requests:

- "Use explain-in-depth to evaluate these teaching materials against all five depths."
- "Use explain-in-depth to plan explanations of this repository for beginners through domain experts."
- "Use explain-in-depth to build the next eligible item in this learning plan."
- "Use explain-in-depth to independently review this exact candidate."

Evaluation and planning do not automatically authorize implementation. A complete build includes all five depths; individual sessions and companion presentations can focus on one audience.

## What is included

- A concise skill entry point with evaluate, plan, build and review modes.
- A reusable application plan with audience contracts, source intake, bounded task cards and independent-review criteria.
- A safe initializer that creates a new application folder and refuses to overwrite existing work.
- A plan validator for five-depth coverage, task dependencies, routes and completion evidence.
- Standard-library tests and optional agent UI metadata.

The core instructions are tool-provider independent. Helper scripts require Python 3.9+ and no third-party packages. If Python is unavailable, the templates and documented checks can be applied manually.

## Start an application

Run from this repository, replacing the example destination, track and topic:

```sh
python scripts/init_plan.py ../learning-plan --track topic-explanations --topic "The bounded subject"
```

The generated documents begin at G5-01. After the agent completes the G5-02 blueprint and run/PLAN.json:

```sh
python scripts/validate_plan.py ../learning-plan
```

See [the machine-readable plan contract](references/plan-schema.md). A successful structural check is not evidence that the explanation is true, readable or independently reviewed.

## Review and completion

Each build item has a frozen candidate and a fresh independent reviewer. All five depths must pass their distinct contracts before integration and closure. Actual audience testing and timed rehearsal remain separate evidence categories.

TRACK identifies an application; ITEM identifies an exact task card. Handoff prompts are thin chat pointers, following [the handoff contract](references/handoff.md). No application state belongs in this skill repository.

## Development

```sh
python -m unittest discover -s tests -v
```

The tests exercise missing depths, invalid maps, broken/cyclic dependencies, unsafe paths, premature completion and overwrite refusal.
