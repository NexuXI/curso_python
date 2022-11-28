from CasaApuestas.utils.conexion import get_mysql_conection
from CasaApuestas.utils.loging import log
from CasaApuestas.clases.gran_premio import Gran_premio

class gran_premioDAO:
    """
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    """
    _SELECCIONAR = 'SELECT * FROM gran_premio ORDER BY id'
    _SELECCIONAR_ESPECIFICO = 'SELECT * FROM gran_premio WHERE id=%s'
    _INSERTAR = 'INSERT INTO gran_premio(nombre, distancia, num_carreras) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE gran_premio SET nombre=%s, distancia=%s num_carreras=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM gran_premio WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                grandes_premios = []
                for registro in registros:
                    gran_premio = Gran_premio(registro[1], registro[2], registro[3], registro[0])
                    grandes_premios.append(gran_premio)
                conexion.commit()
                return grandes_premios

    @classmethod
    def seleccionar_especifico(cls, id):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR_ESPECIFICO, (id,))
                registros = cursor.fetchall()
                grandes_premios = []
                for registro in registros:
                    gran_premio = Gran_premio(registro[1], registro[2], registro[3], registro[0])
                    grandes_premios.append(gran_premio)
                conexion.commit()
                return grandes_premios

    @classmethod
    def insertar(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (gran_premio.nombre, gran_premio.distancia, gran_premio.num_carreras)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'gran premio insertado: {gran_premio}')
                conexion.commit()
                return cursor.rowcount


    @classmethod
    def actualizar(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (gran_premio.nombre, gran_premio.distancia, gran_premio.num_carreras ,gran_premio.id)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'gran premio actualizado: {gran_premio}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def eliminar(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, (gran_premio.id,))
                log.debug(f'gran premio eliminado: {gran_premio}')
                conexion.commit()
                return cursor.rowcount
