from helper.task_iterator import TaskIterator


def test_task_iterator():
    task_example = [
        {"type": "sleep", "payload": {"seconds": 1}},
        {"type": "url_check", "payload": {"url": "https://example.com"}},
    ]

    assert list(TaskIterator(task_example)) == task_example


def test_task_iterator_empty():
    task_example = []

    assert list(TaskIterator(task_example)) == []