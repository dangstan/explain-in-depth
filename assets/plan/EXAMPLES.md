# Illustrative applications

These examples demonstrate adaptation of the framework. They are planning illustrations, not researched explanations or factual source evidence. Each real application must establish its own sources and claims.

| Application | D1 | D2 | D3 | D4 | D5 |
| --- | --- | --- | --- | --- | --- |
| Software repository | User need and visible result | Capabilities, dependencies and tradeoffs | One request through components and handoffs | Interfaces, state, failure and recovery | Detailed component, interface and dependency map linked to code, tests and contracts |
| Scientific topic | Familiar phenomenon and question | Main ideas, significance and unresolved questions | Worked model or observation sequence | Assumptions, methods and boundary cases | Detailed concept and mechanism map linked to papers, data, derivations and methods |
| Historical topic | A bounded episode and its human context | Themes, actors and competing interpretations | Chronology and relationships with evidence | Source criticism and historiographical argument | Detailed actor, event and interpretation map linked to primary sources |
| Organizational procedure | Situation and intended outcome | Responsibilities, constraints and choices | Ordinary case and exception handoff | Decision rules and ambiguous cases | Detailed decision, role and exception map linked to policy, forms and records |

For a mathematical topic, D3 can work a concrete example while D4 explains a proof or assumption and D5 visualizes definition, theorem and proof dependencies with references to exact derivations. Do not invent organizational roles to make it resemble software.

## Minimal document application

A single subject can use one document with five named sections, annotated static figures, a mandatory detailed D5 map and supporting references. The generated chain is U01-D5 -> U01-D1 -> U01-D2 -> U01-D3 -> U01-D4 -> U01-INTEGRATE. There are no companion tasks unless requested.

G5-PILOT follows U01-INTEGRATE. G5-QA checks the selected complete deliverable and release conditions; it does not repeat pilot checks without reason. G5-CLOSE then reports actual evidence and stops.

## Multiple subject website

For a repository with two bounded subsystems, U01 is the pilot. G5-PILOT gates U02. Each subject has its own evidence and depth cards, while G5-03 owns shared navigation and styles. G5-QA checks cross-subject links and final integration.

The subject count is a scope decision, not a requirement to document the whole repository. Existing source maps are preserved only when the intake classifies them that way.

## Sources missing or disputed

If a topic lacks a single authoritative artifact, create a detailed D5 map that distinguishes relationships, provenance and disagreement, supported by a source guide. If the evidence cannot support the planned central claim, narrow the explanation or block its dependent card. Do not fill the gap with a plausible invented source.

## Audience specific companion

An executive briefing may emphasize D1 and D2 as a companion to the complete five-depth deliverable. Its parent build still includes D3, D4 and the detailed D5 map. The chain remains U01-D5 -> U01-D1 -> U01-D2 -> U01-D3 -> U01-D4 -> U01-INTEGRATE, followed by the requested companion card. Focusing a presentation on one audience does not waive any depth from the complete build.
