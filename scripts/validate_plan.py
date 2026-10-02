#!/usr/bin/env python3
"""Validate plan structure, not teaching quality or review independence."""
import argparse
import json
import re
from pathlib import Path, PurePosixPath

DEPTHS = {"D1", "D2", "D3", "D4", "D5"}
ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]*")
TRACK = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def text(value):
    return isinstance(value, str) and bool(value.strip())


def local_path(root, value):
    if not text(value):
        raise ValueError("missing relative path")
    name = value.split("#", 1)[0]
    if "\\" in name or ":" in name or not name or ".." in PurePosixPath(name).parts:
        raise ValueError("path must be relative, using forward slashes, without traversal")
    path = PurePosixPath(name)
    if path.is_absolute():
        raise ValueError("absolute path is not allowed")
    resolved = root.joinpath(*path.parts).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError:
        raise ValueError("path escapes application directory")
    return resolved


def read_json(path):
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def validate(root, complete=False):
    root = Path(root)
    errors = []
    try:
        plan = read_json(root / "run" / "PLAN.json")
    except (OSError, ValueError) as error:
        return ["Cannot read run/PLAN.json: " + str(error)]
    if not isinstance(plan, dict):
        return ["PLAN must be an object"]
    track = plan.get("track")
    if not text(track) or not TRACK.fullmatch(track) or len(track) > 64:
        errors.append("Invalid TRACK")
    if plan.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    for name, prefix in [("CURRENT_STATE.md", "- TRACK: "), ("ROUTES.md", "Default TRACK: ")]:
        try:
            lines = (root / name).read_text(encoding="utf-8").splitlines()
            if prefix + str(track) not in lines:
                errors.append(name + " TRACK does not match PLAN")
        except OSError:
            errors.append("Missing " + name)
    tasks = plan.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        return errors + ["tasks must be a nonempty array"]
    graph = {}
    for task in tasks:
        if not isinstance(task, dict):
            errors.append("Each task must be an object")
            continue
        item = task.get("id")
        if not text(item) or not ID.fullmatch(item):
            errors.append("Invalid task ID")
            continue
        if item in graph:
            errors.append("Duplicate task: " + item)
            continue
        deps = task.get("requires")
        if not isinstance(deps, list) or any(not text(x) for x in deps):
            errors.append(item + ": requires must be an array of IDs")
            deps = []
        if len(deps) != len(set(deps)):
            errors.append(item + ": duplicate dependencies")
        graph[item] = deps
        try:
            card = local_path(root, "tasks/" + item + ".md").read_text(encoding="utf-8")
            if card.splitlines().count("TRACK: " + str(track)) != 1:
                errors.append(item + ": card TRACK mismatch")
            if card.splitlines().count("ITEM: " + item) != 1:
                errors.append(item + ": card ITEM mismatch")
        except (OSError, ValueError):
            errors.append(item + ": missing or unsafe card")
    for item, deps in graph.items():
        for dep in deps:
            if dep not in graph:
                errors.append(item + ": unknown dependency " + dep)
    visiting, visited = set(), set()

    def visit(item):
        if item in visiting:
            raise ValueError("Dependency cycle at " + item)
        if item in visited or item not in graph:
            return
        visiting.add(item)
        for dep in graph[item]:
            visit(dep)
        visiting.remove(item)
        visited.add(item)
    try:
        for item in graph:
            visit(item)
    except (ValueError, RecursionError) as error:
        errors.append(str(error) or "Graph too deep")

    def ancestors(item):
        seen, pending = set(), list(graph.get(item, []))
        while pending:
            value = pending.pop()
            if value not in seen:
                seen.add(value)
                pending.extend(graph.get(value, []))
        return seen

    terminal = plan.get("terminal_item")
    if not isinstance(terminal, str) or terminal not in graph:
        errors.append("terminal_item must name an existing task")
    elif set(graph) - {terminal} - ancestors(terminal):
        errors.append("Terminal task does not depend on all required work")
    subjects = plan.get("subjects")
    if not isinstance(subjects, list) or not subjects:
        return errors + ["subjects must be a nonempty array"]
    subject_ids = set()
    depth_owners = {}
    for subject in subjects:
        if not isinstance(subject, dict):
            errors.append("Each subject must be an object")
            continue
        sid = subject.get("id")
        if not text(sid) or not ID.fullmatch(sid) or sid in subject_ids:
            errors.append("Invalid or duplicate subject ID")
            continue
        subject_ids.add(sid)
        if not text(subject.get("title")):
            errors.append(sid + ": missing title")
        depths = subject.get("depths")
        if not isinstance(depths, dict) or set(depths) != DEPTHS:
            errors.append(sid + ": exactly D1-D5 are mandatory")
            continue
        integration = subject.get("integration_item")
        if not isinstance(integration, str) or integration not in graph:
            errors.append(sid + ": missing integration task")
            integration = ""
        covered_items = set()
        for depth in sorted(DEPTHS):
            spec = depths[depth]
            label = sid + "/" + depth
            if not isinstance(spec, dict):
                errors.append(label + ": depth must be an object")
                continue
            items = spec.get("items")
            if not isinstance(items, list) or not items or any(not text(x) for x in items):
                errors.append(label + ": missing task IDs")
                items = []
            for item in items:
                if item not in graph:
                    errors.append(label + ": unknown task " + item)
                if item in covered_items:
                    errors.append(label + ": depth task reused across distinct depths")
                covered_items.add(item)
                if item in depth_owners and depth_owners[item] != label:
                    errors.append(label + ": task already assigned to " + depth_owners[item])
                depth_owners[item] = label
                if item not in ancestors(integration):
                    errors.append(label + ": integration bypasses " + item)
            kind = "detailed-map" if depth == "D5" else "explanation"
            if spec.get("kind") != kind:
                errors.append(label + ": kind must be " + kind)
            criteria = spec.get("criteria")
            if not text(spec.get("outcome")) or not isinstance(criteria, list) or not criteria or any(not text(x) for x in criteria):
                errors.append(label + ": outcome and criteria are required")
            try:
                path = local_path(root, spec.get("destination"))
                if complete and not path.is_file():
                    errors.append(label + ": destination does not exist")
            except ValueError as error:
                errors.append(label + ": " + str(error))
    if complete:
        try:
            status = read_json(root / "run" / "STATUS.json")
            if not isinstance(status, dict) or status.get("track") != track:
                raise ValueError("STATUS track mismatch")
            rows = status.get("tasks")
            if not isinstance(rows, list):
                raise ValueError("STATUS tasks must be an array")
            records = {}
            for row in rows:
                if not isinstance(row, dict) or not text(row.get("id")):
                    raise ValueError("Invalid STATUS record")
                if row["id"] in records:
                    errors.append("Duplicate STATUS record: " + row["id"])
                records[row["id"]] = row
            if set(records) != set(graph):
                errors.append("STATUS must cover exactly the planned tasks")
            for item in graph:
                row = records.get(item, {})
                if row.get("status") != "accepted" or row.get("verdict") != "ACCEPT":
                    errors.append(item + ": no accepted review")
                candidate = row.get("candidate")
                if not text(candidate) or row.get("review_candidate") != candidate:
                    errors.append(item + ": missing or stale candidate identity")
                try:
                    if not local_path(root, row.get("review")).is_file():
                        errors.append(item + ": review report missing")
                except ValueError as error:
                    errors.append(item + ": " + str(error))
        except (OSError, ValueError) as error:
            errors.append("Cannot validate completion: " + str(error))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("application", type=Path)
    parser.add_argument("--complete", action="store_true")
    args = parser.parse_args()
    errors = validate(args.application, args.complete)
    if errors:
        for error in errors:
            print("ERROR: " + error)
        raise SystemExit(1)
    print("Structural checks passed. Source truth, visuals and review independence require inspection.")


if __name__ == "__main__":
    main()
