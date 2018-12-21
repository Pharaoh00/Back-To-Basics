#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ----------------------------------------------------------- #
# Filename: test.py
# Creation Date: sexta-feira, 21 dezembro 2018 04:40
# Author: Hamon-Rá Taveira Guimarães
# Contact:
#         GitHub: https://github.com/
#         E-mail: hamoncsl@hotmail.com
#         Facebook: https://www.facebook.com/hamonra.taveira
# ----------------------------------------------------------- #

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

    def battle(self, defensor):
        damage = self.atack_p - defensor.defense_p
        defensor.health -= damage
        
p1 = Player("Pharaoh", "Warrior", 10, 5)
p2 = Player("Skeleton", "Necromancer", 5, 2, mana=500, is_friend=False)

while p1.health >= 0 or p2.health >= 0:
    p1.battle(p2)
    p1.battle(p2)
    print(p2.health)
    if p1.health <= 0 or p2.health <= 0:
        break
