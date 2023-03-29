# From a previous script:
from collections import defaultdict
document = 'Mary had a little lamb'
word_counts = defaultdict(int)     # int() produces 0 by default
for word in document:
    word_counts[word] += 1

### Control Flow ###

# Like in many languages, you can perform conditions and loops:
if 1 > 2:
    message = 'if only 1 were greater than two...'
elif 1 > 3:
    message = 'elif stands for else if'
else:
    message = 'when all else fails, use else (if you want to)'

# You can also write a ternary if-then-else on one line
x = 2
parity = 'even' if x % 2 == 0 else 'odd'

# To perform a while loop
x = 0
while x < 10:
    print(f'{x} is less than 10')
    x += 1

# To perform a for loop
for x in range(10):
    print(f'{x} is less than 10')

# If you need more complex logic, you can use coninue and break
for x in range(10):
    if x == 3:
        continue
    elif x == 5:
        break
    print(x)

### Booleans ###

# Booleans in Python work as in most other languages
print(1 < 2)
print(True == False)

# Python used the value None to indicate a nonexistent value. It is
# similar to other languages' null
x = None
assert x == None, 'this is the non-Pythonic way to check for None'
assert x is None, 'this is the Pythonic way to check for None'

# Python lets you use any value where it expects a Boolean. The following
# are all 'False'
'hello' if False else 'world'
'hello' if None else 'world'
'hello' if [] else 'world'
'hello' if {} else 'world'
'hello' if '' else 'world'
'hello' if set() else 'world'
'hello' if 0 else 'world'
'hello' if 0.0 else 'world'

# Pretty much anything else gets treated as True. This allows you to easily
# use if statements to test for empty lists, empty strings, empty dictionaries, etc.

# Python has an all function, which takes an iterable and returns True precisely 
# when every element is true, and an any function, which returns True when 
# at least one element is true
all([True, 1, {3}])   # True
all([True, 1, {}])    # False
any([True, 1, {}])    # True
all([])               # True
any([])               # False

### Sorting ###

# Every list has a sort method that sorts it in place. You can also
# use a sort function instead to return a new list

x = [4, 1, 2, 3]

y = sorted(x)
print(y)

x.sort()
print(x)

# If you want elements sorted from largest to smallest, you can specify a reverse=True
# parameter. You can also compare the results of a function that you specify with a key.
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)
print(x)

wc = sorted(word_counts.items(), key=lambda word_count: word_count[1], reverse=True)
print(wc)

### List Comprehensions ###

# Frequently, you'll want to transform a list into another list by choosing only certain
# elements, by transforming elements, or both. This can be done with list comprehensions

even_numbers = [x for x in range(5) if x % 2 == 0]
squares = [x * x for x in range(5)]
even_squares = [x * x for x in even_numbers]

# You can similarly turn lists into dictionaries or sets
square_dict = {x: x * x for x in range(5)}
square_set = {x: x * x for x in range(5)}

# A list comprehension can include multiple for loops:
pairs = [(x, y)
         for x in range(10)
         for y in range(10)]

# And the later for loops can use the results of earlier ones:
increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x + 1, 10)]

### Assert Statements ###

# Assert statements cause your code to raise an AssertionError if your specified
# condition is not true. they're commonly used to check that our code is correct

# No message is displayed if error is raised
assert 1 + 1 == 2

# Message is displayed if error is raised
assert 1 + 1 == 2, '1 + 3 = 4 but didn\'t'

