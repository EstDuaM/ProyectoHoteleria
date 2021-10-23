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

    if request.method == 'GET':
        return render_template('login.html')
    else: 
        if request.form['boton-env'] == "anterior":
            nombre = request.form['nombre']
            apellido = request.form["apellido"]
            correo = request.form["correo"]
            contraseña = request.form["contraseña"]
            return redirect('/bedrooms')
        elif request.form['boton-env'] == "siguiente":
            correoIni = request.form['correo-ini']
            contraIni = request.form["contra-ini"]
            return redirect('/bedrooms')

@app.route('/dashboard')
def dashboard():
    return render_template('Dashboard.html')

@app.route('/bedrooms')
def bedrooms():
    return render_template('bedrooms.html')

@app.route('/bedrooms_actions')
def bedroom_actions():
    return render_template('bedroom-actions.html')

@app.route('/bedrooms_qualify')
def bedroom_qualify():
    return render_template('bedroom-qualify.html')

