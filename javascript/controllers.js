let tasks = [];

exports.addTask = (req, res) => {
    const newTask = { taskName: req.body.taskName, taskCategory: req.body.taskCategory };

    for (let task of tasks) {
        if (task.taskName === newTask.taskName) {
            return res.status(400).json({ error: 'Task name already exists', status: 400 });
        }
    }

    tasks.push(newTask);
    return res.status(201).json({ message: 'Task successfuly added', status: 201 });
}

exports.getTasks = (req, res) => {
    return res.status(200).json({ tasks })
}

exports.deleteTask = (req, res) => {
    const taskName = req.body.taskName;

    tasks.forEach(task => {
        if (task.taskName === taskName) {
            tasks.splice(tasks.indexOf(task), 1);
            return res.status(200).json({ message: 'Task deleted', status: 200 });
        }
    })

    return res.status(400).json({ error: 'Task does not exist', status: 400 });
}
