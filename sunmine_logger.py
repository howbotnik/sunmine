import logging
from logging.handlers import RotatingFileHandler

def get_logger():
    print('Creating logger')
    logger = logging.getLogger('sunmine_log')
    logger.setLevel(logging.DEBUG)
    fh = RotatingFileHandler('sunmine.log', mode='a', maxBytes=5*1024*1024, backupCount=2, encoding=None, delay=0)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

    # logger.debug('Debug Message')
    # logger.info('Info Message')
    # logger.warning('Warning')
    # logger.error('Error Occured')
    # logger.critical('Critical Error')