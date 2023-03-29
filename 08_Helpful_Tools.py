### Iterables and Generators ###

# Often all we need is to iterate over the collection using for and in. We can
# create generators, which can be iterated over just like lists but generate
# their values lazily on demand

# One way to create generators is with functions and the yield operator:

def generate_range(n):
    i = 0
    while i < n:
        yield i # every call to yield produces a value of the generator
        i += 1

for i in generate_range(10):
    print(f'i:{i}')

# With a generator, you can even create an infinite sequence:

def natural_numbers():
    '''
    returns 1, 2, 3, ...
    '''
    n = 1
    while True:
        yield n
        n += 1

for i in natural_numbers():
    print(f'i:{i}')
    if i == 9:
        break

# A second way to create generators is by using for comprehensions:
evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)

# To grab the next value in the generator:
a = next(evens_below_20)
print(a)

# If you iterate over them now, you'll start with values after a
for i in evens_below_20:
    print(i)

# You can iterate over a sequence's items along with their index:
names = ['Alice', 'Bob', 'Charlie', 'Debbie']

for i, name in enumerate(names):
    print(f'name {i} is {name}')

### Randomness ###

# You can generate random numbers with the random module
import random
random.seed(10)

# Generate a list of random uniform numbers
four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)

# This function will shuffle the elements of a list (in place)
up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten)

# If you need to randomly pick one element from a list, you can use random.choice
my_best_friend = random.choice(['Alice', 'Bob', 'Charlie'])
print(my_best_friend)

# If you need to randomly choose a sample of elements without replacement:
lottery_numbers = [i for i in range(60)]
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)

# To choose a sample of elements with replacement, you can make multiple choice calls
four_with_replacement = [random.choice(lottery_numbers) for _ in range(4)]
print(four_with_replacement)

### Regular Expressions ###

# Regular expressions provide a way of searching through text. One thing to note is that
# re.match checks whether the beginning of a string mathces a regular expression, while
# re.search checks whether any part of a string matches a regular expression
import re

re_examples = [                            #  all of these are True because...
    not re.match('a', 'cat'),              # 'cat' doesn't start with 'a'
    re.search('a', 'cat'),                 # 'cat' has an 'a' in it
    not re.search('c', 'dog'),             # 'dog' doesn't have a 'c' in it
    3 == len(re.split('[ab]', 'carbs')),   #  split on a or b to ['c', 'r', 's']
    'R-D-' == re.sub('[0-9]', '-', 'R2D2') #  replace digits with dashes
]

