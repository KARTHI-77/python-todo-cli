# PyTodo CLI

A simple and modular command-line To-Do List Manager built with Python.

This project was developed as part of the **YuvaIntern Junior Python Developer Internship – Week 1 Task**.

The application allows users to create, view, complete, and remove tasks through an interactive command-line interface. Task data is persisted locally using a JSON file so that tasks remain available after restarting the application.

---

## Features

- Add new tasks
- View all tasks
- Mark tasks as completed
- Remove tasks
- Automatic task ID generation
- Persistent task storage using JSON
- Input validation
- Error handling for invalid user input
- Handling of nonexistent task IDs
- Handling of empty task lists
- Handling of corrupted JSON data
- Modular project structure
- Automated unit tests using Python's built-in `unittest` framework
- No external Python dependencies required

---

## Project Structure

```text
python-todo-cli/
│
├── data/
│   └── tasks.json
│
├── src/
│   ├── main.py
│   ├── storage.py
│   └── todo.py
│
├── tests/
│   └── test_todo.py
│
├── .gitignore
└── README.md
```

### File Responsibilities

#### `src/main.py`

Handles the command-line interface and user interaction.

Responsibilities:

- Displaying the application menu
- Reading user input
- Validating task IDs
- Calling task management operations
- Displaying tasks
- Displaying success and error messages
- Loading and saving task data

#### `src/todo.py`

Contains the `TodoManager` class and the application's core task management logic.

Responsibilities:

- Adding tasks
- Generating task IDs
- Retrieving tasks
- Marking tasks as completed
- Removing tasks
- Finding tasks by ID
- Validating task existence

#### `src/storage.py`

Handles persistent task storage using JSON.

Responsibilities:

- Loading tasks from the JSON file
- Saving tasks to the JSON file
- Handling missing files
- Handling invalid JSON
- Handling invalid data formats
- Creating the data directory when required

#### `data/tasks.json`

Stores task data locally in JSON format.

#### `tests/test_todo.py`

Contains automated unit tests for the task management and storage functionality using Python's built-in `unittest` framework.

---

## Architecture

The project follows a simple layered structure that separates the user interface, business logic, and data storage.

```text
┌──────────────────────┐
│        User          │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      main.py         │
│   CLI / User Input   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       todo.py        │
│   TodoManager Logic  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      storage.py      │
│   Load / Save JSON   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    tasks.json        │
│   Persistent Data    │
└──────────────────────┘
```

### Architecture Responsibilities

**User**

Interacts with the application through the terminal.

**`main.py`**

Acts as the presentation layer. It handles user input, menu options, and user-facing messages.

**`todo.py`**

Acts as the business logic layer. It manages task creation, completion, retrieval, and removal.

**`storage.py`**

Acts as the persistence layer. It manages reading and writing task data.

**`tasks.json`**

Provides local persistent storage for the application's task data.

This separation keeps different responsibilities independent and makes the application easier to understand, test, maintain, and extend.

---

## Application Flows

### Application Startup Flow

```text
Start Application
       ↓
Load tasks from tasks.json
       ↓
Create TodoManager
       ↓
Display Main Menu
       ↓
Wait for User Input
       ↓
Perform Selected Operation
       ↓
Return to Main Menu
       ↓
Continue Until Exit
```

### Add Task Flow

```text
User selects "Add Task"
        ↓
Enter task title
        ↓
Validate task title
        ↓
Generate task ID
        ↓
Create task
        ↓
Add task to task list
        ↓
Save tasks to JSON
        ↓
Display success message
```

### View Tasks Flow

```text
User selects "View Tasks"
        ↓
Retrieve tasks
        ↓
Check whether tasks exist
        ↓
Display task list
```

### Complete Task Flow

```text
User selects "Mark Task as Completed"
        ↓
Check whether tasks exist
        ↓
Display available tasks
        ↓
Enter task ID
        ↓
Validate task ID
        ↓
Find task
        ↓
Check completion status
        ↓
Mark task as completed
        ↓
Save tasks to JSON
        ↓
Display success message
```

### Remove Task Flow

