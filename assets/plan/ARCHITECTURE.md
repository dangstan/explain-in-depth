# General plan architecture

## Three layers

The framework layer contains learning contracts, execution rules and reusable card templates. The application layer binds sources, audiences, medium, subject inventory and output destinations. The artifact layer contains the explanations, evidence access and any requested companions.

This separation allows a topic without code to use the same planning method as a repository without inheriting code-specific tools or claims.

## Application data flow

User request and bounded sources -> intake and claim inventory -> subject briefs and task graph -> medium specimen -> pilot artifacts -> independent pilot review -> remaining subjects -> integrated review -> closure.

Arrows describe work dependencies, not a claim that the subject itself is a pipeline. Evidence and source links remain attached to the relevant claims throughout.

## State and ownership

TASKS.md holds stable IDs and dependencies. run/STATUS.json holds actual execution status, ownership, attempts and candidate pointers. CURRENT_STATE.md routes the next session and summarizes only actionable state. DECISIONS.md holds material choices. MEMORY.md points to persistent pitfalls.

One writer owns production files at a time. Read-only analysis can run separately when allowed by the host. Coordination metadata does not provide a reliable distributed lock.

## Output structures

A website may use routes and interactive diagrams. A document may use sections, annotated figures and references. Slides may use coherent scenes and speaker notes. A subject's five purposes can occupy one artifact or several; run/OUTPUTS.md makes the destinations exact.

Source originals and generated explanations have separate identities. Each subject has a mandatory detailed D5 map connecting the in-scope structure to precise supporting material. A source index may accompany the map but does not replace it. The map can be static or interactive according to the medium. A frozen candidate is a scoped commit, file hash manifest or versioned document/export with an exact identity.

## Adaptation boundary

Apply destination instructions and user authorization. Do not import the original project's filenames, baseline mismatches, deferred checks, runtime constraints or completed task state. Existing legal, operational or domain review requirements belong in the application's acceptance contract when applicable.

## Mandatory depth coverage

Every application subject includes all five distinct depths. The output manifest and task graph map each depth to a destination, candidate and acceptance evidence. Files and media may be shared; learning purposes may not be collapsed or omitted. D5 remains a detailed visualization or map. No integration or closure can pass with missing or unaccepted depth coverage.
