from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Configuración de la base de datos
DATABASE = 'database.db'
