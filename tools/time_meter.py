from functools import wraps
from timeit import timeit


def time_meter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        start = timeit()
        k = func(*args, **kwargs)
        print((timeit() - start))
        return k

    return wrapper
