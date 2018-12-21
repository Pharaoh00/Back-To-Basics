#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Player:
    
    def __init__(self, name, char, atack_p, defense_p,
                 health=100, mana=100, is_friend=True):
        self.name = name 
        self.char = char # Short for characteristics
        self.atack_p = atack_p # atack points
        self.defense_p = defense_p # defense_p
        self.health = health
        self.mana = mana
        self.is_friend = is_friend
        self.damage = 0 # Just a way to output this damage

    def __eq__(self, other):

        if self.is_friend and other.is_friend:
            return True
        elif not self.is_friend or not other.is_friend:
            return False

    def battle(self, defensor):
        # The function battle is only here to show you.
        # You need to create another function or class to handle the combat "mode".
        # You can make two modes, battle mode, and i dont know, resupply mod. Buy stuff and etc.
        # With "resupply mod" you can have a currency and a NPC to buy.
        # Only your creativity can stop you. 
        self.damage = self.atack_p - defensor.defense_p
        defensor.health -= self.damage
        
p1 = Player("Pharaoh", "Warrior", 10, 5)
p2 = Player("Skeleton", "Necromancer", 5, 2, mana=500, is_friend=False)

if not p1 == p2: # Dump check for hostilite
    print("You encounter a Enemy!")
    print("Enemy {} have {} of life.".format(p2.name, p2.health))
    while p1.health >= 0 or p2.health >= 0:
        p1.battle(p2)
        print("Your damage are: {} - Your enemy life: {}"
              .format(p1.damage, p2.health))
        if p1.health <= 0 or p2.health <= 0:
            break
