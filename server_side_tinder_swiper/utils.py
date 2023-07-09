import logging

def log(message, level=logging.INFO):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    if level == logging.INFO:
        logger.info(message)
    elif level == logging.ERROR:
        logger.error(message)

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log(f"Error occurred: {str(e)}", level=logging.ERROR)
    return wrapper

def format_message(message):
    return f"Whats going on or wudup {message}"