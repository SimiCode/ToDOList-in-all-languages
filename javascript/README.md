# ToDoList JavaScript implementation

A simple implementation of a ToDoList in Node.js

## Getting Started

- Install all dependencies `npm install`

- Start the server `npm start`

### Consuming the API

Endpoint | Body | Response
-------- | ---- | --------
GET /api/v1/tasks | | A list of objects
POST /api/v1/tasks | taskName, taskCategory | Task successfully added
DELETE /api/v1/tasks | taskName | Task successfully deleted
