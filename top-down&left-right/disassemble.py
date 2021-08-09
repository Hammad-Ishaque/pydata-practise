from dis import dis

def f():
    pass
# dis(f)
#
def f(x, y):
    return x + y
# dis(f)

class A:
    pass
# dis(A)

def _():
    class A:
        pass
# dis(_)

def _():
    def f():
        pass

# dis(_)

import modules
dis(modules)