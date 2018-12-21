#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Object Oriented Programming or OOP
# This is the core of working with classes
#
# You don't need to understand this right now
# but all things in python are objects, meaning,
# all functions/implementation are a classe somewhere
# on the source code.
#
# Lets have a quick look
# You know the module random right?
# Import random
# random()
# This is are is generated.
# random.py
#
# PLEASE
# DONT WORRY WITH THIS STUFF
# IS ONLY FOR YOU TO SEE.

# class Random(_random.Random):
#     """Random number generator base class used by bound module functions.

#     Used to instantiate instances of Random to get generators that don't
#     share state.

#     Class Random can also be subclassed if you want to use a different basic
#     generator of your own devising: in that case, override the following
#     methods:  random(), seed(), getstate(), and setstate().
#     Optionally, implement a getrandbits() method so that randrange()
#     can cover arbitrarily large ranges.

#     """

#     VERSION = 3     # used by getstate/setstate

#     def __init__(self, x=None):
#         """Initialize an instance.

#         Optional argument x controls seeding, as for Random.seed().
#         """

#         self.seed(x)
#         self.gauss_next = None

#         ...

#         def choice(self, seq):
#             """Choose a random element from a non-empty sequence."""
#             try:
#                 i = self._randbelow(len(seq))
#             except ValueError:
#                 raise IndexError('Cannot choose from an empty sequence') from None
#             return seq[i]
        
# You see?
# When you call random.choice(), internally
# the function call _randbelow function and
# use on random.choice()
# Is hard to explain whats are happening, but
# the _randbelow is calling another function
# getrandbits who make bits operations...
# this is something more deep, even for me.
# I dont understand fully.
# The _randbelow make some error handling, and return the result.
# AND now, the choice() have the answer.
# Everything in python is a object. is a class.

# Now, we can begin.
#
# Lets use a game concept for this.
# Class's are good for two reasons (have more than two, but...)
# Don't repeat code, and organize.
# Games have entities, right?
# Players, NPCs, Enemys, etc...
# So, whats they share?
# Name: --- [string]
# Health: --- [integer]
# Mana: --- [integer]
# Class: --- (warrior, mage, etc) [string]
# isFrieadly: --- [True or False]
# Now, lets code.

# If you don't know about classes, you would do something like this:

def player(name, health, mana, clas, is_fried):

    return "The name is: {} - MaxHealth is: {} - MaxMana is: {} - Class is: {}".format(name, health, mana, clas)

player1 = player("Pharaoh", 100, 100, "Worrior", True)
player2 = player("deathxroe", 100, 100, "Worrior", True)
print(player1)
print(player2)

# Reallt weird right?
# If i want to check the health from player1 and player2?
# I would have to make some logic to do this.

# With OOP easily accomplished

class Player: #always class's name should start with upper case

    some_variable = 1 # this is a class variable

    # when you are working with class you need to refer
    # the functions and variables of her with "self"
    # self mean:
    # "This code is from the same class's we are working with"
    # When you create a new function you need to use:
    # def someFunction(self, your_arguments)
    # and when you create some variable on initialization (__init__)
    # or the class variable
    # you will refer with self.some_variable.
    
    def __init__(self, name, char, health=100, mana=100, is_friend=True):
        # we make the class Player accept a name, the Class (warrios, mage, etc)
        # and health, mana, is_friend are default arguments.
        self.name = name # for convetion, we use the same name
        self.char = char # Short for characteristics
        self.health = health
        self.mana = mana
        self.is_friend = is_friend
        # This init method will be created at
        # the object creation time.
        # All the properties, all the code inside __init__

p1 = Player("Pharaoh", "Warrior")
print(p1)
# When you print this, python will return something like that
# <__main__.Player object at 0x00000...>
# This is the actually location of your class on memory.
# You see? Python know "this is a object at ..."
#
# Now if you want to print something from the class you need to call
print(p1.name)
print(p1.char)

# You can make more than one object of a class
# That is the purpose of a class

