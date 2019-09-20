const express = require('express');
const controllers = require('./controllers');

const app = express();

const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.post('/api/v1/tasks', controllers.addTask);
app.get('/api/v1/tasks', controllers.getTasks);
app.delete('/api/v1/tasks', controllers.deleteTask);

app.listen(PORT, () => console.log(`Server is running...
http://localhost:${PORT}
`));
