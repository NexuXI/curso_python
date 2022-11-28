from CasaApuestas.utils.conexion import get_mysql_conection
from CasaApuestas.utils.loging import log
from CasaApuestas.clases.apostantes import Apostante

class apostantesDAO:
    """
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    """
    _SELECCIONAR = 'SELECT * FROM apostantes ORDER BY id'
    _INSERTAR = 'INSERT INTO apostantes(nombre, saldo) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE apostantes SET nombre=%s, saldo=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM apostantes WHERE id=%s'
    _ACTUALIZAR_SALDO = 'UPDATE apostantes SET experiencia=%s WHERE id=%s '

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                apostantes = []
                for registro in registros:
                    apostante = Apostante(registro[1], registro[2], registro[0])
                    apostantes.append(apostante)
                conexion.commit()
                return apostantes

    @classmethod
    def insertar(cls, apostante):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (apostante.nombre, apostante.saldo)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'apostante insertado: {apostante}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def actualizar(cls, apostante):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (apostante.nombre, apostante.saldo, apostante.id)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'apostante actualizado: {apostante}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def actualizar_saldo(cls, apostante):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (apostante.saldo, apostante.id)
                cursor.execute(cls._ACTUALIZAR_SALDO, valores)
                log.debug(f'apostante actualizado: {apostante}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def eliminar(cls, apostante):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, (apostante.id,))
                log.debug(f'apostante eliminado: {apostante}')
                conexion.commit()
                return cursor.rowcount
