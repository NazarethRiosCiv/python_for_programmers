### Object-oriented programming ###

# Python allows you to define classes that encapsulate
# data and the functions that operate on them. We'll use them sometimes to make our
# code cleaner and simpler

# To define a class, you use the class keyword and a PascalCase name. A class contains
# zero or more member functions. By convention, each takes a first parameter, self, that
# refers to the particular class instance

# Normally, a class has a constructor (__init__) that takes whatever parameters you 
# need to construct an instance of your class and does whatever setup you need. Notice
# that the __init__ method name starts and ends with double underscores. These magic
# methods represent special behaviors

class CountingClicker(object):
    '''
    A class can/should have a docstring, just like a function
    '''
    def __init__(self, count=0): # constructor
        self.count = count
        
    def __repr__(self, num_times=1): # produces the string representation of a class instance
        return f'CountingClicker(count={self.count})'
    
    def click(self, num_times=1):
        self.count += num_times
        
    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0

# To instantiate an instance of the class
clicker = CountingClicker()

assert clicker.read() == 0, 'clicker should start with 0'

clicker.click()
clicker.click()

assert clicker.read() == 2, 'after two clicks, clicker should have count 2'

clicker.reset()

assert clicker.read() == 0, 'after reset, clicker should be back to 0'

# We'll occasionally create subclasses that inherit some of their functionality
# from a parent class. 

class NoResetClicker(CountingClicker):
    # This class has all the same methods as CountingClicker

    # Except that it has a reset method that does nothing
    def reset(self):
        pass

