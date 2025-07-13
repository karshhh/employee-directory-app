from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB = 'employees.db'

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']
        role = request.form['role']
        conn = sqlite3.connect(DB)
        conn.execute('INSERT INTO employees (name, department, role) VALUES (?, ?, ?)', (name, department, role))
        conn.commit()
        conn.close()
        return redirect('/')
    conn = sqlite3.connect(DB)
    employees = conn.execute('SELECT name, department, role FROM employees').fetchall()
    conn.close()
    return render_template('index.html', employees=employees)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')
