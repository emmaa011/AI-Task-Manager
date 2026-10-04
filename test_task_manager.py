from task_manager import TaskManager


def test_add_task():
    manager = TaskManager()

    task = manager.add_task("Learn Python")

    assert task["id"] == 1
    assert task["title"] == "Learn Python"
    assert task["completed"] is False


def test_empty_task_rejected():
    manager = TaskManager()

    try:
        manager.add_task("")
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_whitespace_task_rejected():
    manager = TaskManager()

    try:
        manager.add_task("   ")
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_complete_task():
    manager = TaskManager()

    manager.add_task("Learn Python")
    manager.complete_task(1)

    tasks = manager.get_tasks()

    assert tasks[0]["completed"] is True


def test_delete_task():
    manager = TaskManager()

    manager.add_task("Learn Python")
    manager.delete_task(1)

    assert len(manager.get_tasks()) == 0


def test_invalid_task_id():
    manager = TaskManager()

    try:
        manager.complete_task(999)
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_delete_invalid_task_id():
    manager = TaskManager()

    try:
        manager.delete_task(999)
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_save_and_load_tasks(tmp_path):
    filename = tmp_path / "tasks.json"

    manager = TaskManager()
    manager.add_task("Learn Python")
    manager.add_task("Build Task Manager")

    manager.save_tasks(filename)

    new_manager = TaskManager()
    new_manager.load_tasks(filename)

    assert new_manager.get_tasks() == manager.get_tasks()


def test_load_missing_file(tmp_path):
    filename = tmp_path / "missing.json"

    manager = TaskManager()
    manager.load_tasks(filename)

    assert manager.get_tasks() == []


def test_load_corrupted_json(tmp_path, capsys):
    filename = tmp_path / "corrupted.json"
    filename.write_text("{invalid json")

    manager = TaskManager()
    manager.load_tasks(filename)

    captured = capsys.readouterr()

    assert manager.get_tasks() == []
    assert "Warning" in captured.out