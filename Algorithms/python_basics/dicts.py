# Dictionary creation
my_dict = {"name": "Avinash", "age": 29, "gender": "Male"}
print(my_dict, "my_dict")

my_dict2 = dict(name="prakash", age=50)
print(my_dict2, 'my_dict2')

# Accessing dict keys

print(my_dict['name'])

# Adding prop to dict

my_dict["hobby"] = "Cricket"
print(my_dict, "added_prop")


# Deleting prop in dict
my_dict.pop("hobby")
print(my_dict, "pop_dict")
my_dict.popitem()
print(my_dict, "pop_item")
del my_dict2["name"]
print(my_dict2, "del_prop")

# Updating dict

my_dict.update(my_dict2)
print(my_dict, "update_dict")

# Copy dicts

copied_dict1 = my_dict.copy()
print(copied_dict1, "copied_dict1")
copied_dict2 = dict(my_dict)
print(copied_dict2, "copied_dict2")


# Looping through dicts

for key, value in my_dict.items():
    print(key, "key_loop")
    print(value, "value_loop")

for key in my_dict.keys():
    print(key, "only_key")

for value in my_dict.values():
    print(value, "only_value")

# Number and Tuple as keys in dic

my_dict3 = {1: 3, 2: 4, 5: 7}
print(my_dict3, "number_key_dict")
print(my_dict3[5], "accessing_number_key_dict")

my_tuple = 1, "name", False, 2
print(dict(my_tuple=list()))

# Handling condition in dicts

if "name" in my_dict:
    print("yes, found - by condition")

# try and except

try:
    my_dict["name"]
    print("random prop found - try block")
except:
    print("oops not found - except_block")

