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




if __name__ == '__main__':
    app.run(debug=True)