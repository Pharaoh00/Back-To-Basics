#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Control Flow
# Controlling the program flow is crucial.
#
# Like you see on the Data Structe tutorial
# you can use for loops to loop through a list
# Lets create a "fast" list to loop.
import time

for numbers in range(10):
    print(numbers)
    # So, this will create a sequence of numbers
    # from 0 to 10
    # the ouput is:
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # Remember, you tell python to create 10 numbers,
    # so 10 numbers in computers is 0 to 9.
    # If you need the number 10, you can specify
    # ... in range(11) or in range(10+1)
    # But the range() function work with two number.
    # Remember the default arguments from functions and variables?
    # range() have a default value.
    # The first value is 0. You dont need to pass.
    # You can tell python to begin on the number 1.
    # ... in range(1, 10)
    # but this will give 1 to 9 again.
    # The range works with the number you pass -1.

print("***************************************************")

# This is a control flow.
# You can make a clock, for whatever you need.

for clocks in range(1, 11):
    print(clocks)
    # This is the sleep from the module time
    # Dont worry with import right now.
    # We will see them.
    time.sleep(0.5) # If you want, you can comment this line. The code will run faster
    # Now, everytime the loop go through the clocks
    # they will wait half a second for loop again.

print("***************************************************")

# Lets take the clock loop and make another now.
# But now, we use a while loop.

clocks = 0
while clocks <= 10:
    # this mean, while the numbers from clocks
    # is less or equal (<=) 10... Keep going.
    print(clocks)
    time.sleep(0.5) # If you want, you can comment this line. The code will run faster
    clocks += 1 # this mean, take the curruent number and sum +1
    # Now we dont need to specify the number 11
    # because python know "less or EQUAL" to 10
    # When the clocks get to 10, the loop is over

print("***************************************************")

# Programs work with a while loop on the main function
# ALL THEM.
# They generic have a variable "running = True" or whataver
# And the program will run forever until "running = False"
# DONT RUN THIS CODE if you dont know how to manually break the loop
# running = True
# while running:
#     # "run the program"
#     print("running")
#
# This will run forever.

# Lets take a look at if/elif/else statement
# We use them on other tutorials.
# Lets take your example:

def beats(one, two):
    result = False

    # Only two outcome can occur
    # If you Win = True
    # If you Lose = False
    # This is the boolean logic (George Boole created this on 1854)
    # BEFORE all the computer stuff. Cool right?
    
    if one is two:
        return "Tie"
    # If the values is not equal
    # Keep trying
    # elif mean this
    # If you make another if here
    # the code works just fine... but
    # we i'll see a case which things get weird
    elif one is "rock":
        if two is "paper": # Rock Lose from paper
            return False
        elif two is "scissors": # Rock win from scissors
            return True
    elif one is "paper":
        if two is "rock": # Paper lose from rock
            return False
        elif two is "scissors": # Paper win from scissors
            return True
    elif one is "scissors": 
        if two is "rock": # Scissors lose from rock
            return False
        elif two is "paper": # Scissors win from paper
            return True

print(beats("rock", "rock")) # Tie
print(beats("rock", "paper")) # False
print(beats("rock", "scissors")) # Will print True

print(beats("paper", "rock")) # False
print(beats("paper", "scissors")) # True

print(beats("scissors", "rock")) # False
print(beats("scissors", "paper")) # True

# Lets explain more:
#
# When you test something python only have two options
# True of False
# Testing mean, "if this thing is True, do something"
# if you put another if again, and the value is the same
# the if statement will run again, because is the same value.
# BUT,
# if you put elif, and the fist thing is True,
# python only run on the first interation.
# I know, is confuse, but test this code.

foo = True
if foo is True:
    print("First-interation-1") # Will only run this
elif foo is True:
    print("First-interation-2")
if foo is True:
    print("Second-interation-1") # Will only run this
elif foor is True:
    print("Second-interation-2")

print("***************************************************")

# Now the fizzbuzz problem.
# The problem is:
# Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# Lets work.
# We need to work with module %, this is the factoring from math.
# Devide the number, and output the remaining.
# We need this, because we need to know if the number is multiple of 3
# if % 3 is 0 and if % 5 is 0.
# Lets write the program.
#
# Now, for this if/elif/else i need to you go on the Exercise folder
# and try solve the fizzbuzz problem.
