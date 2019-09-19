# ToDoList Python implementation

A simple implementation of a ToDoList in Python Flask


## Getting Started

- Install all dependencies `pip install -r requirements.txt`

- Start the server `python run.py`


### Consuming the API

Endpoint | Body | Response
-------- | ---- | --------
GET /api/v1/tasks | | A list of objects
POST /api/v1/tasks | taskName, taskCategory | Task successfully added
DELETE /api/v1/tasks | taskName | Task successfully deleted
