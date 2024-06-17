import time
import random
import math


def logger(amount_points: int):
    def decorator(func):
        def wrap(*args, **kwargs):
            print("Running")
            start = time.monotonic()
            result = func(*args, **kwargs)
            end = time.monotonic()
            elapsed_time = end - start
            print(f"Elapsed time: {elapsed_time:.{amount_points}f} seconds")
            return result

        return wrap

    return decorator


@logger(4)
def sin(x):
    time.sleep(random.random())
    return f"x = {x}, sin(x) = {math.sin(x)}"


test = sin(1)
print(test)