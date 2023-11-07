def simple_decorator(func):
    def inner_func(a, b):

        print("I am decorating a and b", a, b)
        return func(a, b)

    return inner_func


def addFunc(a, b):
    print("Simple function")
    return a + b


# this adds decorator by default to the function
@simple_decorator
def addFuncMore(a, b):
    print("In the function")
    return a + b


def all_decorator(func):
    def inner(*args, **kwargs):
        print("I can decorate any functions")
        return func(*args, **kwargs)

    return inner


@all_decorator
def func1():
    print("func1")


@all_decorator
def func2(a):
    print("funct 2: ", a)


@all_decorator
def func3(a, b):
    print("func3 ", a, b)


a = 1
b = 5

print(addFunc(a, b))

decorated_addFunc = simple_decorator(addFunc)
print(decorated_addFunc(a, b))

auto_decorator_addFunc = addFuncMore
print(auto_decorator_addFunc(a, b))

print(func1())
#positonal args
print(func2(a))
#keyword args
print(func3(a=1, b=2))
