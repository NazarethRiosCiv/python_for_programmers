### Strings ###

# Strings can be delimited by single or double quotation marks, but they
# need to match on both ends.
single_quoted_string = 'data science'
double_quoted_string = "data science"

# Python uses backslashes to encode special characters
tab_string = '\t'
print(len(tab_string))

# If you want backslashes as literal backslashes (which you might in Windows
# directories or regular expressions) you can create raw strings
not_tab_string = r'\t'
print(len(not_tab_string))

# You can multiline strings using three quotes on each end of the string
multi_line_string = '''
This is the first line.
and this is the second.
and this is the third.
'''

# A new feature in Python 3.6 is the f-string, which provides a simple way to 
# substitute values into strings.

# For example, suppose we the first and last names of someone
first_name = 'Nazareth'
last_name = 'Rios'

# And then wanted to combine them; there are a few ways of doing so:
full_name1 = first_name + ' ' + last_name # operator overloading
full_name2 = '{} {}'.format(first_name, last_name) # format method
full_name3 = f'{first_name} {last_name}' # f-string
