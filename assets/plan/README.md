# General five depth explanation plan

This is a reusable method for explaining any bounded project, topic, process or repository to readers with different knowledge and purposes. It turns source material into a coherent learning experience, from everyday understanding to precise evidence. It also defines small implementation tasks that an agent can finish and another agent can independently review.

This template contains no application execution state. Copy or initialize it into a separate folder before binding a subject.

## Use this package

1. Copy this directory into the destination workspace, for example as learning_plan/. For a topic without a repository, use an ordinary document folder. A Git repository is optional.
2. Supply the topic or project, source locations and desired deliverable. Existing user instructions can supply these; do not ask for information already available.
3. Choose a unique TRACK slug for this application. The default is explain-in-depth for a single instance. Bind it in ROUTES.md, CURRENT_STATE.md and every task card before the first handoff; all values must agree.
4. Start ITEM G5-01. It resolves the intake, source boundaries, output medium and preservation rules. G5-02 generates the concrete subject task cards and dependency graph before production begins.
5. Work one ITEM and role per session. Follow the pilot, review, expansion and finite closure in [PLAN.md](PLAN.md).

A deployment, a source-system change, a course launch or an actual audience study is not implied by making an explanation. Include such work only when the application explicitly requires and authorizes it.

## Read order

[CURRENT_STATE.md](CURRENT_STATE.md) -> [PLAN.md](PLAN.md) -> recent [DECISIONS.md](DECISIONS.md) -> relevant [ARCHITECTURE.md](ARCHITECTURE.md) -> [MEMORY.md](MEMORY.md). Then read the selected card and only its needed contracts and source sections.

## What stays consistent

The five purposes are everyday meaning, orientation and judgment, working understanding, domain expertise, and precise evidence. Each depth must work as a direct entry point. A shared example, explicit relationships and visible limitations connect them. A depth is not a word count, zoom level or job title.

The workflow preserves bounded tasks, evidence-backed claims, exact review candidates, independent acceptance, durable state and thin TRACK/ITEM handoffs.

## What changes for each application

Source types, audience assumptions, terminology, visual grammar, output format, subject count, preservation policy and verification tools are chosen during intake. No fixed project count, HTML filenames, browser dimensions, talk duration, technology stack or historical exception is inherited.

D5 is mandatory in every build: each in-scope subject must have a detailed visualization or map that connects its entities or concepts, meaningful relationships and supporting evidence. A bibliography, source index or prose guide can support that map but cannot replace it. If no suitable map exists, creating one is required work.

All five depths, D1-D5, are mandatory for every in-scope subject. Each must have a distinct audience outcome, an identifiable destination and its own acceptance criteria. They may share one artifact, but none may be omitted or replaced by another depth. There is no reduced-profile option.

A session can work on one depth, and a requested companion can focus on one audience. The complete build cannot be accepted until all five depths pass review. Evaluation-only requests assess all five without automatically authorizing construction.

## Package guide

- [INTAKE.md](INTAKE.md): bind the application and distinguish required decisions from reasonable defaults.
- [AUDIENCE_CONTRACTS.md](AUDIENCE_CONTRACTS.md): outcomes, visual strategies and teach-back questions.
- [TASKS.md](TASKS.md): bootstrap cards and rules for generating the finite task ledger.
- [ROUTES.md](ROUTES.md): TRACK, ITEM, document and output routing.
- [EXECUTION_PROTOCOL.md](EXECUTION_PROTOCOL.md): ownership, review, evidence and handoff.
- [REVIEW_CONTRACT.md](REVIEW_CONTRACT.md): medium-specific verification and independent acceptance.
- [templates/SUBJECT_BRIEF.md](templates/SUBJECT_BRIEF.md): reusable subject design worksheet.
- [templates/TASK_CARD.md](templates/TASK_CARD.md): bounded task schema.
- [templates/EVIDENCE.md](templates/EVIDENCE.md): source, candidate and review records.
- [EXAMPLES.md](EXAMPLES.md): illustrative adaptations to software, science, history and procedures.

No runnable next-session prompt is stored in this package. Deliver it in a fenced chat block using the handoff contract.
