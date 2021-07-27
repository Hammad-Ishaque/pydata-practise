class Polynomial:
    def __init__(self, *coef):
        self.coef = coef

    def __add__(self, other):
        return Polynomial(*(x + y for x,y in zip(self.coef, other.coef)))

    def __repr__(self):
        return "Polynomial(*{!r})".format(self.coef)

    def __call__(self, *args, **kwargs):
        pass

    def __len__(self):
        return len(self.coef)


p1 = Polynomial(1, 2, 3)
p2 = Polynomial(4, 5, 6)