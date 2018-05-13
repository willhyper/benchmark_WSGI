import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        resp = func(*args, **kwargs)

        elasped_sec = time.time() - start

        print(elasped_sec)

        return resp

    return wrapper
