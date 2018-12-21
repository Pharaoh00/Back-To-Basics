#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Working with files
#
# When you are working with files
# you need to be careful.
# If you open a file, you need to close it.
# For this you can use:
# Context manager, simple "with statement".

import json # again dont worry with imports for now

my_data = {}
my_data["First"] = "python"
my_data["Second"] = "C++"
my_data["Third"] = "C"
my_data["Fourth"] = "JavaScript"

with open("test.json", "w") as f: # "w" means write
    data = json.dump(my_data, f, indent=4)
    # dump is a function from the json module
    # in the standard library.
    # dump means, "this data i want to put on a json file"
    # first argument is what you want
    # second is the file (this case is f) and
    # the optional is indent... 4 spaces.

# now if i want to read the file

with open("test.json", "r") as f: # "r" means read
    data = json.load(f)
    print(data)
    # And now we have all the data
    # you can "unpack" the data too
    for x in data:
        print("Key: {} - Value: {}".format(x, data[x]))