```text
User selects "Remove Task"
        ↓
Check whether tasks exist
        ↓
Display available tasks
        ↓
Enter task ID
        ↓
Validate task ID
        ↓
Find task
        ↓
Remove task
        ↓
Save tasks to JSON
        ↓
Display success message
```

### Exit Flow

```text
User selects "Exit"
        ↓
Save current task data
        ↓
Display exit message
        ↓
Terminate application
```

---

## Data Model

Each task is represented using three fields:

```json
{
    "id": 1,
    "title": "Learn Python",
    "completed": false
}
```

### Task Fields

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Unique identifier for the task |
| `title` | String | Description of the task |
| `completed` | Boolean | Indicates whether the task is completed |

Multiple tasks are stored as a JSON list:

```json
[
    {
        "id": 1,
        "title": "Learn Python",
        "completed": false
    },
    {
        "id": 2,
        "title": "Build a project",
        "completed": true
    }
]
```

---

## Requirements

The project requires:

- Python 3.x
- Command-line terminal

The application uses only Python's standard library.

No external Python packages or dependencies are required.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KARTHI-77/python-todo-cli.git
```

### 2. Navigate to the Project Directory

```bash
cd python-todo-cli
```

### 3. Verify Python Installation

Check that Python 3 is installed:

```bash
python --version
```

The project does not require a virtual environment or package installation for normal use.

---

## Running the Application

From the project root, navigate to the `src` directory:

```bash
cd src
```

Run the application:

```bash
python main.py
```

The application will display the following menu:

```text
===================================
          PYTODO CLI
===================================
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Remove Task
5. Exit
===================================
Choose an option (1-5):
```

---

## Usage

### Add a Task

Select:

```text
1. Add Task
```

Enter the task title:

```text
Enter task title: Learn Python
```

The application automatically creates the task and assigns a task ID.

Example:

```text
✅ Task 1 added successfully.
```

---

### View Tasks

Select:

```text
2. View Tasks
```

Example output:

```text
------------------------------------------------------------
ID   Status      Task
------------------------------------------------------------
1    Pending     Learn Python
2    ✓ Done      Build a project
------------------------------------------------------------
```

---

### Mark a Task as Completed

Select:

```text
3. Mark Task as Completed
```

The application displays the available tasks and asks for the task ID.

```text
Enter task ID: 1
```

Example result:

```text
✅ Task 1 marked as completed.
```

---

### Remove a Task

Select:

```text
4. Remove Task
```

The application displays the available tasks and asks for the task ID.

```text
Enter task ID: 2
```

Example result:

```text
✅ Task 2 removed successfully.
```

---

### Exit the Application

Select:

```text
5. Exit
```

The application saves the current task data before exiting.

Example:

```text
👋 Thank you for using PyTodo CLI!
```

---

## Error Handling

The application includes input validation and error handling for common user and file-related errors.

### Empty Task Titles

Empty task titles are rejected.

```text
Enter task title:
❌ Task title cannot be empty.
```

Whitespace-only titles are also rejected.

```text
Enter task title:     
❌ Task title cannot be empty.
```

### Invalid Task IDs

Task IDs must be positive integers.

For non-numeric input:

```text
Enter task ID: abc
❌ Invalid task ID. Please enter a number.
```

For zero or negative values:

```text
Enter task ID: -1
❌ Task ID must be a positive number.
```

### Nonexistent Task IDs

If the entered task ID does not exist:

```text
Enter task ID: 999
❌ Task with ID 999 does not exist.
```

### Already Completed Tasks

The application prevents an already completed task from being completed again:

```text
❌ Task is already completed.
```

### Empty Task List

If there are no tasks available, the application displays an appropriate message instead of attempting an invalid operation.

### Invalid JSON

If the task storage file contains invalid JSON, the application handles the error and starts with an empty task list while displaying a warning.

### Invalid Data Format

If the JSON file contains data in an unexpected format, the application handles the error and starts with an empty task list.

### File System Errors

File system errors that occur while reading or saving task data are handled and reported to the user.

---

## Data Persistence

Task data is stored locally in:

```text
data/tasks.json
```

When a task is added, completed, or removed, the updated task list is saved to the JSON file.

When the application starts, the existing task data is loaded from the JSON file.

This allows tasks to remain available between application sessions without requiring a database or external service.

---

## Testing

The project includes automated unit tests using Python's built-in `unittest` framework.

### TodoManager Tests

The following functionality is tested:

- Adding a task
- Adding multiple tasks
- Automatic task ID generation
- Removing whitespace from task titles
- Rejecting empty task titles
- Rejecting whitespace-only task titles
- Retrieving tasks
- Completing tasks
- Preventing duplicate task completion
- Handling nonexistent task IDs
- Removing tasks
- Handling nonexistent tasks during removal

### Storage Tests

The storage functionality is tested for:

- Saving and loading tasks
- Loading a missing JSON file
- Handling invalid JSON
- Handling invalid data formats

### Running the Tests

Run the tests from the project root:

```bash
python -m unittest discover -s tests -v
```

Expected result:

```text
Ran 15 tests

