from flask import Flask, render_template, request, redirect, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'clave_super_secreta'

@app.route('/')
def index():
    conn = sqlite3.connect('services.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, descripcion, precio FROM servicios ORDER BY id")
    servicios = cursor.fetchall()
    conn.close()
    return render_template('servicios.html', servicios=servicios)

if __name__ == '__main__':
    app.run(debug=True)
