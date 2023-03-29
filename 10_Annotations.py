### Type Annotations ###

# Python is a dynamically typed language. That means that in general it doesn't
# care about the types of objects we use, as long as we use them in valid ways
x = 5
y = 'some string'
z = True

# In a statically typed language our functions and objects would have specific types
def add(a: int, b: int) -> int:
    return a + b

# Having to think about the types in your code forces you to design cleaner 
# functions and interfaces
from typing import Union

def ugly_function(value: int, operation: Union[str, int, float, bool]) -> int:
    # Here we have a function whose 'operation' parameter is allowed to be 
    # a string, an int, a float, or a bool
    pass

## How to Write Type Annotations ##

# For built-in types like int, bool, and float, you just use the type itself:
def some_function(a: int, b: float, c: bool) -> float:
    return None

# The typing module provides a number of parameterized types that we can use
from typing import List

def total(xs: List[float]) -> float:
    return sum(total)

# You can also annotate variables
x: int = 5

from typing import Optional
values: List[int] = []
best_so_far: Optional[float] = None  # allowed to be either a float or None

# The type annotations in this snippet are all unnecessary
from typing import Dict, Iterable, Tuple

# Keys are strings, values are ints
counts: Dict[str, int] = {'data': 1, 'science': 2}
    
lazy = True
    
# Lists and generators are both iterables
if lazy:
    evens: Iterable[int] = (x for x in range(10) if x % 2 == 0)
        
else: 
    evens = [x for x in range(10) if x % 2 == 0]
    
# Tuples specify a type for each element
triple: Tuple[int, float, int] = (10, 2.3, 5)

# Since Python has first-class functions, we need a type to represent those as well
from typing import Callable

# The type hint says that repeater is a function that takes two arguments
# (a string and an int) and returns a string
def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

# As type annotations are just Python objects, we can assign them to variables
Number = int
Numbers = List[Number]

def total(xs: Numbers) -> Number:
    return sum(xs)