
# lambda with two args

multiplier = lambda x,y: x*y

print(multiplier(5,4), "multiplier_lambda")

# lambda with higher order functions

list_with_tuples = [(1,2),(3,-1),(5,6),(7,9)]

sort_by_wish = sorted(list_with_tuples, key = lambda x:x[1])

print(sort_by_wish,"sorted_lamba")

list_values = [1,2,3,4,5]

mapped_values = map(lambda x:x*2,list_values)

print(list(mapped_values),"mapping_lambda")

filter_values = filter(lambda  x:x<2,list_values)

print(list(filter_values),"filter_lambda")

# reduce_values = reduce(lambda x,y:x+y,list_values)


# print(reduce_values,"reduce_lambda")