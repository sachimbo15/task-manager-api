from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

tasks = [
    {"id": 1, "title": "some task", "completed": False},
    {"id": 2, "title": "some task", "completed": True}  
]

@app.route('/tasks')
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    print("Received a POST request!")  # Debugging line
    data = request.get_json()
    print("Received data:", data)
    return jsonify({"message": "Task received"}), 201


@app.route('/tasks/<int:task_id>', methods=['GET'])
def fetch_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data["title"]
            task["completed"] = data.get("completed", task["completed"])
            return jsonify({"message": "Task updated", "task": task}), 200
        return jsonify({"error": "Task not found"}), 404


        


if __name__ == '__main__':
    app.run(debug=True)