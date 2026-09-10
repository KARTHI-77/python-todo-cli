import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""

    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Task data must be a list.")

        return data

    except json.JSONDecodeError:
        print("⚠️ Warning: tasks.json contains invalid JSON. Starting with an empty task list.")
        return []

    except OSError as error:
        print(f"⚠️ Warning: Unable to read task data: {error}")
        return []

    except ValueError:
        print("⚠️ Warning: Invalid task data format. Starting with an empty task list.")
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""

    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)

    except OSError as error:
        raise OSError(f"Unable to save tasks: {error}") from error