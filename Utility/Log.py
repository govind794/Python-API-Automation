'''
DateTime : 06/07/2020 04:20PM
Author   : Govind Patidar
File     : Log.py
'''

import logging
import os
import time

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

logger = logging.getLogger()
level = 'default'


def create_file(filename):
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass


def set_handler(levels):
    if levels == 'error':
        logger.addHandler(Logs.err_hendler)
    logger.addHandler(Logs.hendler)


def remover_handler(levels):
    if levels == 'error':
        logger.removeHandler(Logs.err_hendler)
    logger.removeHandler(Logs.hendler)


def get_current_time():
    return time.strftime(Logs.date, time.localtime(time.time()))


class Logs():
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = path + '/Logs/log.log'
    err_file = path + '/Logs/err.log'
    logger.setLevel(LEVELS.get(level, logging.NOTSET))
    create_file(log_file)
    create_file(err_file)
    date = '%Y-%m-%d %H:%M:%S'

    hendler = logging.FileHandler(log_file, encoding='utf-8')
    err_hendler = logging.FileHandler(err_file, encoding='utf-8')

    @staticmethod
    def debug(log_meg):
        set_handler('debug')
        logger.info(f"[DEBUG {get_current_time()} ] {log_meg}")
        remover_handler('debug')

    @staticmethod
    def info(log_meg):
        set_handler('info')
        logger.info(f"[INFO {get_current_time()} ] {log_meg}")
        remover_handler('info')

    @staticmethod
    def warning(log_meg):
        set_handler('warning')
        logger.info(f"[WARNING {get_current_time()} ] {log_meg}")
        remover_handler('warning')

    @staticmethod
    def error(log_meg):
        set_handler('error')
        logger.info(f"[ERROR {get_current_time()} ] {log_meg}")
        remover_handler('error')

    @staticmethod
    def critical(log_meg):
        set_handler('critical')
        logger.info(f"[CRITICAL {get_current_time()} ] {log_meg}")
        remover_handler('critical')


if __name__ == "__main__":
    Logs.debug("This is debug message")
    Logs.info("This is info message")
    Logs.warning("This is warning message")
    Logs.error("This is error message")
    Logs.critical("This is critical message")
