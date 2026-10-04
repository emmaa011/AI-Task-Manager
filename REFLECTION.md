# AI-Assisted Development Reflection

## 1. Where AI Saved Me the Most Time

AI saved me the most time during the planning, implementation, testing, and debugging stages of the project.

It helped me break the Task Manager into smaller components, such as adding tasks, viewing tasks, completing tasks, deleting tasks, JSON storage, input validation, and testing. It also helped explain Python concepts and suggested code that I could review, run, and modify.

Instead of trying to design the entire application at once, I was able to develop it step by step and test each part before moving forward.

AI was particularly useful when identifying edge cases, such as empty task titles, invalid task IDs, missing JSON files, and corrupted JSON data.

## 2. Example of Incorrect AI-Generated Code

One issue was discovered while running the automated tests.

The test expected a newly created task to have:

```python
"completed": False
```

but the implementation temporarily contained an incorrect value that caused the test to fail.

The test output showed:

```text
AssertionError: True is not false
```

This helped identify that the implementation did not match the expected behavior.

I reviewed the code, found the incorrect value, changed it back to:

```python
"completed": False
```

and ran the tests again. The tests then passed successfully.

I also encountered an indentation error while modifying the `load_tasks()` method. Reviewing the Python error message helped me identify that the indentation did not match the surrounding code, so I corrected the structure and ran the tests again.

These experiences showed me that AI-generated code still needs to be reviewed, tested, and verified by the developer.

## 3. What I Understand Better Now

After reviewing and testing the AI-assisted code, I understand Python classes and methods better.

I now have a clearer understanding of how a class such as `TaskManager` can store application data and provide methods for operations such as adding, completing, and deleting tasks.

I also understand better how JSON can be used to persist application data and how automated tests can verify whether the application behaves as expected.

Working with pytest also helped me understand how individual application behaviors can be tested automatically instead of checking everything manually.

Most importantly, I learned that using AI in software development does not remove the need for the developer to understand the requirements, review the generated code, test it, find problems, and make the final decisions.

## 4. How AI Was Used

AI was used as a development assistant for:

- Project planning
- Breaking requirements into smaller tasks
- Generating and explaining code
- Identifying possible edge cases
- Creating automated tests
- Debugging errors
- Improving error handling
- Supporting documentation

The generated code was reviewed, executed, and tested before being considered part of the project.