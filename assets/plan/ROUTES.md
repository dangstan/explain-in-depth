# Track and document routes

## Track identity

Default TRACK: explain-in-depth

This names the reusable application instance, not a registered runtime service. When copying into a new workspace, select a unique slug if needed and record it here, in CURRENT_STATE.md and in each task card before dispatch. Generated cards use this exact value; handoff prompts always contain the resolved literal slug.

ITEM is an exact ID in TASKS.md resolving to tasks/<ITEM>.md. First ITEM: G5-01. Review and repair retain that ID. The role assignment is authoritative in durable state; the prompt may name that role for orientation. Attempts, candidates and status stay in durable state, not in the handoff prompt.

## Document routing

All paths below are relative to this plan directory.

| Purpose | Path |
| --- | --- |
| State | CURRENT_STATE.md |
| Plan | PLAN.md |
| Decisions | DECISIONS.md |
| Architecture | ARCHITECTURE.md |
| Memory | MEMORY.md |
| Ordered task inventory | TASKS.md |
| Individual task | tasks/<ITEM>.md |
| Execution status | run/STATUS.json, created by G5-01 |
| Application intake | run/INTAKE.md |
| Output and source destinations | run/OUTPUTS.md, created by G5-02 |
| Subject design | subjects/<SUBJECT_ID>.md, created by G5-02 |
| Candidate evidence | evidence/<ITEM>/attempt-<n>/ |
| Final report | run/FINAL_REPORT.md |

G5-01 records the absolute workspace and plan-directory paths in CURRENT_STATE.md. The bootstrap ledger is not an external orchestration registration. Honor host-specific registration requirements separately if the user invokes such an orchestrator.

## Audience destinations

G5-02 replaces conceptual destinations with exact files, anchors, slides, sections or document IDs in run/OUTPUTS.md. Every one of D1-D5 has a meaningful direct entry point and an explicit card mapping for every subject. Record the exact detailed-map destination and its Uxx-D5 card alongside the D1-D4 destinations and cards. Several depths can share one file; the D5 map must remain legible and directly accessible.

For existing material, inventory actual incoming links and preserve or redirect them according to the application contract. Do not inherit project-specific filenames or aliases from the first version of this framework. For print, provide section names and page references after layout is final.
