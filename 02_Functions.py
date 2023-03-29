### Functions ###

# A function is a rule for taking any number of inputs and returning a corresponding output

def double(x):
    '''
    This is where you put an optional docstring that explains what the 
    function does. For example, this function multiplies its input by 2.
    '''
    return x * 2

# Python functions are first-class objects, which means that we can assign them to
# variables and pass them into functions just like any other arguments

def apply_to_one(function):
    '''
    Calls the function with 1 as its argmuent
    '''
    return function(1)

my_double = double
x = apply_to_one(my_double)
print(x)

# It is also easy to create short anonymous functions, or lambdas:
y = apply_to_one(lambda x: x + 4)

print(y)

# Function parameters can also be given default arguments, which only need
# to be specified when you want a value other than the default

def my_print(message='my default message'):
    print(message)

my_print('hello')

my_print()
