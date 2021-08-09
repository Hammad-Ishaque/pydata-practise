class A:
    pass

class A:
    def __init__(self, b):
        self._b = b

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if value < 0:
            raise ValueError("must be possitive")
        self._b = value


if __name__ == '__main__':
    a = A(10)
    print(f'a.b = {a.b}')
    a.b = -100
    print(f'a.b = {a.b}')