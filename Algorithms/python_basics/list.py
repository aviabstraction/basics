# mutable


# list creation 1
my_list = [1, 2, 3, 4]
print(my_list, "my_list")

# list creation 2
new_list = list()
print(new_list, "new_list")

# Accessing list elements
print(my_list[1], "second_idx")

# Accessing last element
print(my_list[-1], "last_idx")
print(my_list[-2], "second_last_idx")

# Iterating through list
for item in my_list:
    print(item, "item")

# check element is in list
if 2 in my_list:
    print("yes, element exist")

# Length of list
print(len(my_list), "length")

# Adding to List
my_list.append(5)
print(my_list, "append")

# Adding at specific index
my_list.insert(2, "odd one")
print(my_list, "insert")

# pop item in list
removed_item = my_list.pop()
print(removed_item, "pop")

# Remove item in list
my_list.remove("odd one")
print(my_list, "remove")

# Clear list
# my_list.clear()
print(my_list, "clear")

my_list.reverse()
print(my_list, 'reverse')

# my_list.sort()
print(my_list, "inplace sort")

new_sorted = sorted(my_list)
print(new_sorted, "!inplace sort")
print(my_list, "input list")

# new list with same element
my_list2 = [5] * 5
print(my_list2, "same elems repeated")

# concate two list
concat_list = my_list + my_list2
print(concat_list, "concate")

# slice list
print(my_list[0:2], "slice")
print(my_list[:2], "slice with no start idx")
print(my_list[1:], "slice with no stop idx")
print(my_list[::2], "step idx at two level")

# copy list

copied_list1 = my_list.copy()
print(copied_list1, "copied_list1")

copied_list2 = list(my_list)
print(copied_list2, "copied_list2")

copied_list3 = my_list[:]
print(copied_list3, "copied_list3")

# list comprehension
squared_list = [item*item for item in my_list if item == 4]
print(squared_list, "list_comprehension")