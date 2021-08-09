from ast import parse

with open('modules.py') as f:
    source = f.read()

ast = parse(source)
print(f'ast = {ast!r}')

code = compile(ast, 'modules.py', mode='exec')
print(f'code = {code!r}')
print(code.co_code)

namespace = {}
exec(code, namespace)
print(f'namespace = {namespace.keys()}')

# construct module
class mod:
    def __init__(self, name, bases, body):
        self.name, self.base = name, bases
        self.__dict__.update(body)

module = mod('module', (), namespace)
print(f'module = {dir(module)!r}')

f = module.f
print(f'f(1,2) = {f()}')