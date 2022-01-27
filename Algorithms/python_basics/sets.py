# Creation of set

my_set = {"hello", "name", 1, "2", "2" }
print(my_set, "my_set")


my_set2 = set()
print(my_set2, "my_set2")

# Accessing set element
# print(my_set["1"], "second_elem_set")

# Adding to set
my_set.add(4)
print(my_set, "add")

# removing in set
my_set.pop()
print(my_set, "pop")

my_set.remove('hello')
print(my_set, "remove")

my_set.discard(1)
print(my_set, "discard")

# list and dict to set and vice vera

my_list = set([1, 2, 3, 4, 4])
print(my_list, "list2set")

my_dict = set({"name": "Avnash","age": 12})
print((my_dict, "dict2set"))

# copy is same as list and dict

#looping through set

for value in my_set:
    print(value, "loop_set")


#union,intersection,diff,symmetric diff
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

union = odds.union(evens)
print(union, "union")

intersect = odds.intersection(primes)
print(intersect, "interset")

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setB.difference(setA)
print(diff, "difference")

sym_diff = setA.symmetric_difference(setB)
print(sym_diff, "symmetic_difference")

#subsets and disjoints
setC = {1, 2, 3, 4, 5, 6, 7}
setD = {1, 2, 3}

print(setD.issubset(setC), "is_subset")
print(setC.issuperset(setD), "is_superset")
print(setC.isdisjoint(setD), "is_disjoint")

# frozen set

froze = frozenset((1, 2, 3))
print(froze, "frozen_set")