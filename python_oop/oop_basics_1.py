# define interface in python

import abc
from abc import ABC, abstractmethod


class AbstractFactory(metaclass=abc.ABCMeta):
    """
    By default becomes the interface
    """
    def create_product_a(self):
        """no implementation class
        """

    def create_product_b(self):
        """no implementation class
        """


class ConcreteFactory(AbstractFactory):
    """This makes the class as Abstract class since it has abstract method defined

    Args:
        AbstractFactory (_type_): Parent Interface
    """
    @property
    @abstractmethod
    def product_name(self):
        """this is abstract property of the class
        """

    def create_product_a(self):
        print("Creating product A")

    @abstractmethod
    def create_product_b(self):
        """_summary_
        """


class ImplementationClass(ConcreteFactory):
    def create_product_b(self):
        print("Creating product B")

    @property
    def product_name(self):
        return "Product Name is A"


def example_interface():
    obj = ImplementationClass()
    obj.create_product_a()
    obj.create_product_b()

    print(obj.product_name)


class Parent():
    def __init__(self):
        self.public_value = 0
        self.__private_value = 100

    def get_private_value(self):
        return self.__private_value

    def set_private_value(self, value):
        self.__private_value = value


def example_encapsulation():
    obj = Parent()

    print("Public ", obj.public_value)
    #AttributeError: 'Parent' object has no attribute '__private_value'
    # print("Private Value access: ", obj.__private_value)
    #set private value
    obj.__private_value = 121
    print("Print value :", obj.__private_value
          )  # it will show 121 but actual object value would not be changed
    print("Using Get", obj.get_private_value())  # this will show still 100
    print("Using Set: ",
          obj.set_private_value(123))  # this will make it 123 in instance


example_encapsulation()