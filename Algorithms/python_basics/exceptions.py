# try and except block


try:
    test_func = lambda x: x/0
    print(test_func(5), "try_block")
except Exception as e:
    print(e)


# finally and else

try:
    test_func = lambda x: x/0
    print(test_func(5), "try_block")
except ZeroDivisionError as e:
    print(e)
else:
    print("passed all excepts")
finally:
    print("dont see excepts and else block, just print or do something")

# raise your own exceptions


class ValueTooLowError(Exception):
    def __int__(self,message,value):
        self.message = message
        self.value = value

def test_value(x):
    if x<0:
        raise ValueTooLowError("value too low",x)


try:
    test_value(-1)
except ValueTooLowError as e:
    print(e)


# assert

test = -1
assert (test<1), "less value"