from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Function to load habits data from JSON file
def load_habits():
    habits = []
    if os.path.exists('habits.json'):
        with open('habits.json', 'r') as file:
            habits = json.load(file)
    return habits

# Function to save habits data to JSON file
def save_habits(habits):
    with open('habits.json', 'w') as file:
        json.dump(habits, file, indent=4)

# Route to render index.html and load initial habits data
@app.route('/')
def index():
    habits = load_habits()
    return render_template('index.html', habits=habits)

# API endpoint to handle adding new habit
@app.route('/add_habit', methods=['POST'])
def add_habit():
    habit_name = request.form['habit_name']
    habits = load_habits()
    new_habit = {'name': habit_name, 'completed': False}
    habits.append(new_habit)
    save_habits(habits)
    return jsonify({'message': 'Habit added successfully'})

# API endpoint to handle completing a habit
@app.route('/complete_habit', methods=['POST'])
def complete_habit():
    habit_name = request.form['habit_name']
    habits = load_habits()
    for habit in habits:
        if habit['name'] == habit_name:
            habit['completed'] = True
            break
    save_habits(habits)
    return jsonify({'message': 'Habit marked as completed'})

# API endpoint to handle marking a habit as incomplete
@app.route('/incomplete_habit', methods=['POST'])
def incomplete_habit():
    habit_name = request.form['habit_name']
    habits = load_habits()
    for habit in habits:
        if habit['name'] == habit_name:
            habit['completed'] = False
            break
    save_habits(habits)
    return jsonify({'message': 'Habit marked as incomplete'})

if __name__ == '__main__':
    app.run(debug=True)
