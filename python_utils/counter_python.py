'''
Use of counter in python 

Counter from collections provides quick way to count the object in any iterable
Be it string, list or dict 

https://realpython.com/python-counter/

'''

# Creating Counter
from collections import Counter

str1 = "rakshit"
str_counter = Counter(str1)
print(str_counter)
'''
Counter({'r': 1, 'a': 1, 'k': 1, 's': 1, 'h': 1, 'i': 1, 't': 1})
'''

list1 = [1, 2, 1, 1, 3, 4, 2, 2]
list_counter = Counter(list1)
print(list_counter)
'''
Counter({1: 3, 2: 3, 3: 1, 4: 1})
'''

str_list_1 = ["ab", "bc", "cc"]
str_list_counter = Counter(str_list_1)
print(str_list_counter)
'''
Counter({'ab': 1, 'bc': 1, 'cc': 1})
'''

# Accessing element from counter

#using elements()

for value in str_counter.elements():
    print(value, str_counter[value])
'''
r 1
a 1
k 1
s 1
h 1
i 1
t 1
'''

#using items() like dict
for k, v in str_counter.items():
    print(k, v)
'''
r 1
a 1
k 1
s 1
h 1
i 1
t 1
'''

keys = str_counter.keys()
print(keys)
'''
dict_keys(['r', 'a', 'k', 's', 'h', 'i', 't'])
'''

# Updating the Counter with new Elements
'''
Existing counter can be updated by adding new iterable to it
'''

print(str_counter)
'''
Counter({'r': 1, 'a': 1, 'k': 1, 's': 1, 'h': 1, 'i': 1, 't': 1})
'''

str_counter.update("aabbcc")
print(str_counter)
'''
Counter({'a': 3, 'b': 2, 'c': 2, 'r': 1, 'k': 1, 's': 1, 'h': 1, 'i': 1, 't': 1})
'''

# Finding most common element
# elements returned are sorted by count

most_common_all = str_counter.most_common()
print(most_common_all)
'''
[('a', 3), ('b', 2), ('c', 2), ('r', 1), ('k', 1), ('s', 1), ('h', 1), ('i', 1), ('t', 1)]
'''

#finding top N most common
n = 2
most_common_n = str_counter.most_common(n)
print(most_common_n)
'''
[('a', 3), ('b', 2)]
'''

# Finding least common

least_common_all = str_counter.most_common()[::-1]
print(least_common_all)
'''
[('t', 1), ('i', 1), ('h', 1), ('s', 1), ('k', 1), ('r', 1), ('c', 2), ('b', 2), ('a', 3)]
'''

# Finding top N least common
n = 3
# observce n+1 carefully
least_common_n = str_counter.most_common()[:-(n + 1):-1]
print(least_common_n)
'''
[('t', 1), ('i', 1), ('h', 1)]
'''