from flask import Blueprint, render_template, request, redirect, url_for

dashboard_bp = Blueprint("dashboard", __name__)

# Base de datos temporal (Mock Data)
# Nota: Al reiniciar el servidor, estos datos se perderán.
movimientos_db = []

def calcular_resumen(movimientos):
    """Calcula ingresos, gastos y balance total."""
    ingresos = sum(m[3] for m in movimientos if m[1] == "Ingreso")
    gastos = sum(m[3] for m in movimientos if m[1] == "Gasto")
    return {
        "ingresos": ingresos,
        "gastos": gastos,
        "balance": ingresos - gastos
    }

@dashboard_bp.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        return registrar_movimiento()

    resumen = calcular_resumen(movimientos_db)
    
    return render_template(
        "dashboard.html", 
        movimientos=reversed(movimientos_db), # Mostrar los más recientes primero
        **resumen
    )

def registrar_movimiento():
    """Maneja la lógica de inserción de datos."""
    try:
        tipo = request.form.get("tipo")
        descripcion = request.form.get("descripcion")
        # Validación básica de datos
        monto_str = request.form.get("monto", "0")
        monto = float(monto_str) if monto_str else 0.0
        
        if not tipo or not descripcion or monto <= 0:
            # Aquí podrías añadir un flash message para feedback profesional
            return redirect(url_for("dashboard.dashboard"))

        nuevo_id = len(movimientos_db) + 1
        movimientos_db.append((nuevo_id, tipo, descripcion, monto))
        
    except ValueError:
        pass # Manejo de error si el monto no es numérico
        
    return redirect(url_for("dashboard.dashboard"))