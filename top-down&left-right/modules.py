def f():
    print('called f')
    return 1


def g():
    print('called g')


print(f'defined f = {f!r}')
print(f'defined g = {g!r}')

h = f
print(f'defined h = {h!r}')


class A:
    pass


class B:
    pass
