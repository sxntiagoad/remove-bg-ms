from flask import Flask
from routes.bg_remove_routes import remove_bg

app = Flask(__name__)

# Registra las rutas
app.register_blueprint(remove_bg)

if __name__ == '__main__':
    app.run(debug=True)