from flask import Flask, render_template, request, redirect, jsonify, send_file, session
from werkzeug.utils import redirect
import werkzeug.security as ws
import bd
from flask import make_response

app = Flask(__name__)
app.secret_key = 'mi_llave_secreta'

@app.before_request
def antes_peticion():
    if 'correo' not in session and request.endpoint in ['perfil']:
       return redirect('/')

    elif 'correo' in session and request.endpoint in ['login']:
        return redirect('/perfil/{}'.format(session['correo']))

@app.route('/')
def bienvenido():
    return render_template('welcome.html')
    

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    else: 
        #Validar los valores de los formularios de registro
        if request.form['boton-env'] == "anterior":
            nombre = request.form['nombre']
            apellido = request.form["apellido"]
            correo = request.form["correo"]
            contraseña = request.form["contraseña"]
            bd.insertar_usuario(nombre,apellido,correo,ws.generate_password_hash(contraseña))
            session['correo'] = correo
            return redirect('/perfil/{}'.format(correo))
        #Validar los valores de los formularios de inicio de sesión
        elif request.form['boton-env'] == "siguiente":
            correoIni = request.form['correo-ini']
            registro_usuario = bd.obtener_registro('Usuario', "correo='{}'".format(correoIni))
            contraseña_bd = registro_usuario[0][4]
            if registro_usuario is not None:
                contraIni = request.form["contra-ini"]
                contraseña_igual = ws.check_password_hash(contraseña_bd, contraIni)
                if contraseña_igual:
                    session['correo'] = correoIni
                    return redirect('/perfil/{}'.format(correoIni))
            return render_template('login.html')

#sesión de perfil de usuario       
@app.route('/perfil')
@app.route('/perfil/<correo>')
def perfil(correo=None):
    if correo:
        registro_usuario = bd.obtener_registro('Usuario', "correo='{}'".format(correo))
        if registro_usuario:
            
            id_usuario = registro_usuario[0][0]
            
            agregar = False
            if correo == session['correo']:
                agregar = True
            
            return render_template('perfil-usuario.html', correo = registro_usuario, agregar = agregar)     
    else:
        return render_template('perfil-usuario.html')        

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

@app.route('/cerrar_sesion')
def cerrar_sesion():
    if 'correo' in session:
        session.pop('correo')
        return redirect('/')