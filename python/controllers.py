from models import Tasks, Task


def get_tasks():
 return Tasks.get_tasks()


def add_task(task, category):
	Tasks.add_task(task, category)
