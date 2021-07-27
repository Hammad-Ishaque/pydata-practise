class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if 'bar' not in body:
            raise TypeError("Bad user class")
        return super().__new__(cls, name, bases, body)


class Base(metaclass=BaseMeta):
    def foo(self):
        # return "Foo"
        return self.bar()
