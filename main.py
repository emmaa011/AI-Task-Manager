from task_manager import TaskManager


def display_tasks(manager):
    tasks = manager.get_tasks()

    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nYour Tasks:")

    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f'{task["id"]}. [{status}] {task["title"]}')


def main():
    manager = TaskManager()
    manager.load_tasks()

    while True:
        print("\n=== AI Task Manager ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            title = input("Enter task title: ")

            try:
                manager.add_task(title)
                manager.save_tasks()
                print("Task added successfully.")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            display_tasks(manager)

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID: "))
                manager.complete_task(task_id)
                manager.save_tasks()
                print("Task completed successfully.")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID: "))
                manager.delete_task(task_id)
                manager.save_tasks()
                print("Task deleted successfully.")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()