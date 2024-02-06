from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Configuración de la base de datos
DATABASE = 'database.db'

# Función para conectarse a la base de datos
def connect_db():
    return sqlite3.connect(DATABASE)
