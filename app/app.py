from flask import Flask
from routes.bg_remove_routes import bgRemove_bp

app = Flask(__name__)

# Registra las rutas
app.register_blueprint(bgRemove_bp)

if __name__ == '__main__':
    app.run(debug=True)