p2 = Player("deathxroe", "Mage")
print(p2.name)
print(p2.char)

p3 = Player("Skeleton", "Necromancer", mana=500, is_friend=False)
print(p3.name)
print(p3.char)
print(p3.health)
print(p3.mana)
print(p3.is_friend)

print("****************************************************************")

# Lets tinkering our class

class Player:
    
    def __init__(self, name, char, health=100, mana=100, is_friend=True):
        self.name = name 
        self.char = char # Short for characteristics
        self.health = health
        self.mana = mana
        self.is_friend = is_friend

    def __eq__(self, other):
        # This is a magic method
        # Dont worry to much about it right now.
        # If you want, you can check this site:
        # https://rszalski.github.io/magicmethods/
        #
        # This mean if foo == bar:
        # __eq__ is the "==" operation
        #
        # if self.is_friend is True and other.is_friend is True:
        #     return True
        # elif self.is_friend is True and other.is_friend is False:
        #     return False

        if self.is_friend and other.is_friend:
            # if both is True, return True
            return True
        elif not self.is_friend or not other.is_friend:
            # if one of them is False, return False
            return False

        # Another convetion, but...
        # "is", "not" is a GOOD convetion.

p1 = Player("Pharaoh", "Warrior")
p2 = Player("deathxroe", "Mage")
p3 = Player("Skeleton", "Necromancer", mana=500, is_friend=False)

if not p1 == p3:
    print("Be careful. This entity is hostile.")

if p1 == p2:
    print("Good to have a ally.")

print("****************************************************************")

#
# Lets talk about inheritance
# We will tinkering our class again.
# 
# First we need to change the name of her

class Entetie: # Not the right name, but for now is simple enough
    
    def __init__(self, name, char, health=100, mana=100, is_friend=True):
        self.name = name 
        self.char = char # Short for characteristics
        self.health = health
        self.mana = mana
        self.is_friend = is_friend

    def __eq__(self, other):

        if self.is_friend and other.is_friend:
            # if both is True, return True
            return True
        elif not self.is_friend or not other.is_friend:
            # if one of them is False, return False
            return False

class Player(Entetie):
    pass
    # "pass" mean:
    # "This class does have nothing yet,
    # But create something for now."

p1 = Player("Pharaoh", "Warrior")
print(p1.name)
# We can access the name. But the class Player does have nothing.
# Thats because Player inheritance from Entitie which have the
# name variable.
# We can add something more, without change Entitie.

print("---------------------------------------------------------------")

class Player(Entetie):
    # To properly initialize the heiress class
    def __init__(self, name, last_name,
                 guild, char,
                 health=100, mana=100, is_friend=True):
        # Make how you want the class to be initialized
        super().__init__(name, char, health, mana, is_friend)
        # And with super you call the init from the Entetie
        self.last_name = last_name
        self.guild = guild

p1 = Player("Pharaoh", "Zatt", "The Alliance", "Warrior", mana=150, health=200)
print(p1.guild)
print(p1.mana)
print(p1.last_name)
print("---------------------------------------------------------------")
p2 = Player("deathxroe", "Apollyon", "The Vanguards", "Viking",
            health=250, mana=50)
print(p2.guild)
print(p2.mana)
print(p2.last_name)
print("---------------------------------------------------------------")
# And now we can make a separate class for the enemys

class Enemy(Entetie):
    def __init__(self, name, guild, char,
                 health=100, mana=100, is_friend=False):
        # Make how you want the class to be initialized
        super().__init__(name, char, health, mana, is_friend)
        # And with super you call the init from the Entetie
        self.guild = guild

e1 = Enemy("The False Prophet", "Unholy Circle", "Dark Mage", mana=500)
print(e1.name)
print(e1.guild)
print(e1.char)
print("---------------------------------------------------------------")
e2 = Enemy("Skeleton King", "Catedral of Death", "Dark Warrior", health=500)
print(e2.name)
print(e2.guild)
print(e2.char)

