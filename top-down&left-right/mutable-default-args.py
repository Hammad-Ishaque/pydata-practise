def f(x=[]):
    x.append(len(x))
    return x

print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')

def f(x=None):
    if x is None:
        x = []
    x.append(len(x))
    return x

print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')

def d(f):
    def _(*args, **kwargs):
        return f(*args, **kwargs)
    return _

@d
def f(x=[]):
    x.append(len(x))
    return x

print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')

class A:
    @staticmethod
    def f(x=[]):
        x.append(len(x))
        return x

print(f'f() = {A.f()}')
print(f'f() = {A.f()}')
print(f'f() = {A.f()}')

class A:
    def f(self, x=[]):
        x.append(len(x))
        return x

print(f'f() = {A().f()}')
print(f'f() = {A().f()}')
print(f'f() = {A().f()}')