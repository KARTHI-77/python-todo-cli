import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "tasks.json"


def load_tasks(file_path=DATA_FILE):

    file_path = Path(file_path)

    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Task data must be a list.")

        return data

    except json.JSONDecodeError:
        print(
            "⚠️ Warning: tasks.json contains invalid JSON. "
            "Starting with an empty task list."
        )
        return []

    except OSError as error:
        print(f"⚠️ Warning: Unable to read task data: {error}")
        return []

    except ValueError:
        print(
            "⚠️ Warning: Invalid task data format. "
            "Starting with an empty task list."
        )
        return []


def save_tasks(tasks, file_path=DATA_FILE):

    file_path = Path(file_path)

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with file_path.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)

    except OSError as error:
        raise OSError(f"Unable to save tasks: {error}") from error