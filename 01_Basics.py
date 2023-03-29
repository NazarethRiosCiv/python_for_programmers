### Virtual environments ###

# every data science project you do
# will require some combination of external libraries, sometimes
# with specific versions that differ from specific versions you 
# used for other projects. If you were to have a single Python 
# installation, these libraries would conflict and cause you all
# sorts of problems

# The standard solution is to use virtual environments, which are
# sandboxed Python environments that maintain their own versions
# of Python libraries. Anaconda has a built-in mechanism for creating
# virtual environments, but if you use a standard Python installation,
# you can use the built-in venv module or install virtualenv

# To create an Anaconda virtual environment:
# CMD/> conda create -n dsfs python=3.6

# Follow the prompts and you'll have a virtual environment called 'dsfs'
# and will present the following instructions:
# 
# To activiate this environment, use:
# CMD/> conda activate dsfs
# 
# To deactivate and active environment, use:
# CMD/> conda deactivate
#

# As long as this environment is active, any libraries you install will 
# be installed only in the dsfs environment.

### Whitespacing ###

# Python uses indentation to delimit blocks of code

# The pound sign marks the start of a comment
for i in [1, 2, 3, 4, 5]:
    print(i)
    for j in [1, 2, 3, 4, 5]:
        print(j)
        print(i + j)
    print(i)
print('done looping')

# Whitespace is ignored inside parentheses and brackets
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 +
                           11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]

### Modules ###

# Certain features of Python are not loaded by default. These
# include both features that are included as part of the language, as 
# well as third-party features that you download yourself. In order to
# use these features, you'll need to import the modules that contain them

# One approach is to simply import the module itself:
import re
# With this type of import, you must prefix contents with module name
my_regex = re.compile('[0-9]+', re.I)

# If you already had a different object with the same name, use an alias
import re as regex
my_regex = regex.compile('[0-9]+', regex.I)

# You may also want to use an alias when the name length is long
import matplotlib.pyplot as plt

# If you need a few specific values from a module, you can import them explicitly
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

