from CasaApuestas.utils.conexion import get_mysql_conection
from CasaApuestas.utils.loging import log
from CasaApuestas.clases.caballos import Caballo

class caballosDAO:
    """
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    """
    _SELECCIONAR = 'SELECT * FROM caballos ORDER BY id'
    _SELECCIONAR_CARRERA = 'SELECT * FROM caballos WHERE id_carrera=%s'
    _INSERTAR = 'INSERT INTO caballos(nombre, fecha_nacimiento, velocidad, experiencia, valor_apuesta, id_carrera) ' \
                'VALUES(%s, %s, %s, %s, %s, %s) '
    _ACTUALIZAR = 'UPDATE caballos SET nombre=%s, fecha_nacimiento=%s, velocidad=%s, experiencia=%s, ' \
                  'valor_apuesta=%s, id_carrera=%s WHERE id=%s '
    _ACTUALIZAR_EXPERIENCIA = 'UPDATE caballos SET experiencia=%s WHERE id=%s '
    _ELIMINAR = 'DELETE FROM caballos WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                caballos = []
                for registro in registros:
                    caballo = Caballo(registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[0])
                    caballos.append(caballo)
                conexion.commit()
                return caballos

    @classmethod
    def seleccionar_carrera(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR_CARRERA, (gran_premio.id,))
                registros = cursor.fetchall()
                caballos = []
                for registro in registros:
                    caballo = Caballo(registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[0])
                    caballos.append(caballo)
                conexion.commit()
                return caballos

    @classmethod
    def insertar(cls, caballo):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (caballo.nombre, caballo.fecha_nacimiento, caballo.velocidad, caballo.experiencia, caballo.valor_apuesta, caballo.id_carrera)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'caballo insertado: {caballo}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def actualizar(cls, caballo):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (caballo.nombre, caballo.fecha_nacimiento, caballo.velocidad, caballo.experiencia, caballo.valor_apuesta, caballo.id_carrera, caballo.id)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'caballo actualizado: {caballo}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def actualizar_experiencia(cls, caballo):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (caballo.experiencia, caballo.id)
                cursor.execute(cls._ACTUALIZAR_EXPERIENCIA, valores)
                log.debug(f'caballo actualizado: {caballo}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def eliminar(cls, caballo):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, (caballo.id,))
                log.debug(f'caballo eliminado: {caballo}')
                conexion.commit()
                return cursor.rowcount
