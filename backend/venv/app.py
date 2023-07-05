from flask import Flask, jsonify, request
from flask_cors import CORS
import cx_Oracle
import json
app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from the backend!'}
    return jsonify(data)

# Configuración de la conexión
username = 'C##REDES'  # Nombre de usuario de la base de datos
password = 'REDES'  # Contraseña del usuario
host = 'localhost'
port = 1522
service_name = 'XE'

try:
    # Crear la cadena de conexión
    dsn = cx_Oracle.makedsn(host, port, service_name=service_name)

    # Establecer la conexión
    connection = cx_Oracle.connect(username, password, dsn)
    print("conexion con oracle")
    cursor = connection.cursor()
    
    # Cerrar la conexión
    connection.close()
except cx_Oracle.Error as error:
    print("Error al conectar a Oracle: ", error)

if __name__ == '__main__':
    app.run()
