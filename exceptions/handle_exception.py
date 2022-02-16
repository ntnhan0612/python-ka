def sum(a, b):
    return a / b

# syntax
try:
    print(sum(6, 0))
except ZeroDivisionError:
    print('Error occused here')
finally:
    print('This is finally')

# list of python built-in exceptions
# https://docs.python.org/3/library/exceptions.html