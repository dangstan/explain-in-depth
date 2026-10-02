#!/usr/bin/env python3
"""Create a fresh five-depth application. Python 3.9+, standard library only."""
import argparse
import json
import re
import shutil
from pathlib import Path

SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def initialize(destination, track, topic):
    if not SLUG.fullmatch(track) or len(track) > 64:
        raise ValueError("TRACK must be a lowercase hyphenated slug, at most 64 characters")
    if not topic.strip() or "\n" in topic or "\r" in topic:
        raise ValueError("Topic must be a nonempty single line")
    destination = Path(destination).absolute()
    skill = Path(__file__).resolve().parents[1]
    try:
        destination.resolve().relative_to(skill)
    except ValueError:
        pass
    else:
        raise ValueError("Application state must live outside the skill repository")
    if destination.exists() or destination.is_symlink():
        raise FileExistsError("Destination already exists; nothing was overwritten")
    source = skill / "assets" / "plan"
    shutil.copytree(source, destination)  # dirs_exist_ok is deliberately false.
    for path in destination.rglob("*.md"):
        body = path.read_text(encoding="utf-8").replace("explain-in-depth", track)
        path.write_text(body, encoding="utf-8")
    state = destination / "CURRENT_STATE.md"
    body = state.read_text(encoding="utf-8")
    body = body.replace("Application subject: unbound", "Application subject: " + topic.strip())
    body = body.replace(
        "Application workspace and plan directory: resolved by G5-01 from the destination and user request",
        "Application plan directory: " + str(destination.resolve())
        + "\n- Source workspace: resolve during G5-01 from the user request"
    )
    body = body.replace(
        "State: reusable framework prepared; no application has begun",
        "State: application scaffold initialized; intake and implementation have not begun"
    )
    state.write_text(body, encoding="utf-8")
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--track", required=True)
    parser.add_argument("--topic", required=True)
    args = parser.parse_args()
    try:
        path = initialize(args.destination, args.track, args.topic)
    except (ValueError, OSError) as error:
        parser.exit(2, str(error) + "\n")
    print(json.dumps({"plan": str(path), "track": args.track, "item": "G5-01",
                      "status": "scaffold_only"}))


if __name__ == "__main__":
    main()
