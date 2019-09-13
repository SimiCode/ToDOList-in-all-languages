# ToDoList JavaScript implementation

A simple implementation of a ToDoList in Node.js

## Getting Started

- Install all dependencies `npm install`

- Start the server `npm start`

### Consuming the API

Endpoint | Body | Response
-------- | ---- | --------
GET /api/v1/task | | A list of objects
POST /api/v1/task | taskName, taskCategory | Task successfully added
DELETE /api/v1/task | taskName | Task successfully deleted
