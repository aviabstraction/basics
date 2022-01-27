# immutable

# Tuple creation

from tkinter import N


my_tuple = ("banana", "apple", "grape")
print(my_tuple, "my_tuple")

my_tuple2 = ("banana", "apple", "grape")
print(my_tuple2, "my_tuple2")

my_tuple3 = ("banana",)
print(type(my_tuple3), "tuple with one element")

my_tuple4 = tuple([1, 2, 3, 4])
print(my_tuple4, "tuple builtin")

# Accessing tuple elements
print(my_tuple[0], 'first_idx')

# count
my_tuple5 = ("a", "b", "c", "d", "e")
print(my_tuple5.count("a"), "count")

# index
print(my_tuple5.index("d"), "first occurence in idx")

# convert list to tuple & vice versa
my_list = list(my_tuple5)
print(my_list, "tuple2list")

my_tuple6 = tuple(my_list)
print(my_tuple6, "list2tuple")

# loops,if else, slice are same as list for tuples

dfdf
# unpack
a1, a2, a3 = my_tuple
print(a1, "unpack")
print(a2, "unpack")
print(a3, "unpack")

a1, *a2, a3 = my_tuple5
print(a2, "unpack as list")
