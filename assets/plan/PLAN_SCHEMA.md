# Machine readable application plan

G5-02 writes run/PLAN.json alongside the human-readable TASKS and output manifest. The JSON is the machine-checkable graph and coverage contract; TASKS and cards explain the work. Keep both synchronized. Runtime ownership and attempts remain in run/STATUS.json.

## Required fields

- schema_version: 1.
- track: the literal lowercase slug used throughout the application.
- tasks: a nonempty array of objects with id and requires (array of exact task IDs). Each has a tasks/<id>.md card containing literal TRACK and ITEM lines.
- subjects: a nonempty array with unique id, title and depths.
- terminal_item: the final task ID.

Every subject's depths object contains exactly D1, D2, D3, D4 and D5. Each depth has:
- items: nonempty array of task IDs that deliver this depth, including split cards if needed.
- destination: application-relative artifact path, optionally followed by an anchor.
- outcome: a concrete learning outcome.
- criteria: nonempty array of acceptance statements.
- kind: explanation for D1-D4; detailed-map for D5.

Add integration_item to each subject. It must depend transitively on all that subject's depth items. The terminal_item must depend transitively on every other task so closure cannot bypass required work. Independent task branches are supported if all required integration edges are present.

Paths must remain inside the application folder, without absolute paths, traversal or symlink escapes. Existing external protected maps may be exposed through a local guide/wrapper path; the reviewer still verifies the actual map and evidence. Do not copy or edit a protected original to satisfy a file-existence check.

## Structural validation

The validator checks unique IDs, known dependencies, acyclic graph, card metadata, all five depth mappings, exact D5 kind, nonempty outcomes/criteria, integration ancestry and terminal coverage. CURRENT_STATE must contain the matching TRACK and ROUTES must declare Default TRACK.

Destinations do not need to exist before production. The validator does not resolve anchors, inspect visuals or certify sources; reviewers do those checks.

## Completion validation

With --complete, destinations must exist and run/STATUS.json must contain:
- track matching PLAN.
- tasks: an array with exactly one record for every planned task.
- Each record: id, status accepted, candidate (nonempty exact identity), review (relative existing report path), review_candidate matching candidate, and verdict ACCEPT.

Review-only task evidence may be its own independent review report; this does not require reviewer-of-reviewer chains. For build tasks the review must be independent. The script can verify identities and files, but cannot prove the reviewer actually inspected the artifact or was independent.

An accepted record whose prerequisite is missing, unaccepted or for a stale candidate is not a legitimate completion. Preserve earlier attempts and resolve candidate changes through the review workflow.
