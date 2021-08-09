print(f'locals() = {locals().keys()}')
print(f'globals() = {globals().keys()}')
print(f'locals() is globals() = {locals() is globals()}')

# old = locals()
# x = 10
# print(f'locals()-old = {set(locals()) - set(old)}')

old = locals().copy()
y = 10
print(f'locals()-old = {set(locals()) - set(old)}')

locals()['z'] = 10
print(f'z = {z}')


def f(x):
    print(f'x = {x}')


f(10)


def f(x=10):
    locals()['x'] = 100
    print(f'x = {x}')

f()

# def f():
#     locals()['x'] = 10
#     print(f'x = {x}')
#
#
# f()

def f():
    globals()['x'] = 100
    print(f'x = {x}')


f()

def f(x=10):
    def f():
        locals()['x'] = 1
        globals()['x'] = 100
        print(f'x = {x}')
    f()
f()

def f(x=10):
    def f():
        nonlocal x
        x += 1
        print(f'x = {x}')

    f()
f()


# What are non executable statements
# global
# nonlocal
# pass

# The def and class are part of executable code and the body is just into byte object