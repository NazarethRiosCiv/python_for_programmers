### Exceptions ###

# Exceptions: when something goes wrong, Python raises an exception. When unhandled,
# they will cause your program to crash. you can handle them using try and except
try: 
    print(0 / 0)
except ZeroDivisionError:
    print('cannot divide by zero')