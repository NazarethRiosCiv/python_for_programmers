### Lists ###

# Probably the most fundamental data structure in Python is the list, which is simply
# an ordered collection (similar to an array in other languages)
integer_list = [1, 2, 3]
heterogeneous_list = ['string', 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

list_length = len(integer_list)
list_sum = sum(integer_list)

# You can get or set the nth element of a list with square brackets:
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
zero = x[0]    # lists are zero-indexed
one = x[1]
nine = x[-1]   # Pythonic for last element
eight = x[-2]  # Pythonic for next-to-last element
x[0] = -1      # reassign the first element to another value

# You can also use square brackets to slice lists. The i:j slice means all elements
# from i (inclusive) to j (non-inclusive)
first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

# A slice can take a third argument to indicate its stride, which can be negative
every_third = x[::3]
five_to_three = x[5:2:-1]

# Python has an in operator to check for membership.
# The in operator involves examining the elements of the list one at a time, which
# means that you probably shouldn't use it unless you know your list is pretty small
# (or if you don't care how long it takes to check membership)
print(1 in [1, 2, 3])
print(0 in [1, 2, 3])

# You can also concatenate lists together
x = [1, 2, 3]
x = x + [4, 5, 6]       # operator overloading (not necessarily in-place)
x.extend([4, 5, 6])     # extend method (in-place)

# More frequently, we will append to lists one item at a time
x = [1, 2, 3]
x.append(0)
print(x[-1])
print(len(x))

# It's often convenient to unpack lists when you know how many elements they contain
x, y = [1, 2]
# And a common idiom is to use an underscore for a value you're going to throw away
_, y = [1, 2]

### Tuples ###

# Tuples are lists' immutable cousins. Pretty much anything you can do to a list
# that doesn't involve modifying it, you can do to a tuple. You specify a tuple by
# using parentheses (or nothing) instead of square brackets
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4

# Tuples are a convenient way to return multiple values from functions:

def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2, 3)
s, p = sum_and_product(5, 10)

# Tuples can also be used for multiple assignment
x, y = 1, 2    # Assign values on a single line
x, y = y, x    # Pythonic way to swap variables

### Dictionaries ###

# Another fundamental data structure is a dictionary, which associates values
# and keys and allows you to quickly retrieve the value corresponding to a given key
empty_dict = {}                     # Pythonic
empty_dict2 = dict()                # less Pythonic
grades = {'Joel': 80, 'Tim': 95}    # dictonary literal

# You can look up the value for a key using square brackets
joels_grade = grades['Joel']

# You can check for the existence of a key (fast for dictionaries, as opposed to lists)
print('Joel' in grades)
print('Kate' in grades)

# Dictionaries have a get method that returns a default value (instead of raising
# an exception) when you look up a key that's not in the dictionary
print(grades.get('Joel', 0))
print(grades.get('Kate', 0))
print(grades.get('No one'))     # default is None

# You can assign key/value pairs using square brackets
grades['Tim'] = 99
grades['Kim'] = 100
num_students = len(grades)

# You can use dictionaries to represent structured data:
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

# Besides for looking for specific keys, we can look at all of them:
tweet_keys = tweet.keys()      # iterable for the keys
tweet_values = tweet.values()  # iterable for the values
tweet_items = tweet.items()    # iterable for the (key, value) tuples

print('user' in tweet_keys)       # non-Pythonic way of checking for keys (slow)
print('user' in tweet)            # Pythonic way of checking for keys (fast)
print('joelgrus' in tweet_values) # only way to check value (but is slow)

### DefaultDicts ###

# Imagine you're counting the words in a document. An obvious approach is to 
# create a dictionary in which the keys are words and the values are counts.

document = 'Mary had a little lamb'

# Method 1: as you check each word, you can increment its count if it's already
# in the dictionary and add it to the dictionary if it's not
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Method 2: you could also use the forgiveness is better that permission approach
# and handle the exception from trying to look up a missing key
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

# Method 3: use get, which behaves gracefully for missing keys:
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

# Each of these are slightly unwieldly, which is why defaultdict is useful.
# A defaultdict is like a regular dictionary, except that when you try to
# look up a key it doesn't contain, it first adds a value for it using a 
# zero-argument function you provided when you created it

from collections import defaultdict

word_counts = defaultdict(int)     # int() produces 0 by default
for word in document:
    word_counts[word] += 1

print(word_counts)

# defaultdict can also be used with list or dict, or even your own functions
dd_list = defaultdict(list)           # list() produces an empty list
dd_list[2].append(1)                  # now dd_list contains {2: [1]}

dd_dict = defaultdict(dict)           # dict() produces an empty dict
dd_dict['Joel']['City'] = 'Seattle'   # {'Joel': {'City': 'Seattle'}

dd_pair = defaultdict(lambda: [0, 0]) # now dd_pair contains {2: [0, 1]}
dd_pair[2][1] = 1

# defaultdicts will be useful when we're using dictionaries to collect results
# by some key and don't want to have to check every time to see if the key exists yet

### Counters ###

# A Counter turns a sequence of values into a defaultdict(int)-like object mapping
# keys to their counts in the sequence

from collections import Counter
c = Counter([0, 1, 2, 0])

print(c)

# This gives us a very simple way to solve our word_counts problem
word_counts = Counter(document)

print(word_counts)

# A counter instance has a most_common method that is frequently useful
for word, count in word_counts.most_common(10):
    print(word, count)

### Sets ###

# Another useful data structure is set, which represents a collection of distinct elements
primes_below_10 = {2, 3, 5, 7}     # creating a set with initial elements
s = set()                          # to initialize an empty set
s.add(1)
s.add(2)
s.add(2)
print(len(s))

# We'll use sets for two main reasons. The first is that 'in' is a very fast operation
# on sets. The second reason is to find the distinct items in a collection

# To check membership in a list (slow)
stopwords_list = ['a', 'an', 'at', 'yet', 'you']
'zip' in stopwords_list

# To check membership in a set (fast)
stopwords_set = set(stopwords_list)
'zip' in stopwords_set

# To gather distinct items in a collection
item_list = [1, 2, 3, 1, 2, 3]
print(len(item_list))
item_set = set(item_list)
print(len(item_set))
