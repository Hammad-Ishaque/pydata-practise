from library import Base

assert hasattr(Base, "foo")


class Derived(Base):

    def bar(self):
        # return self.foo()
        return "bar"


# d1 = Derived()
# print(d1.bar())
