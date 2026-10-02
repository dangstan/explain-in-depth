import importlib.util
import copy
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


validate = module("validate_plan").validate
initialize = module("init_plan").initialize


class PlanTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "application"
        initialize(self.root, "test-topic", "A bounded topic")
        (self.root / "run").mkdir()
        self.plan = {"schema_version": 1, "track": "test-topic", "tasks": [],
                     "subjects": [], "terminal_item": "CLOSE"}
        previous = None
        depths = {}
        for depth in ["D5", "D1", "D2", "D3", "D4"]:
            item = "U01-" + depth
            self.plan["tasks"].append({"id": item, "requires": [previous] if previous else []})
            depths[depth] = {"items": [item], "destination": "outputs/" + depth + ".md",
                             "kind": "detailed-map" if depth == "D5" else "explanation",
                             "outcome": "Trace a meaningful relationship", "criteria": ["Explain a changed case"]}
            previous = item
        self.plan["tasks"] += [{"id": "INTEGRATE", "requires": [previous]},
                               {"id": "CLOSE", "requires": ["INTEGRATE"]}]
        self.plan["subjects"] = [{"id": "U01", "title": "A topic", "depths": depths,
                                  "integration_item": "INTEGRATE"}]
        for task in self.plan["tasks"]:
            (self.root / "tasks" / (task["id"] + ".md")).write_text(
                "TRACK: test-topic\nITEM: " + task["id"] + "\n", encoding="utf-8")
        self.write()

    def tearDown(self):
        self.temp.cleanup()

    def write(self):
        (self.root / "run" / "PLAN.json").write_text(json.dumps(self.plan), encoding="utf-8")

    def test_valid_blueprint_before_outputs(self):
        self.assertEqual(validate(self.root), [])

    def test_each_depth_is_required(self):
        for depth in ["D1", "D2", "D3", "D4", "D5"]:
            original = self.plan["subjects"][0]["depths"].pop(depth)
            self.write()
            self.assertTrue(any("mandatory" in e for e in validate(self.root)))
            self.plan["subjects"][0]["depths"][depth] = original

    def test_d5_source_index_is_not_map(self):
        self.plan["subjects"][0]["depths"]["D5"]["kind"] = "source-index"
        self.write()
        self.assertTrue(any("detailed-map" in e for e in validate(self.root)))

    def test_cycle_and_unknown_dependency(self):
        self.plan["tasks"][0]["requires"] = ["CLOSE", "MISSING"]
        self.write()
        errors = validate(self.root)
        self.assertTrue(any("cycle" in e for e in errors))
        self.assertTrue(any("unknown dependency" in e for e in errors))

    def test_integration_cannot_skip_depths(self):
        self.plan["tasks"][-2]["requires"] = ["U01-D5"]
        self.write()
        self.assertTrue(any("bypasses" in e for e in validate(self.root)))

    def test_destination_cannot_escape(self):
        self.plan["subjects"][0]["depths"]["D5"]["destination"] = "../outside.md"
        self.write()
        self.assertTrue(any("traversal" in e for e in validate(self.root)))

    def test_track_and_card_identity(self):
        (self.root / "tasks" / "U01-D1.md").write_text("TRACK: other\nITEM: U01-D2\n")
        errors = validate(self.root)
        self.assertTrue(any("TRACK mismatch" in e for e in errors))
        self.assertTrue(any("ITEM mismatch" in e for e in errors))

    def test_existing_destination_is_not_overwritten(self):
        sentinel = self.root / "sentinel.txt"
        sentinel.write_text("keep")
        with self.assertRaises(FileExistsError):
            initialize(self.root, "another-topic", "Another topic")
        self.assertEqual(sentinel.read_text(), "keep")

    def test_no_application_inside_skill(self):
        with self.assertRaises(ValueError):
            initialize(ROOT / "must-not-create", "test-topic", "Topic")

    def test_premature_completion_fails(self):
        self.assertTrue(validate(self.root, complete=True))


    def test_subject_cannot_reuse_another_subjects_depth_tasks(self):
        second = copy.deepcopy(self.plan["subjects"][0])
        second["id"] = "U02"
        second["title"] = "A different subject"
        self.plan["subjects"].append(second)
        self.write()
        self.assertTrue(any("already assigned" in e for e in validate(self.root)))

    def test_template_metadata_matches_card_parser(self):
        template = (ROOT / "assets" / "plan" / "templates" / "TASK_CARD.md").read_text(encoding="utf-8")
        card = template.replace("exact literal slug from ROUTES.md", "test-topic")
        card = card.replace("stable unique ID listed in TASKS.md", "U01-D1")
        (self.root / "tasks" / "U01-D1.md").write_text(card, encoding="utf-8")
        self.assertEqual(validate(self.root), [])

    def test_completion_and_stale_review(self):
        (self.root / "outputs").mkdir()
        (self.root / "evidence").mkdir()
        for depth in self.plan["subjects"][0]["depths"]:
            (self.root / "outputs" / (depth + ".md")).write_text("Synthetic test artifact")
        records = []
        for task in self.plan["tasks"]:
            review = "evidence/" + task["id"] + ".md"
            (self.root / review).write_text("Synthetic structural test, not a real review")
            records.append({"id": task["id"], "status": "accepted", "verdict": "ACCEPT",
                            "candidate": "fixture-identity", "review_candidate": "fixture-identity",
                            "review": review})
        status = {"track": "test-topic", "tasks": records}
        path = self.root / "run" / "STATUS.json"
        path.write_text(json.dumps(status), encoding="utf-8")
        self.assertEqual(validate(self.root, complete=True), [])
        records[0]["review_candidate"] = "old-candidate"
        path.write_text(json.dumps(status), encoding="utf-8")
        self.assertTrue(any("stale" in e for e in validate(self.root, complete=True)))


if __name__ == "__main__":
    unittest.main()
