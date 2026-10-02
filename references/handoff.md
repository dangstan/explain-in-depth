# Session handoff contract

Deliver a fenced code block in chat. Do not save the next-session prompt as a file.

The first line is verbatim "Operate in journal-mode." Immediately below it put TRACK with the literal application slug and ITEM with the exact eligible task ID. Read these values from the application's ROUTES, CURRENT_STATE and ledger; never dispatch template placeholders.

Include one brief role/workspace/plan orientation line. Point to CURRENT_STATE (Current plan and Active runs), PLAN, recent DECISIONS, relevant ARCHITECTURE and MEMORY, in that order. Include "Derive your task from THOSE, not from this prompt."

Do not carry status, numbers, results, implementation recipes or repeated rules in the prompt. Fix missing durable knowledge in the documents. Review and repair retain the candidate's ITEM; the role and exact candidate are authoritative in state.

This is a textual coordination convention. It does not imply that the host implements journal-mode machinery or has registered the TRACK externally. Use the host's actual capabilities without inventing integrations or authority.
