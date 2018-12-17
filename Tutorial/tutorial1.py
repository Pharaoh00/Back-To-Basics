#!/usr/bin/env python
#-*- coding:utf-8 -*-

variable_int = 1
variable_float = 1.0
variable_str = "Hello Python!"
variable_bool = True

# The type() function is for know the type of a object
print(type(variable_int)) # This is a Integer
print(type(variable_float)) # This is a float
print(type(variable_str)) # This is a string
print(type(variable_bool)) # This is a boolean

# Now we can start interact with other

print("This is a float: {}".format(variable_int + variable_float))
print("To proof, this is a float: {}"
      .format(type(variable_int + variable_float)))

# Now to interact with strings is a little weird.
# The way things work is like this:
print("{} My name is {}".format(variable_str, "Pharaoh"))
# Python i'll add the "Hello Python" string with the "My name is" string
# You can add a number too, but you need to cast.
print("I love Python. Python is the number {}. {}"
      .format(variable_int, variable_str))
# This example, with the format() function will convert all thing to a string
# Thats why you the format() is convenient.
# Lets use without:
try:
    print("I love Python. Python is the number " + variable_int,".",
          variable_str)
except TypeError as e:
    print("You cannot add a number with string. Error: {}".format(e))
# Dont need to understand this error handling now. This is just a example.
# Short explonation, the try: will literally try what you and, and
# the except will except the especific error, "TypeError" and now the
# program will not exit/crash, just output some error.

# And for the last the boolean
# Boolean if good for test things
if variable_bool is True:
    print("This is True. Because the variable passed is: {}"
          .format(variable_bool))
