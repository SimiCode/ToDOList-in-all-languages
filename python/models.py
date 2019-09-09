class Task:
    def __init__(self, task_name, category):
        self.task_name = task_name
        self.category = category


class Tasks:
    tasks = []
    
    @classmethod
    def add_task(cls, task, category):
        cls.tasks.append(Task(task, category))

    @classmethod
    def delete(cls, task_name):
        cls.tasks = [task for task in cls.tasks if task.task_name != task_name]

    @classmethod
    def get_tasks(cls):
        return [(task.task_name, task.category) for task in cls.tasks]

