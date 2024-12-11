from flask import Flask
from app import create_app
from flask import jsonify

app = create_app()

@app.route('/')
def home():
    return "¡Bienvenido al Servicio de Remover Fondos!"

if __name__ == '__main__':
    app.run(debug=True)

