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
│── src/
│   ├── main.py
│   ├── storage.py
│   └── todo.py
├── tests/
│   └── test_todo.py
│
├── .gitignore
└── README.md