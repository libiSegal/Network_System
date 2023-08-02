import functools
import logging


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename=r'C:\bootcamp\Network_System\log.txt', level=logging.INFO)
        logging.info(f"Running function {func.__name__}")
        return func(*args, **kwargs)

    return wrapper



