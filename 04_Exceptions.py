### Exceptions ###

# Exceptions: when something goes wrong, Python raises an exception. When unhandled,
# they will cause your program to crash. you can handle them using try and except

try: 
    print(0 / 0)
except ZeroDivisionError:
    print('cannot divide by zero')

# Exception handling with try, except, else, and finally:
#     try: This block will test the expected error to occur
#     except: Here you can handle the error
#     else: If there is no exception, then this block will be executed
#     finally: This block always gets executed (regardless of previous steps)


# # Syntax of try blocks

# try: 
#     # some code to attempt

# except:
#     # optional block
#     # handling of exception (if required)

# else:
#     # execute if no exception

# finally:
#     # some code (always executed)

# The following code illustrates an example

def divide(x, y):
    try: 
        result = x // y

    except ZeroDivisionError:
        print('Sorry! You are dividing by zero')

    else:
        print(f'Yeah! Your answer is: {result}')
        
    finally:
        print('This is always executed')

# Example that runs the else block
divide(3, 2)

# Example that runs the except block
divide(3, 0)