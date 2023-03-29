### Argument Unpacking ###

# Often we'll neet to zip tow or more iterables together. The zip function transforms
# multiple iterables into a single iterable of tuples
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# iterate over the contents of the lists as mapped tuples
[pair for pair in zip(list1, list2)]

# You can also unzip a list
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)          # * performs argument unpacking (returns individual elements)
print(letters)
print(numbers)

# The above implementation is the same as:
letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))

# You can use argument unpacking with any function but it's rarely useful:

def add(a, b): return a + b

print(add(1, 2))

try:
    add([1, 2])
except TypeError:
    print('add expects two inputs')

print(add(*[1, 2]))

### Generalized Parameters ###

# Let's say we want to create a higher-order function that takes as input some function f
# and returns a new function that for any input returns twice the value of f:

def doubler(f):
    # Here we define a new function that keeps a reference to f
    def g(x):
        return 2 * f(x)
    # And return that new function
    return g

# This will work in some cases but doesn't work with functions that take more than a single argument:

def f2(x, y):
    return x + y

g = doubler(f2)
try:
    g(1, 2)
except TypeError:
    print('as defined, g only takes one argument')

# What we need is a way to specify a function that takes arbitrary arguments. 
# When we define a function like this, args is a tuple of its unnamed arguments and
# kwargs is a dict of its named arguments. 

def magic(*args, **kwargs):
    print('unnamed args:', args)
    print('keyword args:', kwargs)
    
magic(1, 2, key='word', key2='word2')

# It works the other way too, if you want to use a list/tuple and dict to supply 
# arguments to a function

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {'z': 3}
assert other_way_magic(*x_y_list, **z_dict) == 6, '1 + 2 + 3 should be 6'

# We'll only use this scheme to produce higher-order functions whose inputs can
# accept arbitrary arguments

def doubler_correct(f):
    '''
    works no matter what kind of inputs f expects
    '''
    def g(*args, **kwargs):
        '''
        whatever arguments g is supplied, pass them through to f
        '''
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
assert g(1, 2) == 6, 'doubler should work now'