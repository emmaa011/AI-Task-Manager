import json


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        title = title.strip()

        if not title:
            raise ValueError("Task title cannot be empty.")

        task = {
            "id": self.next_id,
            "title": title,
            "completed": False
        }

        self.tasks.append(task)
        self.next_id += 1

        return task

    def get_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return task

        raise ValueError("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return task

        raise ValueError("Task not found.")

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=4)

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.tasks = json.load(file)

            if not isinstance(self.tasks, list):
                raise ValueError("Invalid task data.")

            if self.tasks:
                self.next_id = max(task["id"] for task in self.tasks) + 1
            else:
                self.next_id = 1

        except FileNotFoundError:
            self.tasks = []
            self.next_id = 1

        except (json.JSONDecodeError, ValueError):
            print(
                "Warning: Could not load task data. "
                "Starting with an empty task list."
            )
            self.tasks = []
            self.next_id = 1