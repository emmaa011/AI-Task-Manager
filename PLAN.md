# AI Task Manager — Project Plan

## 1. Project Goal

Build a simple command-line Task Manager in Python that allows users to manage their personal tasks.

The application will use JSON for persistent data storage and will include input validation, automated tests, documentation, and error handling.

AI tools may be used during development to assist with planning, implementation, debugging, testing, and documentation, while the final code and decisions will be reviewed and understood by the developer.

---

## 2. Core Features

The Task Manager will support the following operations:

- Add a new task
- View all tasks
- Mark a task as completed
- Delete a task
- Save tasks to a JSON file
- Load tasks from a JSON file when the application starts
- Validate user input
- Handle invalid task IDs and other common errors gracefully

The application will run through a command-line interface (CLI).

---

## 3. Task Data Model

Each task will contain the following information:

```text
Task
├── id
├── title
└── completed
```

### Fields

- `id` — A unique identifier for the task.
- `title` — The text describing what needs to be done.
- `completed` — A Boolean value indicating whether the task is completed.

Example:

```json
{
    "id": 1,
    "title": "Complete Python project",
    "completed": false
}
```

---

## 4. User Stories

### Add Task

As a user, I want to add a task so that I can keep track of something I need to do.

### View Tasks

As a user, I want to view my tasks so that I can see what needs to be done.

### Complete Task

As a user, I want to mark a task as completed so that I can track my progress.

### Delete Task

As a user, I want to delete a task so that I can remove tasks that are no longer needed.

### Persistent Storage

As a user, I want my tasks to be saved so that they are still available when I restart the application.

### Input Validation

As a user, I want invalid input to be handled properly so that the application does not crash unexpectedly.

---

## 5. Acceptance Criteria

The project will be considered complete when:

- A user can add a task.
- A user can view all tasks.
- A user can mark a task as completed.
- A user can delete a task.
- Tasks are saved to a JSON file.
- Existing tasks are loaded when the application starts.
- Each task has a unique ID.
- Task titles cannot be empty.
- Invalid task IDs are handled without crashing the application.
- Invalid menu/input choices are handled properly.
- The application can run successfully from the command line.
- Automated tests cover the main task-management functionality.
- The project includes a README explaining how to use it.
- The project includes a reflection describing how AI was used during development.
- The project includes appropriate Git/GitHub files and documentation.

---

## 6. Edge Cases

The application should handle situations such as:

- The user enters an empty task title.
- The user enters an invalid menu option.
- The user enters a non-numeric task ID.
- The user enters a task ID that does not exist.
- The JSON file does not exist yet.
- The JSON file contains invalid or corrupted data.
- The task list is empty.
- The user tries to complete an already completed task.
- The user tries to delete a task that does not exist.

The application should handle these situations gracefully instead of crashing.

---

## 7. Out of Scope

The following features are intentionally excluded from the initial version:

- User accounts and authentication
- Cloud/database storage
- Web or mobile interface
- Multi-user collaboration
- Task sharing
- Notifications and reminders
- Advanced AI features inside the application
- Complex task scheduling
- External APIs

The goal is to keep the project focused on building a reliable Python CLI application and demonstrating the development process.