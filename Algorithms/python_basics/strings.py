from timeit import default_timer as timer
# Initiation of strings

str1 = "Hello world"
print(str1, "str1")

str2 = 'Sample text'
print(str2, "str2")


# Accessing string
print(str1[0], "first_idx_inplace")


# Looping strings
for char in str1:
    print(char, "loop_str")

# Slicing strings
str1 = str1[1:2]
print(str1, "sliced_string")
str3 = "Sample"
str3 = str3[::-1]
print(str3, "reverse_string")


#replace

str4 = "hello Avinash"
str4 = str4.replace("Avinash", "Dinesh")
print(str4, "replace")

#find and count

str5 = "my text"
str5 = str5.find("text")
print(str5, "find_index")

str6 = "abcdddfdefdf"
str6 = str6.count("d")
print(str6, 'str6')

# timer

start = timer()

reverse_char = "reverse"

for char in reverse_char[::-1]:
    reverse_char += char

stop = timer()


print(reverse_char, "reverse_time1")
print(stop-start, "time_taken")


#formatting string

sample1 = '''Hello
hei
hi'''

print(sample1, "multi liner")

put_this = "avi"

print_this1 = "hello %s welcome" % put_this

print(print_this1, "percent_formatter")


put_this1 = "hey"

print("hello {} {}".format(put_this1, put_this1), "string_format")

my_string = f'this variable is {put_this}'

print(my_string, "-f string")

#convert string to list and list to string

sample2 = "hello"
sample2 = sample2.split("")

print(sample2, "split")

sample2 = "".join(sample2)

print(sample2, "join")