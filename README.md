# AI Task Manager

A simple command-line task manager built with Python. The project was developed using an AI-assisted software development approach, with AI used for planning, coding support, testing, debugging, and documentation.

## Features

- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Save tasks to a JSON file
- Load tasks when the application starts
- Validate task input
- Handle invalid task IDs and menu options
- Automated tests for core functionality

## Technologies Used

- Python 3
- JSON
- Python `unittest`
- Command-Line Interface (CLI)

## Project Structure

```text
AI-Task-Manager/
│
├── main.py
├── task_manager.py
├── test_task_manager.py
├── tasks.json
├── PLAN.md
├── README.md
└── REFLECTION.md
```

### File Descriptions

- `main.py` — Provides the command-line interface and handles user interaction.
- `task_manager.py` — Contains the task-management logic and JSON storage functionality.
- `test_task_manager.py` — Contains automated tests for the Task Manager.
- `tasks.json` — Stores tasks for persistent storage.
- `PLAN.md` — Contains the project plan, requirements, user stories, and acceptance criteria.
- `REFLECTION.md` — Documents the use of AI during development and lessons learned.
- `README.md` — Provides project documentation and usage instructions.

## How to Run

Make sure Python is installed on your computer.

Open a terminal in the project directory and run:

```bash
python main.py
```

The application will display a menu:

```text
=== AI Task Manager ===
1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit
```

Choose an option by entering the corresponding number.

## Running the Tests

The project uses Python's built-in `unittest` framework.

Run the tests with:

```bash
python -m unittest test_task_manager.py
```

A successful test run should display:

```text
......
----------------------------------------------------------------------
Ran 6 tests

OK
```

## Data Storage

Tasks are stored in `tasks.json`.

Each task contains:

```json
{
    "id": 1,
    "title": "Learn Python",
    "completed": false
}
```

The JSON file allows tasks to remain available after the application is closed and started again.

## AI-Assisted Development

AI was used as a development assistant during the project for:

- Project planning
- Breaking requirements into smaller tasks
- Code generation and explanation
- Identifying edge cases
- Creating automated tests
- Debugging
- Improving error handling
- Documentation

AI-generated code was reviewed, tested, and corrected when necessary. The developer remained responsible for understanding the requirements, making implementation decisions, testing the application, and verifying the final result.

More details about the development experience are provided in `REFLECTION.md`.