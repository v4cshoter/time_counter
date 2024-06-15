import time
import random
import math


def logger(*args, **kwargs):
    def decorator(func):
        def wrap(*args, **kwargs):
            print("Running")
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            elapsed_time = end - start
            print(f"Started at {time.strftime('%X', time.localtime(start))} \n"
                  f"Ended at {time.strftime('%X', time.localtime(end))} \n"
                  f"Elapsed time: {elapsed_time:.4f} seconds")
            return result

        return wrap

    return decorator


@logger(2)
def sin(x):
    time.sleep(random.randint(1, 3))
    return f"x = {x}, sin(x) = {math.sin(x)}"


test = sin(1)
print(test)
