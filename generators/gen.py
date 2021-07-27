from time import sleep


def add(x, y):
    return x + y


class Adder:
    def __init__(self):
        self.z = 0

    def __call__(self, x, y):
        self.z += 1
        return x + y + self.z


add2 = Adder()


def compute():
    rv = []
    for i in range(10):
        sleep(5)
        rv.append(i)
    return rv


class Compute:
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration
        sleep(.5)
        return rv


def compute_gen():
    for i in range(10):
        sleep(.5)
        yield i


# compute_gen()
for val in compute_gen():
    print(val)
