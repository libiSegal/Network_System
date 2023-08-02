import functools
import logging


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='log.txt', level=logging.INFO)
        logging.info(f"Running function {func.__name__}")
        print("in log")
        return func(*args, **kwargs)

    return wrapper
