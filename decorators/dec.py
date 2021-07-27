from time import time


def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('elapsed', after - before)
        return rv

    return f


def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print('running {.__name__}'.format(f))
                rv = f(*args, **kwargs)
            return rv
        return wrapper
    return inner


@timer
def add(x, y=10):
    return x + y


@timer
def sub(x, y=10):
    return x - y


print('add(10)', add(10))
print('sub(10)', sub(10))