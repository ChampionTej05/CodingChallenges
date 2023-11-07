import enum


class Life_Status(enum.Enum):
    Alive = 0
    Dead = 1


'''
class Dog:

    # Common Class attribute
    species = "Dog Species"
    
    # We can not have more than one constructor methods in python
    # There is overloading of methods in python
    

    # def __init__(self):

    #     self.name = "No Name"
    #     self.status = Life_Status.Dead

    def __init__(self, name):
        self.name = name
        self.status = Life_Status.Alive

    def __str__(self):
        #.name gives the value of ENUM
        life_status_value = self.status.name
        return "{name} is {status}".format(name=self.name,
                                           status=life_status_value)

    def get_dog_name(self):
        return self.name


dog1 = Dog(name="Rakshit")
dog2 = Dog()
print(dog1)
print(dog2)
'''

#Inheritance in Python

# we can override the existing functionality or we can extend the functionality of the parent class


#parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #default behaviour of the met
    def speak(self, sound="Grr"):
        print('{name} speaks {sound}'.format(name=self.name, sound=sound))
        return


#Inherits Animal
class Dog(Animal):
    # overrides the functionality of the parent class
    def speak(self):
        sound = "Bow Bow"
        print('{name} barks {sound}'.format(name=self.name, sound=sound))


class Cat(Animal):
    #extending the attribute of the class
    def __init__(self, name, age, breed):
        self.breed = breed
        super().__init__(name, age)

    #extends the functionality of the parent class
    def speak(self):
        return super().speak(sound="Meow")

    def __str__(self):
        return "{name} has breed = {breed}".format(name=self.name,
                                                   breed=self.breed)


from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price

    #this is used to mark the method as abstractmethod
    @abstractmethod
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


# we have deliberately missed out on implementation of __repr__ to check if the error is thrown or not
class Novel(Book):

    # class level hidden variable
    __hidden_var = 10

    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

        #adding one private variable here
        self.__privateValue = "NovelPrivateValue"

    #comment this to see the error for abstract method
    def __repr__(self):
        return f"Book: {self.title} is Novel"

    def get_private_value(self):
        return self.__privateValue


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return f"Book: {self.title}, Branch: {self.branch}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


#using multi level inheritance
class Fiction(Novel):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price, pages)
        #should throw error, as trying to access private member of the class
        print(self.__privateValue)
        '''
        File "oop_basics.py", line 185, in <module>
        fiction1 = Fiction('Two States', 20, 'Chetan Bhagat', 200, 187)
         File "oop_basics.py", line 140, in __init__
        print(self.__privateValue)
        AttributeError: 'Fiction' object has no attribute '_Fiction__privateValue'
        '''

        #should not throw error
        print(self.get_private_value())


# name = "Rakshit"
# age = 24
# animal1 = Animal(name, age)
# animal1.speak()

# dog1 = Dog(name, age)
# dog1.speak()

# is_dog_instance_of_animal = isinstance(dog1, Animal)
# is_dog_instance_of_dog = isinstance(dog1, Dog)
# is_animal_instance_of_animal = isinstance(animal1, Animal)
# is_animal_instance_of_dog = isinstance(animal1, Dog)

# print(is_dog_instance_of_animal)
# print(is_dog_instance_of_dog)
# print(is_animal_instance_of_animal)
# print(is_animal_instance_of_dog)

# cat1 = Cat(name, age, breed="Cat1")
# cat1.speak()
# print(cat1)

# #developer friendly representatio is given by repr
# print(repr(cat1))

# print(issubclass(Dog, Animal))  #true
# print(issubclass(Animal, Dog))  #false

novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')

# print(novel1)
# print(academic1)
'''
Traceback (most recent call last):
  File "oop_basics.py", line 150, in <module>
    novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
TypeError: Can't instantiate abstract class Novel with abstract methods __repr__
'''

#throws error as trying to access private variables
# fiction1 = Fiction('Two States', 20, 'Chetan Bhagat', 200, 187)

# can't access private value to class
# print(novel1.__privateValue)
'''
Traceback (most recent call last):
  File "oop_basics.py", line 195, in <module>
    print(novel1.__privateValue)
AttributeError: 'Novel' object has no attribute '__privateValue'
'''
# only class level hidden variable can be accessed like this
print(novel1._Novel__hidden_var)