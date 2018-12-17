#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Functions and arguments
# DISCLAIMER
# About the naming:
# Pep8 https://www.python.org/dev/peps/pep-0008/#function-and-variable-names
# Call how naming should be.
# I do not follow all the rules
# For example:
# variable names should be lowercase, with words separated by underscores as necessary to improve readability.
# And Functions names is the same.
#
# For me is a little bit confuse
# so i make my variables names separated with underscores
# and my functions start with lowercase and uppercase for separate.

def myFunction(): # this is how you let python know, "this is a function"
    # All variables inside this "scope"
    # is from this function. You cannot
    # access the function variable out side.
    # This mean:
    # my_variable is only acessed by myFunction()
    my_variable = 1
    return my_variable

print("From myFunction: {}".format(myFunction()))
# You need to pass your function name + ()
# this is how you call your function.

def myOtherFunction(a, b):
    return a + b
# The a and b are functions arguments
print("From myOtherFunction: {}".format(myOtherFunction(1, 2)))

# If you dont pass one argument, will give a error.
# TypeError, missing arguments.
# Lets try.
try:
    print("From myOtherFunction: {}".format(myOtherFunction(1)))

except TypeError as e:
    print(e)

# "Required" argument. Huuum!
# Lets tinker something.

def myFunctionWithDefault(a, b=1):
    return a + b

print("From myFunctionWithDefault: {}".format(myFunctionWithDefault(1)))
# Now the argument "b" is a default argument,
# because you pass the value on the argument

# Now lets see about keyword arguments

def myKeywordArguments(a=2, b=1):
    return a + b

# You don't need to pass anything, because the arguments are default.
# BUT...
print("From myKeywordArguments: {}".format(myKeywordArguments()))
# Now you can pass the arguments with their name
print("From myKeywordArguments: {}".format(myKeywordArguments(b=5, a=5)))
# Without the order they are.
# You can pass "b" first, and "a" last.

