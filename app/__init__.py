import os
from flask import Flask
from config import Config

def create_app():
    # Inicializa Flask apuntando correctamente a su propio paquete
    app = Flask(__name__)
    app.config.from_object(Config)

    # Importar y registrar el Blueprint de autenticación
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    @app.route('/')
    def index():
        return "Servidor activo. Ve a <a href='/auth/login'>Login</a>"

    return app