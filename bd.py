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

def obtener_todos_registros(tabla):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    habitaciones = []
    
    strsql = 'SELECT * FROM {}'.format(tabla)
    
    cursor.execute(strsql)
    
    habitaciones  = cursor.fetchall()
    conexion.close()
    
    return habitaciones 

def insertar_usuario(nombre, apellido, correo, contraseña):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    strsql = "INSERT INTO Usuario (nombre, apellido, correo, contraseña) VALUES ('{}','{}','{}','{}')".format(nombre, apellido, correo, contraseña)
    
    cursor.execute(strsql)
    conexion.commit()
    conexion.close()

def insertar_habitaciones(Nombre,Baños,Camas,Huespedes,Aire_Acondicionado,WiFi,Cocina,Precio_Noche):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    strsql = "INSERT INTO Habitacion (Nombre,Baños,Camas,Huespedes,Aire_Acondicionado,WiFi,Cocina,Precio_Noche) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(Nombre,Baños,Camas,Huespedes,Aire_Acondicionado,WiFi,Cocina,Precio_Noche)
    
    cursor.execute(strsql)
    conexion.commit()
    conexion.close()

def eliminar_habitaciones(idhabitacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    strsql = "DELETE FROM Habitacion WHERE  idhabitacion ='%s'" % (idhabitacion)

    cursor.execute(strsql)
    conexion.commit()
    conexion.close()

def obtener_habitacion_por_id(idhabitacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    strsql = "SELECT idhabitacion, Nombre, Baños, Camas, Huespedes, Aire_Acondicionado, WiFi, Cocina, Precio_Noche FROM Habitacion WHERE idhabitacion ='%s'" % (idhabitacion)
    
    cursor.execute(strsql)
    habitacion  = cursor.fetchone()
    conexion.commit()
    conexion.close()

    return habitacion

def actualizar_habitaciones(Nombre,Baños,Camas,Huespedes,Aire_Acondicionado,WiFi,Cocina,Precio_Noche,idhabitacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    strsql = "UPDATE Habitacion SET Nombre = '%s', Baños = '%s', Camas = '%s', Huespedes = '%s', Aire_Acondicionado = '%s', WiFi = '%s', Cocina = '%s', Precio_Noche = '%s' WHERE idhabitacion ='%s'" % (Nombre,Baños,Camas,Huespedes,Aire_Acondicionado,WiFi,Cocina,Precio_Noche,idhabitacion)

    cursor.execute(strsql)

    conexion.commit()
    conexion.close()

