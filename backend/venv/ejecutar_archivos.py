from flask import Flask
from multiprocessing import Process

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

def run_flask_app():
    app.run()

if __name__ == '__main__':
    # Crear un proceso para ejecutar la aplicación Flask
    flask_process = Process(target=run_flask_app)

    # Iniciar el proceso de Flask
    flask_process.start()

    # Realizar otras tareas en el proceso principal
    # ...

    # Esperar a que el proceso de Flask termine
    flask_process.join()
