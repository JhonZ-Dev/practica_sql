from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Configuración de la base de datos
DATABASE = 'database.db'

# Función para conectarse a la base de datos
def connect_db():
    return sqlite3.connect(DATABASE)
# Función para crear la tabla de usuarios
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
# Ruta para mostrar la lista de usuarios
@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)
# Ruta para agregar un nuevo usuario
@app.route('/add', methods=['POST'])
def add_user():
    username = request.form['username']
    email = request.form['email']

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))
# Ruta para eliminar un usuario
@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))
# Ruta para actualizar un usuario
@app.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    new_username = request.form['new_username']
    new_email = request.form['new_email']

