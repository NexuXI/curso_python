import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../logs/MySQL.log'),
                    log.StreamHandler()
                ])


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
