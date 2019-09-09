
work_tasks = Tasks
print(work_tasks.tasks)


work_tasks.add_task('Buy tomatoes', 'home')
work_tasks.add_task('Install Kali', 'work')
print(work_tasks.get_tasks())


work_tasks.delete('Install Kali')
print(work_tasks.get_tasks())

work_tasks.add_task('Install Kali', 'work')
Tasks.delete('Call Ray')

print(Tasks.get_tasks())

