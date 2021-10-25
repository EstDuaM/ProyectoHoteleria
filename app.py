from flask import Flask, render_template, request
from werkzeug.utils import redirect
import werkzeug.security as ws
#import smtplib
import bd

app = Flask(__name__)
app.secret_key = 'mi_llave_secreta'

@app.route('/')
def bienvenido():
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
            bd.insertar_usuario(nombre,apellido,correo,ws.generate_password_hash(contraseña))
            return 'Registro exitoso'
        elif request.form['boton-env'] == "siguiente":
            correoIni = request.form['correo-ini']
            contraIni = request.form["contra-ini"]
            return 'Inicio de sesión exitoso'
        
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
