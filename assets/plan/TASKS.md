# Task inventory and generation rules

## Bootstrap cards

TRACK resolves to the exact slug in ROUTES.md. These cards are pending definitions, not accepted work.

| ITEM | Deliverable | Requires |
| --- | --- | --- |
| [G5-01](tasks/G5-01.md) | Bound intake, sources, preservation and initial ledger | User application context; no task dependency |
| [G5-02](tasks/G5-02.md) | Learning blueprint and concrete production graph | G5-01 accepted |
| [G5-03](tasks/G5-03.md) | Minimal medium scaffolding and verification method | G5-02 accepted |
| [G5-PILOT](tasks/G5-PILOT.md) | Independent whole-pilot review | Exact last pilot card, bound by G5-02 |
| [G5-QA](tasks/G5-QA.md) | Independent full-scope review | Exact final production card and G5-PILOT, bound by G5-02 |
| [G5-CLOSE](tasks/G5-CLOSE.md) | Final report and finite closure | G5-QA accepted |

G5-01 initializes only these known records; unresolved dependencies are explicitly unresolved and not eligible. G5-02 replaces them with exact existing IDs, creates every production card, updates the ledger and validates the entire graph before acceptance. No unresolved dependency, template token or unlisted production task may reach G5-03.

## Generated subject cards

Assign stable U01, U02 and subsequent subject IDs to a finite inventory. Select U01 as pilot. Record each ID's subject in run/OUTPUTS.md. Use the following card recipes and the [task template](templates/TASK_CARD.md); these recipes are not dispatchable cards until instantiated.

| ITEM pattern | Small steps | Deliverable | Acceptance |
| --- | --- | --- | --- |
| Uxx-D5 | Bound coverage; inspect or create the detailed map; label entities and relationships; attach provenance; trace a representative path; verify rendering and source access | Mandatory detailed visualization or map with investigation guidance and precise source references | Map satisfies the D5 audience contract, covers declared scope, supports a trace and evidence lookup, shows uncertainty and preserves originals |
| Uxx-D1 | Choose concrete case; define essential terms; visualize meaning; qualify one limit; check direct entry | Everyday explanation | Newcomer-oriented teach-back addresses what it is, why it matters and what it does not imply |
| Uxx-D2 | Map major relationships; identify value or significance; expose uncertainty and tradeoffs | Orientation view | Reader explains the whole and makes a relevant distinction or judgment |
| Uxx-D3 | Work an ordinary case; explain transitions; show a variation; assign actors only where real | Working explanation | Reader traces the mechanism or reasoning and explains a changed case |
| Uxx-D4 | Curate domain distinctions; expose assumptions; compare a boundary case; link deeper evidence | Expert view | Reader predicts or defends a new case using stated evidence and limits |
| Uxx-INTEGRATE | Align terminology and example; add direct entries and transitions; verify all five depth destinations | Coherent subject experience | All five purposes are findable, distinct and independently understandable |
| Uxx-C01 and later | Bind one requested companion and audience; adapt its narrative; verify the chosen format | Named talk, exercise, summary or other requested companion | Its own bounded audience and format criteria; timing claims require rehearsal |

For every subject, the mandatory production chain is D5 -> D1 -> D2 -> D3 -> D4 -> INTEGRATE -> each requested companion. Production starts with the detailed map to ground the explanations; the audience-facing order remains D1 through D5. Each subject must have a concrete Uxx-D5 card, even when reusing an existing map: that card verifies suitability, guidance, preservation and evidence access.

Generate a concrete Uxx-D1, Uxx-D2, Uxx-D3, Uxx-D4 and Uxx-D5 card for every subject; no depth can be omitted. If a depth is split into smaller cards, retain explicit coverage and acceptance of that depth in the task graph. All five must be accepted before Uxx-INTEGRATE can be accepted. The internal source ledger remains mandatory and supports the visualization; it is not the learner-facing D5 deliverable. If later lessons expose a map defect, repair the D5 item and re-review affected dependencies before integration.

U01's first card depends on G5-03. G5-PILOT depends on the pilot's actual final card. U02's first card depends on G5-PILOT; each later subject depends on the previous subject's final card. G5-QA depends on G5-PILOT and the actual final production card (the pilot's last card if there is only one subject).

Default to a serial graph for one writer. An application may define parallel work only with explicit nonoverlapping ownership and integration dependencies.

## Bound the work

Generate one card per independently reviewable outcome. If a card cannot fit a bounded session, split it before dispatch into stable IDs such as U01-D4-A and U01-D4-B, and update all dependent edges. Do not hide multiple large implementations inside a checklist.

Each card names exact owned files or sections, required source sections, deliverables, acceptance evidence, exclusions and stopping conditions. Shared conventions may be referenced rather than repeated. Use targeted context; do not load every subject's sources.

## Acceptance and repairs

Only ACCEPT of the exact candidate satisfies a dependency. REVISE or INCONCLUSIVE does not. A repair retains the original ITEM and records a new attempt. If a repair invalidates later work, record affected candidates and re-review before accepting final integration.

Scope changes after blueprint acceptance require dated decisions and graph updates with review of the changed plan. Already accepted IDs and verdict history remain intact.
