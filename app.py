from flask import Flask, jsonify
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

if __name__ == '__main__':
    app.run(debug=True)