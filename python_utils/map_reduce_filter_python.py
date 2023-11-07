# https://www.analyticsvidhya.com/blog/2021/07/python-most-powerful-functions-map-filter-and-reduce-in-5-minutes/

#lambda functions
# Add 10 to argument a, and return the result
x = lambda a: a + 10
print(x(5))

# Multiply argument a with argument b and return the result:

x = lambda a, b: a * b
print(x(5, 10))

#map function, returns list of elements
# add 3 each element of the list
arr = [1, 2, 3, 4, 5, 6]
func1 = lambda x: x + 3
new_arr = list(map(func1, arr))
print(new_arr)

one_liner_arr = list(map((lambda x: x + 3), arr))
print(one_liner_arr)


#filter function, returns list of elements
def filterFunc(x):
    if x >= 3:
        return x


filter_arr = list(filter(filterFunc, arr))
print(filter_arr)

one_liner_arr = list(filter((lambda x: x >= 3), arr))
print(one_liner_arr)

# reduce function , return single result by applying to every element


def addFunc(a, b):
    return a + b


from functools import reduce

sum_elements = reduce(addFunc, arr)
print("Sum", sum_elements)

one_liner_sum = reduce((lambda a, b: a + b), arr)
print("one liner sun", one_liner_sum)

#flatten the nested list

my_list = [[1], [2, 3], [4, 5, 6, 7]]


#concatenate two lists passed to the function
def func(x, y):
    return x + y


flatten_list = reduce(func, my_list)
print(flatten_list)
flatten_list = reduce((lambda x, y: x + y), my_list)
