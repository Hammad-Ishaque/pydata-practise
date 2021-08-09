"""
Builder is a creational design pattern, which allows constructing complex objects step by step.
- product with full feature
- product with minimal feature
- product with custom feature
Usage examples: The Builder pattern is a well-known pattern in Python world.
 It’s especially useful when you need to create an object with lots of possible configuration options.

Identification: The Builder pattern can be recognized in a class, which has a single creation
 method and several methods to configure the resulting object.
 Builder methods often support chaining (for example, someBuilder.setValueA(1).setValueB(2).create()).
"""
from abc import ABC, abstractmethod
from typing import Any


class Builder:
    """
       The Builder interface specifies methods for creating the different parts of
       the Product objects.
    """

    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def product_part_a(self):
        pass

    @abstractmethod
    def product_part_b(self):
        pass

    @abstractmethod
    def product_part_c(self):
        pass


class ConcreteBuilder(Builder):
    """
        The Concrete Builder classes follow the Builder interface and provide
        specific implementations of the building steps. Your program may have
        several variations of Builders, implemented differently.
    """

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()

    @property
    def product(self):
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add("PartA1")

    def produce_part_b(self):
        self._product.add("PartB1")

    def produce_part_c(self):
        self._product.add("PartC1")


class Product():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_minimal_viable_product(self):
        self.builder.produce_part_a()

    def build_full_featured_product(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = ConcreteBuilder()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
