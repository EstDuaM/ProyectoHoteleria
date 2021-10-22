from flask import Flask, render_template, request
import smtplib
import bd

app = Flask(__name__)

@app.route('/')
def bienvenido():
    bd.sql_conexion
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    #print(request.form)
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form["apellido"]
        correo = request.form["correo"]
        contraseña = request.form["contra"]
        
        print(nombre)
        print(apellido)
        print(correo)
        print(contraseña)
        return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('Dashboard.html')

@app.route('/bedrooms')
def bedrooms():
    return render_template('bedrooms.html')

@app.route('/bedrooms_actions')
def bedroom_actions():
    return render_template('bedroom-actions.html')

