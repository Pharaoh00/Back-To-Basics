#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Data Structures
#
# The sequences are: list(), tuple(), set(), dict()
# They are the basics of working with data

# -- LIST --
# this is how you make a list
my_list = ["Python", "C", "C++", "Java", "JavaScrpit"]
print("Type of {}: {}".format("my_list", type(my_list)))

# You can loop through them:
# This is for another topic, but for loops is a control flow.
for x in my_list:
    print("Programming Language: {}".format(x)) 
    # And the for loop will loop all items in a list
    # a the "x" variable is each values from the list.
    # So:
    # first item is "Python"
    # second item is "C"
    # last item is "JavaScript"
    # Dont have more items.
    # Stop loop
print("**********************************************************")
# You can add more items on a list.
# you can use append on the list.
my_list.append("Ruby")
print(my_list) # Now you add the Ruby language on the final.

# You can ask the size of the sequence.
# You need to use the len() function
print("How many items are in my list? The list have: {} items"
      .format(len(my_list)))

# You can access only one item in the list.
# The index.
# On computer, all things begin wiht 0.
# The fist item in the list is index[0]
print("This is the first item on my_list: {}".format(my_list[0]))
# If you want, you can print the last too.
# You can use the -1. This tell python, "i want the last item from the list"
print("This is the first item on my_list: {}".format(my_list[-1]))

# You can ask if the list have a specific item
if "Python" in my_list:
    print("This item is on the list.")

if "Pascal" in my_list:
    print("This item is on the list.")
else:
    print("This item is not on the list.")
print("**********************************************************")
# You can remove a specific item from the list
my_list.remove("Ruby")
print(my_list) # Now the list does have the Ruby

# You can get the values from reverse
for x in reversed(my_list):
    print(x)
    # Will print JavaScript first
print("----------------------------------------------------------")

# -- TUPLE --
# Tuples have a interesting property
# This is how you make tuples
my_tuples = ("Orange", "Apples", "Bananas", "Blueberries")
print("Type of {}: {}".format("my_tuples", type(my_tuples)))

# You can loop through them, like a list.
# But tuples are immutables. When you create them
# you cant change the items inside.
# Lets try.

try:
    my_tuples.append("Pears")
    # or
    my_tuples.remove("Orange")
except AttributeError as e:
    print(e)

# or
try:
    my_tuples.remove("Orange")
except AttributeError as e:
    print(e)

# This is good for make something which can not be changed.
print("----------------------------------------------------------")

# Sets are good for make uniques items
# this is how you make sets
my_set = {1, 2, 3, 1, 2, 3}
print("Type of {}: {}".format("my_set", type(my_set)))
# The output will only {1, 2, 3}
print(my_set)

# They work different from lists and tuples.
# Will use them in the future.
# Now you only need to know they are a UNIQUE sets of items
print("----------------------------------------------------------")
# Now the dictionary are a sequence which have keys and values
my_dict = {"Python": 0, "C": 1, "C++": 2, "Java": 3, "JavaScript": 4}
print("Type of {}: {}".format("my_dict", type(my_dict)))
# For loop through them is a little different too.
# But i i'll show you.
for key, value in my_dict.items():
    print("Value of key {} is {}".format(key, value))

# For add something to a dictionary
# you need to specify the key and the value
my_dict["Ruby"] = 6
# Now you add Ruby as a Key with Value of 6
for key, value in my_dict.items():
    print("Value of key {} is {}".format(key, value))

# You can remove a Key from the list from her name.
my_dict.pop("Ruby")
print(my_dict)
print("----------------------------------------------------------")
# A little experiment to you see.
# I will make the same dictionary, my_dict
# but instead of write the values i i'll make them.

my_other_dict = {} # a empty dict
for num, item in enumerate(my_list):
    my_other_dict[item] = num

print(my_other_dict)
# Cool right?
# The enumerate() function follow the index's of the list
# so a loop through the my_list and made the Key the items
# from my_list and the Values the "index's".

