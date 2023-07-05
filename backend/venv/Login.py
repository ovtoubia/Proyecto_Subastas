from flask import Flask, jsonify, request
from flask_cors import CORS
import cx_Oracle
import json

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

def convertir_a_json(cursor, rows):
    results = []
    columns = [d[0] for d in cursor.description]
    for row in rows:
        results.append(dict(zip(columns,row)))
    return results

@app.route('/api/datosUsuario', methods=['POST'])
def get_datos_usuario():
    # Establecer la conexión
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
        print("Conexión con Oracle establecida")

        # Crear el cursor
        cursor = connection.cursor()

        # Se obtienen los datos que ingresó el usuario
        data = request.json
        print(data)

        # Ejecutar la consulta SQL
        cursor.execute("SELECT * FROM CLIENTE")  # Se buscan todos los usuarios
        rows = cursor.fetchall()  # Se obtienen todos en la variable rows
        print(rows)
        usuarios = convertir_a_json(cursor, rows)
        print(usuarios)
        sesion = False
        for usuario in usuarios:
            if data["username"] == usuario["USUARIO_CLI"] and data["password"] == usuario["CONTRASENA_CLI"]:
                sesion = True
                break

        if sesion:
            response = {'message': 'Datos válidos'}
        else:
            response = {'message': 'Usuario o contraseña inválidos'}

        # Cerrar el cursor
        cursor.close()

        # Cerrar la conexión
        connection.close()
        print(response)
        return jsonify(response)

    except cx_Oracle.Error as error:
        print("Error al conectar a Oracle: ", error)
        return jsonify({'message': 'Error al conectar a la base de datos'})
    
if __name__ == '__main__':
    app.run()