OK
```

---

## Manual Testing

The application was manually tested against common user and data-handling scenarios.

| Test Scenario | Expected Result |
|---|---|
| Add a valid task | Task is created successfully |
| Add an empty task | Error message is displayed |
| Add whitespace-only task | Error message is displayed |
| View tasks | All stored tasks are displayed |
| Complete a valid task | Task status changes to completed |
| Complete an already completed task | Error message is displayed |
| Complete nonexistent task | Error message is displayed |
| Remove a valid task | Task is removed successfully |
| Remove nonexistent task | Error message is displayed |
| Enter invalid menu option | Error message is displayed |
| Enter non-numeric task ID | Error message is displayed |
| Enter zero task ID | Error message is displayed |
| Enter negative task ID | Error message is displayed |
| View an empty task list | Appropriate message is displayed |
| Restart the application | Previously saved tasks are loaded |
| Use corrupted JSON data | Warning is displayed and application starts safely |

---

## Design Decisions

### Modular Architecture

The application is divided into separate modules for the command-line interface, business logic, and storage.

This keeps each component focused on a specific responsibility and makes the project easier to maintain and test.

### `TodoManager` Class

Task-related operations are grouped inside the `TodoManager` class.

This provides a clear interface for managing tasks and keeps the core business logic separate from the command-line interface.

### JSON Storage

JSON was selected as the storage format because the application is small and does not require the complexity of a database.

The JSON file is also human-readable and easy to inspect during development.

### Built-in `unittest`

Python's built-in `unittest` framework was selected so that the project does not require additional testing dependencies.

### Automatic Task IDs

Task IDs are generated automatically based on the highest existing task ID.

This prevents users from manually assigning task IDs and helps maintain unique identifiers.

### Input Validation

User input is validated before performing task operations.

This prevents invalid task IDs and empty task titles from being processed.

### Exception Handling

Exceptions are handled at appropriate points so that common errors are reported clearly to the user rather than causing unexpected application termination.

---

## Future Improvements

The current application provides the required core To-Do List functionality. Possible future improvements include:

- Edit existing task titles
- Add task priorities
- Add task due dates
- Add task categories
- Search and filter tasks
- Add an undo feature for completed or removed tasks
- Improve terminal interface formatting
- Add more comprehensive automated tests
- Replace JSON storage with a database for larger applications
- Add application logging
- Add configuration support

---

## Learning Outcomes

Through this project, the following Python development concepts were practiced:

- Python classes and object-oriented programming
- Functions and modular programming
- Lists and dictionaries
- JSON file handling
- File-system operations using `pathlib`
- Exception handling
- Input validation
- Command-line application design
- Unit testing using `unittest`
- Separation of responsibilities
- Basic software architecture
- Git and GitHub-based project development
- Writing technical documentation

---

## Internship Context

This project was developed as part of the **YuvaIntern Junior Python Developer Internship – Week 1 Task**.

The Week 1 task focused on designing and implementing a Python command-line To-Do List Manager with core task management functionality.

The project demonstrates the implementation of:

- Task creation
- Task viewing
- Task completion
- Task removal
- Input validation
- Error handling
- Local data persistence
- Modular Python development
- Automated testing
- Technical documentation

The project was developed with an emphasis on clean structure, maintainability, reliability, and practical Python development practices.

---
