from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List of dictionaries to store tasks
tasks = [
    {'id': 1, 'title': "Buy Groceries", 'description': "Milk, Bread, Flour, sugar"},
    {'id': 2, 'title': "Study", 'description': "Review Python Flask"},
]

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route for creating a new task
@app.route('/create', methods=['POST'])
def create():
    if request.method == "POST":
        new_id = len(tasks) + 1
        title = request.form['title']
        description = request.form['description']
        tasks.append({'id': new_id, 'title': title, 'description': description})
        return redirect(url_for('index'))

# Route for editing an existing task
@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    task = next((task for task in tasks if task['id'] == id), None)
    if not task:
        return "Task not found", 404
    if request.method == "POST":
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

# Route for deleting a task
@app.route('/delete/<int:id>', methods=["POST"])
def delete(id):
    global tasks
    tasks = [task for task in tasks if task['id'] != id]  # Update the tasks list
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
