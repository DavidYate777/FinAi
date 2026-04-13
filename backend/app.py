import os
import sys
from flask import Flask

# Asegura que Python reconozca la carpeta 'backend' como módulo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.config import Config
from backend.database.connection import mysql
from backend.routes.auth_routes import auth_bp
from backend.routes.dashboard_routes import dashboard_bp

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "..", "frontend", "templates"),
    static_folder=os.path.join(BASE_DIR, "..", "frontend", "static")
)

app.config.from_object(Config)

# Inicialización de la base de datos
try:
    mysql.init_app(app)
except Exception as e:
    print(f"Aviso: Error de conexión inicial: {e}")

# Registro de Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(debug=True)