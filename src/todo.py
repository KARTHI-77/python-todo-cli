class TodoManager:
    """Manage tasks in the To-Do List application."""

    def __init__(self, tasks=None):
        """Initialize the task manager with existing tasks or an empty list."""
        self.tasks = tasks if tasks is not None else []

    def add_task(self, title):
        """Add a new task and return the created task."""

        title = title.strip()

        # Prevent empty or whitespace-only task titles.
        if not title:
            raise ValueError("Task title cannot be empty.")

        # Generate a unique ID based on the highest existing ID.
        if self.tasks:
            task_id = max(task["id"] for task in self.tasks) + 1
        else:
            task_id = 1

        task = {
            "id": task_id,
            "title": title,
            "completed": False
        }

        self.tasks.append(task)
        return task

    def get_tasks(self):
        """Return all tasks."""
        return self.tasks

    def complete_task(self, task_id):
        """Mark a task as completed."""

        task = self._find_task(task_id)

        if task["completed"]:
            raise ValueError("Task is already completed.")

        task["completed"] = True
        return task

    def remove_task(self, task_id):
        """Remove a task by its ID."""

        task = self._find_task(task_id)
        self.tasks.remove(task)

        return task

    def _find_task(self, task_id):
        """Find a task by ID or raise an error if it does not exist."""

        for task in self.tasks:
            if task["id"] == task_id:
                return task

        raise ValueError(f"Task with ID {task_id} does not exist.")