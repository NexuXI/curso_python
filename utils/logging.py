import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)')


def genera_mensaje(mensajes):
    reply = ""
    for mensaje in mensajes:
        reply += str(mensaje)
    return reply


def debug(*message):
    log.debug(genera_mensaje(message))


def info(*message):
    log.info(message)


def warn(*message):
    log.warning(message)


def error(*message):
    log.error(message)


def critical(*message):
    log.critical(message)


info("name:", __name__)
if __name__ == '__main__':
    debug('Mensaje a nivel debug')
    log.info('mensaje a nivel info')
    log.warning('Mensaje a nivel de warning')
    log.error('mensaje a nivel de error')
    log.critical('mensaje a nivel de critical')
