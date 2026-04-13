from database.connection import mysql
from werkzeug.security import check_password_hash

class Usuario:

    @staticmethod
    def login(correo, password):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuario WHERE correo = %s", (correo,))
        user = cursor.fetchone()

        if user:
            stored_password = user[4]  # posición password
            if check_password_hash(stored_password, password):
                return user
        return None