import sqlite3

from sqlite3 import Error


def obtener_conexion():
    try:
        conexion = sqlite3.connect('DBradHotel.db')
        return conexion
    except Error: 
        print(Error)

def obtener_registro(tabla, condicion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    if condicion == None:
        strsql = 'SELECT * FROM {}'.format(tabla)
    else: strsql = 'SELECT * FROM {} WHERE {}'.format(tabla, condicion)
    
    cursor.execute(strsql)
    
    datos = cursor.fetchall()
    conexion.close()
    
    return datos

def insertar_usuario(nombre, apellido, correo, contraseña):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    strsql = "INSERT INTO Usuario (nombre, apellido, correo, contraseña) VALUES ('{}','{}','{}','{}')".format(nombre, apellido, correo, contraseña)
    
    cursor.execute(strsql)
    conexion.commit()
    conexion.close()

def insertar_habitaciones(nombreHabitacion,descripcionHabitacion,equipoHabitacion,tamanoHabitacion,noPersonas,noCamasInd,noCamasDob,ubicacionHabitacion,vistaHabitacion,extensionHabitacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    strsql = "INSERT INTO Habitacion (nombreHabitacion,descripcionHabitacion,equipoHabitacion,tamanoHabitacion,noPersonas,noCamasInd,noCamasDob,ubicacionHabitacion,vistaHabitacion,extensionHabitacion) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(nombreHabitacion,descripcionHabitacion,equipoHabitacion,tamanoHabitacion,noPersonas,noCamasInd,noCamasDob,ubicacionHabitacion,vistaHabitacion,extensionHabitacion)
    
    cursor.execute(strsql)
    conexion.commit()
    conexion.close()
