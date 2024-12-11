from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Registrar Blueprints
from app.routes.bg_remove_routes import bgRemove_bp
app.register_blueprint(bgRemove_bp)

@app.route('/')
def home():
    return "¡Bienvenido al Servicio de Remover Fondos!"
