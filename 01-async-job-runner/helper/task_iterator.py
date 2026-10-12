class TaskIterator:
    def __init__(self, tasks):
        self.tasks = tasks
        self.length = len(tasks)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration

        self.index += 1
        return self.tasks[self.index-1]
