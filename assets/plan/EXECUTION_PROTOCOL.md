# Bounded agent execution

## Authority and context

Apply the user's request and destination instructions. This framework supplies a workflow, not authority to execute an unrelated source system. Read CURRENT_STATE, PLAN, recent DECISIONS, relevant ARCHITECTURE and MEMORY; then only the selected card, contracts and source sections needed for that card.

Use the application workspace explicitly. Preserve other users' or agents' work. Existing permission and publication requirements remain in effect; do not add approval ceremonies for routine authorized work.

## One item and role

At session start, resolve TRACK through ROUTES.md and ITEM through TASKS.md. Confirm accepted prerequisites, role, candidate, owned paths and available tools. Re-read ownership before mutation. If another writer owns the scope, stop competing edits and record the conflict.

A builder creates one bounded candidate and its evidence. A separate fresh reviewer accepts or returns it. A reviewer does not repair and certify the same candidate. Supported read-only source analysis can help, but advice is not acceptance.

Each session stays on its assigned ITEM. After acceptance, update state and hand off the next eligible item to a fresh session. Review and repair retain the candidate's ITEM with the role recorded in state. If review cannot be dispatched, leave awaiting_review and provide the concrete handoff; never claim review occurred.

## Builder sequence

1. Verify the task preconditions, scope and source support.
2. State the audience question, essential relationship, chosen example, omitted detail and expected teach-back.
3. Implement only the card's deliverables.
4. Run relevant source, preservation, render and behavior checks; inspect the actual artifact.
5. Freeze the candidate as a scoped commit, exact file hash manifest or identified document version/export. Do not include unrelated work.
6. Record actual observations and missing evidence under evidence/<ITEM>/attempt-<n>/.
7. Set awaiting_review and update CURRENT_STATE with pointers. Deliver the next prompt in chat.

Preparation and documentation cards also need exact candidates and independent review appropriate to their deliverables. G5-PILOT and G5-QA are themselves fresh reviewer items; they do not require a reviewer-of-reviewer.

## Ledger and transitions

G5-01 creates run/STATUS.json. Use a top-level track and tasks array, with each record keyed by id. G5-02 creates run/PLAN.json for the concrete dependency graph and five-depth coverage; follow PLAN_SCHEMA.md. Keep runtime records synchronized with the accepted plan, including candidate, review_candidate, verdict and review path for completion checks. Store track, item, role, status, attempt, owner/session if known, requires, candidate, build evidence, review evidence, verdict and next action. For unresolved bootstrap edges, store an explicit unresolved field; never interpret absence as acceptance. G5-02 resolves these before production.

Allowed statuses: pending, in_progress, awaiting_review, accepted, revise, blocked. A builder may move pending or revise to in_progress, then awaiting_review. Only an independent ACCEPT moves a production item to accepted. REVISE returns the same item to a builder. INCONCLUSIVE leaves it blocked on named missing evidence. Keep all attempts.

Uxx-D1 through Uxx-D5 cards and accepted candidates are mandatory for every in-scope subject. Each depth must satisfy its distinct audience contract, with an actual detailed map at D5. Missing, inadequate or unreviewed depths block subject integration, pilot/final acceptance and closure. A source index does not substitute for the map; the map does not substitute for D1-D4.

The final documentation card remains awaiting_review until independently accepted; only then mark the track complete. Record ownership transitions honestly. A mutable ledger is coordination metadata, not a secure distributed lock.

## Decisions and stopping

Make routine choices autonomously within the application contract. Record consequential choices in DECISIONS. Ask only for unresolved matters that materially change scope or correctness. Work on independent portions while waiting.

Use the finite attempt limit chosen at intake. At the default limit of three unresolved review cycles, stop the item with concrete defects or missing evidence. Do not create an indefinite successor chain. A user-authorized requirement change can revise the plan without rewriting old evidence.

End a session at a coherent boundary before context becomes unreliable. Save partial work as partial; compaction or a self-check is not independent review.

## Thin handoff contract

Deliver a fenced code block in chat, not a saved prompt file. Its first line is verbatim "Operate in journal-mode." Immediately below, place TRACK with the resolved literal slug, then ITEM with the exact eligible ledger ID.

Include one role/workspace/plan orientation line. Route the reader to CURRENT_STATE's Current plan and Active runs, PLAN, recent DECISIONS, the relevant ARCHITECTURE section and MEMORY, in that order. Include the instruction "Derive your task from THOSE, not from this prompt."

Do not carry state, metrics, results, next-step recipes or copied rules in the prompt. Put missing durable knowledge into the documents and point there. Before delivery, verify the named card exists, dependencies and role are eligible, and all document paths resolve. A prompt is not proof of dispatch or external track registration.
