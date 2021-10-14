from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def bienvenido():
    return render_template('welcome.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('Dashboard.html')

@app.route('/bedrooms')
def bedrooms():
    return render_template('bedrooms.html')

