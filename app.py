from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def bienvenido():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    print(request.form)
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

