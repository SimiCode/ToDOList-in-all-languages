from flask import Flask, request, jsonify
import controllers


app = Flask(__name__)


@app.route('/api/v1/tasks', methods=['GET'])
def get_all_tasks():
    tasks = controllers.get_tasks()
    return jsonify(tasks), 200


@app.route('/api/v1/tasks', methods=['POST'])
def add_new_task():
    data = request.get_json()
    task = data.get('task')
    category = data.get('type')
    controllers.add_task(task, category)
    return "success", 201