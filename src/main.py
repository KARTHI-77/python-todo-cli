from todo import TodoManager
from storage import load_tasks, save_tasks


def display_menu():
    """Display the application's main menu."""

    print("\n" + "=" * 35)
    print("          PYTODO CLI")
    print("=" * 35)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")
    print("=" * 35)


def display_tasks(manager):
    """Display all tasks in a readable format."""

    tasks = manager.get_tasks()

    if not tasks:
        print("\n📋 No tasks found.")
        return

    print("\n" + "-" * 60)
    print(f"{'ID':<5}{'Status':<12}Task")
    print("-" * 60)

    for task in tasks:
        status = "✓ Done" if task["completed"] else "Pending"
        print(f"{task['id']:<5}{status:<12}{task['title']}")

    print("-" * 60)


def get_task_id():
    """Ask the user for a valid positive task ID."""

    while True:
        value = input("Enter task ID: ").strip()

        try:
            task_id = int(value)

            if task_id <= 0:
                print("❌ Task ID must be a positive number.")
                continue

            return task_id

        except ValueError:
            print("❌ Invalid task ID. Please enter a number.")


def add_task(manager):
    """Handle adding a new task."""

    title = input("Enter task title: ").strip()

    try:
        task = manager.add_task(title)
        save_tasks(manager.get_tasks())

        print(f"✅ Task {task['id']} added successfully.")

    except ValueError as error:
        print(f"❌ {error}")

    except OSError as error:
        print(f"❌ Task was created but could not be saved: {error}")


def complete_task(manager):
    """Handle marking a task as completed."""

    if not manager.get_tasks():
        print("\n📋 No tasks available.")
        return

    display_tasks(manager)
    task_id = get_task_id()

    try:
        task = manager.complete_task(task_id)
        save_tasks(manager.get_tasks())

        print(f"✅ Task {task['id']} marked as completed.")

    except ValueError as error:
        print(f"❌ {error}")

    except OSError as error:
        print(f"❌ Task status changed but could not be saved: {error}")


def remove_task(manager):
    """Handle removing a task."""

    if not manager.get_tasks():
        print("\n📋 No tasks available.")
        return

    display_tasks(manager)
    task_id = get_task_id()

    try:
        task = manager.remove_task(task_id)
        save_tasks(manager.get_tasks())

        print(f"✅ Task {task['id']} removed successfully.")

    except ValueError as error:
        print(f"❌ {error}")

    except OSError as error:
        print(f"❌ Task was removed but changes could not be saved: {error}")


def main():
    """Run the To-Do List CLI application."""

    manager = TodoManager(load_tasks())

    while True:
        display_menu()

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(manager)

        elif choice == "2":
            display_tasks(manager)

        elif choice == "3":
            complete_task(manager)

        elif choice == "4":
            remove_task(manager)

        elif choice == "5":
            try:
                save_tasks(manager.get_tasks())
                print("\n👋 Thank you for using PyTodo CLI!")
            except OSError as error:
                print(f"\n⚠️ Warning: Could not save tasks before exiting: {error}")

            break

        else:
            print("❌ Invalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()