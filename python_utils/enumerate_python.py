'''
Enumerate helps to add counter of iterations for iterator similar to Counter.
Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.

It is used to get index and values in one shot for list 

https://www.geeksforgeeks.org/enumerate-in-python/
 
'''

list1 = ["r", "a", "b", "a", "m", "b", "b"]
enum1 = enumerate(list1)
print(enum1)
'''
<enumerate object at 0x7f84d807fd40>
'''
print(list(enum1))
'''
[(0, 'r'), (1, 'a'), (2, 'b'), (3, 'a'), (4, 'm'), (5, 'b'), (6, 'b')]
'''

# we can also change the starting index depending on our use case
enum2 = enumerate(list1, 3)
print(list(enum2))
'''
[(3, 'r'), (4, 'a'), (5, 'b'), (6, 'a'), (7, 'm'), (8, 'b'), (9, 'b')]
'''

# Accessing elements
enum1 = enumerate(list1)
for idx, v in enum1:
    print(idx, v)
'''
0 r
1 a
2 b
3 a
4 m
5 b
6 b
'''