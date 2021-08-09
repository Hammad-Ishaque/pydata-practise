from modules import f

from modules import g
from modules import h

from modules import A
a = A()
print(f'isInstance(a,A) = {isinstance(a,A)}')

import modules
b = modules.B()
print(f'isInstance(b,B) = {isinstance(b, modules.B)}')

from importlib import reload
import modules
modules = reload(modules)

print(f'isinstance(a, A) = {isinstance(a,A)}')
print(f'isinstance(b,B) = {isinstance(b,modules.B)}')

from modules import A, B
print(f'isinstance(a, A) = {isinstance(a,A)}')
print(f'isinstance(b,B) = {isinstance(b,B)}')