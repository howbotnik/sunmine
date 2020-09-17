import logging
from logging.handlers import RotatingFileHandler

def get_logger():
    print('Creating logger')
    logger = logging.getLogger('sunmine_log')
    logger = set_level(logger)
    fh = get_file_handler('sunmine.log')
    fh = set_file_handler_level(fh)
    logger = add_file_handler_to_logger(fh, logger)
    fh.setFormatter(get_formatter())
    logger = add_file_handler_to_logger(fh, logger)
    return logger

def set_level(logger):
    logger.setLevel(logging.DEBUG)
    return logger

def get_file_handler(log_filename):
    return RotatingFileHandler(log_filename, mode='a', maxBytes=5*1024*1024, backupCount=2, encoding=None, delay=0)

def set_file_handler_level(file_handler):
    file_handler.setLevel(logging.DEBUG)
    return file_handler

def add_file_handler_to_logger(file_handler, logger):
    logger.addHandler(file_handler)
    return logger

def get_formatter():
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return formatter


    # logger.debug('Debug Message')
    # logger.info('Info Message')
    # logger.warning('Warning')
    # logger.error('Error Occured')
    # logger.critical('Critical Error')