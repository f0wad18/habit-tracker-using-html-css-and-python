# Habit Tracker Application Using HTML, CSS, and Python

The Habit Tracker project is a web-based application developed using HTML, CSS, and Python. This application helps users to monitor and manage their habits effectively. The front-end of the application is built with HTML for structuring the content and CSS for styling, ensuring a user-friendly and visually appealing interface. The back-end is powered by Python, which handles the logic and functionality of the application.

The Key feature of this Habit Tracker is that:
- **Users can add new habits, set goals, and mark habits as completed.**

This project serves as a practical tool for individuals looking to build and maintain positive habits, offering a seamless and interactive experience through the integration of front-end and back-end technologies.

## How Everything Works

The back-end of the Habit Tracker is built using Flask, a Python web framework. Here is an overview of the main functionalities:

### Loading and Saving Habits

Habits are stored in a JSON file (`habits.json`). The functions `load_habits()` and `save_habits(habits)` handle loading and saving habit data to this file.

### Routes and API Endpoints

- **Index Route**: Renders `index.html` and loads initial habits data.
  ```python
  @app.route('/')
  def index():
      habits = load_habits()
      return render_template('index.html', habits=habits)
  ```

- **Add Habit**: Adds a new habit to the list.
  ```python
  @app.route('/add_habit', methods=['POST'])
  def add_habit():
      habit_name = request.form['habit_name']
      habits = load_habits()
      new_habit = {'name': habit_name, 'completed': False}
      habits.append(new_habit)
      save_habits(habits)
      return jsonify({'message': 'Habit added successfully'})
  ```

- **Complete Habit**: Marks a habit as completed.
  ```python
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
  ```

- **Incomplete Habit**: Marks a habit as incomplete.
  ```python
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
  ```

## Future Updates

- **User Authentication**: Implementing secure user authentication and authorization.
- **Advanced Analytics**: Adding more advanced analytics and reporting features for habit tracking.
- **Mobile Support**: Enhancing mobile support for better usability on smartphones and tablets.
- **Social Sharing**: Allowing users to share their progress on social media platforms.
- **Gamification**: Introducing gamification elements like rewards and badges to motivate users.

## Getting Started

To run this application locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/f0wad18/habit-tracker-using-html-css-and-python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd habit-tracker-using-html-css-and-python
   ```
3. Install the required packages:
   ```bash
   pip install flask
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your web browser and go to `http://127.0.0.1:5000/`.

Feel free to contribute to the project by submitting issues or pull requests.

## License

MIT License

Copyright (c) 2024 f0wad18

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

This `README.md` file now includes a comprehensive description, features, functionality, future updates, and instructions for running the project locally.
