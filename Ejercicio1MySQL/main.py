import Proyecto.utils.loging as log
import Proyecto.utils.conexion as con

try:
    conexion = con.get_mysql_conection()
    with conexion:
        cursor = conexion.cursor()
        sentencia = 'Select nombre from personas'
        cursor.execute(sentencia)
        nombres = cursor.fetchall()
        log.debug(f"Todos los nombres de la tabla personas: {nombres}")
        log.debug("-------------------------------")
        sentencia = "SELECT * FROM personas WHERE email LIKE '%@gmail.com';"
        cursor.execute(sentencia)
        gmail = cursor.fetchall()
        log.debug("Todos los datos de las personas con email acabado en @gmail.com: ", gmail)
        sentencia = "SELECT * FROM personas WHERE email LIKE '%@gmail.com'"
        cursor.execute(sentencia)
        gmail = cursor.fetchall()
        sentencia = "SELECT * FROM personas WHERE email not LIKE '%@gmail.com'"
        cursor.execute(sentencia)
        no_gmail = cursor.fetchall()
        for persona in no_gmail:
            index, nombre, apellidos, email = persona
            nuevo_email_partes = email.split("@")
            nuevo_email = (nuevo_email_partes[0] + "@gmail.com")
            sentencia = f"UPDATE personas SET email=%s WHERE id=%s"
            valores = (nuevo_email, index)
            cursor.execute(sentencia, valores)
        conexion.commit()
        cursor = conexion.cursor()
        sentencia = "SELECT * FROM personas WHERE email LIKE '%@gmail.com';"
        cursor.execute(sentencia)
        conexion.commit()
except Exception as e:
    conexion.rollback()
    log.error(f'Ocurrió un error, se hizo rollback: {e}')
