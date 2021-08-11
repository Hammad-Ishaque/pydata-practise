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

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # f()
        print_time(self.name, 5, self.counter)
        print("Exiting " + self.name)


exitFlag = 0


def print_time(threadName, counter, delay):
    while counter:
        f()
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
