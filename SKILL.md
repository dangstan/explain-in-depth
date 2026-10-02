---
name: explain-in-depth
description: Evaluate, plan, build, or independently review explanations of a topic, process, project, or repository across five required audience depths, ending in a detailed evidence-linked map. Use for structured learning experiences and progressive visual explanations, not ordinary short factual answers.
metadata:
  version: "1.0.0"
---

# Explain in depth

Create accurate explanations for five distinct reader purposes. Every complete build must contain all five depths for every in-scope subject:

1. D1: everyday understanding.
2. D2: big-picture understanding and judgment.
3. D3: working understanding.
4. D4: domain expertise.
5. D5: a detailed visualization or map with precise supporting evidence.

The subject and medium can vary; depth coverage cannot. A source list or prose guide does not replace the D5 map. Separate files are optional; distinct learning outcomes, destinations and acceptance evidence are required.

## Choose the requested mode

- **Evaluate:** inspect existing material against all five contracts. Report observed gaps, including missing depths. Do not implement changes unless requested.
- **Plan:** bind sources, readers, medium and scope; generate a finite plan and exact task cards. Do not claim implementation or review has occurred.
- **Build:** implement the selected eligible ITEM from the application plan. Establish the plan first when none exists. Work one bounded item and role per session.
- **Review:** independently inspect an exact candidate against its card and relevant depth contract. Do not repair and certify your own work.

Infer the mode from the request. A brief request for a single explanation does not need this whole workflow unless the user invokes it. A session or companion can focus on one depth, but cannot claim the complete build finished.

## Load only relevant resources

For every mode, read [audience contracts](assets/plan/AUDIENCE_CONTRACTS.md). Then:

- Evaluate or review: read [review requirements](assets/plan/REVIEW_CONTRACT.md) and the relevant subject/source sections.
- Plan a new application: read [intake](assets/plan/INTAKE.md), [task generation](assets/plan/TASKS.md), and [plan schema](references/plan-schema.md).
- Build or continue: start from the application's CURRENT_STATE, PLAN, recent DECISIONS, relevant ARCHITECTURE and MEMORY, then the one selected card. Follow its [execution protocol](assets/plan/EXECUTION_PROTOCOL.md).
- When domain adaptation is unclear, consult [examples](assets/plan/EXAMPLES.md). Do not load every example, task or source into each context.

## Bind an application

Use the user's existing brief before asking questions. Resolve the subject, source authority, reader assumptions, output medium, boundaries, protected artifacts and available verification tools. Ask for missing information only when it changes scope or prevents correct work.

Create application state outside this skill directory. Use the portable standard-library helper when Python 3.9+ is available:

    python scripts/init_plan.py /absolute/path/to/learning-plan --track topic-explanations --topic "The bounded subject"

The destination must not exist. Without Python, copy assets/plan to a new application folder and bind the TRACK and topic in the documents manually. Do not copy prior applications' state.

G5-01 binds sources and intake. G5-02 produces the concrete finite task graph, all five depth mappings and run/PLAN.json using the schema. Validate before production:

    python scripts/validate_plan.py /absolute/path/to/learning-plan

The scripts check structural invariants, not truth, instructional quality or actual review independence. Without the runtime, inspect the same invariants manually and report that the automated check was not run.

## Teach the subject rather than a fixed software model

Preserve a coherent example and direct-entry context across depths. Define essential concepts visibly. Label meaningful relationships and distinguish causation, chronology, dependency, association and inference.

D4 means domain expertise, not necessarily software. D5 maps the detailed in-scope structure: components, concepts, actors, events, states, arguments or proof dependencies as appropriate. Build a new map when no suitable one exists. Preserve any designated immutable originals; create a supplementary map instead of silently modifying them.

Use static, multi-panel or interactive visuals according to the medium. A changed case must teach a consequence; it need not be a control. Do not invent facts or relationships to make a diagram look complete. Trace material claims to precise evidence and expose uncertainty.

## Accept and hand off honestly

Use distinct functional/rendering, source-fidelity and instructional criteria. Report expert judgment, actual audience testing and timed rehearsal separately. Missing rendering or reviewer capabilities are limits, not passes.

A separate fresh reviewer must inspect an exact candidate before acceptance. If the host cannot dispatch that reviewer, prepare the candidate and leave it awaiting review. Do not invoke a model service or modify host configuration merely to manufacture an independent review.

All five depths must be independently accepted before subject integration and final closure. Run the structural completion check only when appropriate:

    python scripts/validate_plan.py /absolute/path/to/learning-plan --complete

Use [the handoff contract](references/handoff.md): a fenced chat prompt with the exact journal-mode opener, literal TRACK and eligible ITEM, and document pointers. Store state in the application documents. This convention does not install hooks, register a track, grant permissions or prove dispatch.

Respect the user's scope and the destination's instructions. The skill does not itself authorize upstream execution, purchases, source changes or publication.
