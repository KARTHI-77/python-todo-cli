import json
import tempfile
import unittest
from pathlib import Path

from src.todo import TodoManager
from src.storage import load_tasks, save_tasks


class TestTodoManager(unittest.TestCase):
    """Test cases for the TodoManager class."""

    def setUp(self):
        """Create a fresh TodoManager before each test."""
        self.manager = TodoManager()

    def test_add_task(self):
        """A valid task should be added successfully."""

        task = self.manager.add_task("Learn Python")

        self.assertEqual(task["id"], 1)
        self.assertEqual(task["title"], "Learn Python")
        self.assertFalse(task["completed"])

        self.assertEqual(len(self.manager.get_tasks()), 1)

    def test_add_multiple_tasks_generates_unique_ids(self):
        """Multiple tasks should receive unique sequential IDs."""

        first_task = self.manager.add_task("Learn Python")
        second_task = self.manager.add_task("Build a project")

        self.assertEqual(first_task["id"], 1)
        self.assertEqual(second_task["id"], 2)

    def test_add_task_strips_whitespace(self):
        """Leading and trailing whitespace should be removed."""

        task = self.manager.add_task("  Learn Python  ")

        self.assertEqual(task["title"], "Learn Python")

    def test_add_empty_task_raises_error(self):
        """An empty task title should raise ValueError."""

        with self.assertRaises(ValueError):
            self.manager.add_task("")

    def test_add_whitespace_task_raises_error(self):
        """A whitespace-only task title should raise ValueError."""

        with self.assertRaises(ValueError):
            self.manager.add_task("     ")

    def test_get_tasks(self):
        """get_tasks should return all existing tasks."""

        self.manager.add_task("Task One")
        self.manager.add_task("Task Two")

        tasks = self.manager.get_tasks()

        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["title"], "Task One")
        self.assertEqual(tasks[1]["title"], "Task Two")

    def test_complete_task(self):
        """A pending task should be marked as completed."""

        task = self.manager.add_task("Complete assignment")

        completed_task = self.manager.complete_task(task["id"])

        self.assertTrue(completed_task["completed"])
        self.assertTrue(self.manager.get_tasks()[0]["completed"])

    def test_complete_already_completed_task_raises_error(self):
        """Completing an already completed task should raise ValueError."""

        task = self.manager.add_task("Complete assignment")

        self.manager.complete_task(task["id"])

        with self.assertRaises(ValueError):
            self.manager.complete_task(task["id"])

    def test_complete_nonexistent_task_raises_error(self):
        """Completing a nonexistent task should raise ValueError."""

        with self.assertRaises(ValueError):
            self.manager.complete_task(999)

    def test_remove_task(self):
        """A task should be removed successfully."""

        task = self.manager.add_task("Remove me")

        removed_task = self.manager.remove_task(task["id"])

        self.assertEqual(removed_task["title"], "Remove me")
        self.assertEqual(len(self.manager.get_tasks()), 0)

    def test_remove_nonexistent_task_raises_error(self):
        """Removing a nonexistent task should raise ValueError."""

        with self.assertRaises(ValueError):
            self.manager.remove_task(999)

class TestStorage(unittest.TestCase):
    """Test cases for task data storage."""

    def test_save_and_load_tasks(self):
        """Tasks should be saved and loaded correctly."""

        tasks = [
            {
                "id": 1,
                "title": "Learn Python",
                "completed": False
            },
            {
                "id": 2,
                "title": "Build a project",
                "completed": True
            }
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "tasks.json"

            save_tasks(tasks, file_path)
            loaded_tasks = load_tasks(file_path)

            self.assertEqual(loaded_tasks, tasks)

    def test_load_missing_file(self):
        """Loading a nonexistent file should return an empty list."""

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "missing.json"

            tasks = load_tasks(file_path)

            self.assertEqual(tasks, [])

    def test_load_invalid_json(self):
        """Invalid JSON should return an empty list."""

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "invalid.json"

            file_path.write_text(
                "this is not valid JSON",
                encoding="utf-8"
            )

            tasks = load_tasks(file_path)

            self.assertEqual(tasks, [])

    def test_load_invalid_data_format(self):
        """JSON containing a non-list value should return an empty list."""

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "invalid_format.json"

            file_path.write_text(
                json.dumps({"task": "Learn Python"}),
                encoding="utf-8"
            )

            tasks = load_tasks(file_path)

            self.assertEqual(tasks, [])

if __name__ == "__main__":
    unittest.main()