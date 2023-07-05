import cx_Oracle

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

    sql_select = "SELECT * FROM CLIENTE"

    cursor.execute(sql_select)
    # Obtener todas las filas de resultados
    rows = cursor.fetchall()

    # Mostrar los resultados
    
    for row in rows:
        print(row)

    # Cerrar la conexión
    connection.close()
except cx_Oracle.Error as error:
    print("Error al conectar a Oracle: ", error)