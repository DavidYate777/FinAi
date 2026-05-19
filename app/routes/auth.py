from flask import Blueprint, render_template

# Registramos el blueprint con el prefijo /auth
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('registro.html')

# Rutas temporales de previsualización para tus tableros
@auth_bp.route('/dashboard/admin')
def admin_dashboard():
    return render_template('admin/dashboard.html')

@auth_bp.route('/dashboard/cliente')
def cliente_dashboard():
    return render_template('cliente/dashboard.html')