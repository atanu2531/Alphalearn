from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Database setup
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return "Welcome to the Science Learning App!"

# Example endpoint for getting lessons
@app.route('/lessons/<subject>')
def get_lessons(subject):
    conn = get_db_connection()
    lessons = conn.execute('SELECT * FROM lessons WHERE subject = ?', (subject,)).fetchall()
    conn.close()
    return jsonify([dict(row) for row in lessons])

if __name__ == '__main__':
    app.run(debug=True)
