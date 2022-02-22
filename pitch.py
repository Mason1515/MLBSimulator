#!/usr/bin/env python
# coding: utf-8

# In[99]:


import random

# The idea of the pitch function is to simulate the roll of two dice, the outcome dependent on the numbers that are rolled

def pitch():
    pitch = ''
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice = [dice1,dice2]
    dice.sort()
    
    if dice == [1,1]:
        pitch = 'hit'
    elif dice == [1,2]:
        pitch = 'ball'
    elif dice == [1,3]:
        pitch = 'strike'
    elif dice == [1,4]:
        pitch = 'ball'
    elif dice == [1,5]:
        pitch = 'hit'
    elif dice == [1,6]:
        pitch = 'strike'
    elif dice == [2,2]:
        pitch = 'hit'
    elif dice == [2,3]:
        pitch = 'ball'
    elif dice == [2,4]:
        pitch = 'hit'
    elif dice == [2,5]:
        pitch = 'strike'
    elif dice == [2,6]:
        pitch = 'ball'
    elif dice == [3,3]:
        pitch = 'hit'
    elif dice == [3,4]:
        pitch = 'strike'
    elif dice == [3,5]:
        pitch = 'ball'
    elif dice == [3,6]:
        pitch = 'strike'
    elif dice == [4,4]:
        pitch = 'hit'
    elif dice == [4,5]:
        pitch = 'strike'
    elif dice == [4,6]:
        pitch = 'hit'
    elif dice == [5,5]:
        pitch = 'hit'
    elif dice == [5,6]:
        pitch = 'hit'
    elif dice == [6,6]:
        pitch = 'hit'

# Upon the occurence of a 'hit' you must then roll again to determine the outcome of the hit
    if pitch == 'hit':
        extra1 = random.randint(1,6)
        extra2 = random.randint(1,6)
        roll = [extra1,extra2]
        roll.sort()
        
        if roll == [1,1]:
            pitch = 'HR'
        elif roll == [1,2]:
            pitch = 'single'
        elif roll == [1,3]:
            pitch = 'single'
        elif roll == [1,4]:
            pitch = 'single'
        elif roll == [1,5]:
            pitch = 'out'
        elif roll == [1,6]:
            pitch = 'DP'
        elif roll == [2,2]:
            pitch = 'double'
        elif roll == [2,3]:
            pitch = 'out'
        elif roll == [2,4]:
            pitch = 'out'
        elif roll == [2,5]:
            pitch = 'DP'
        elif roll == [2,6]:
            pitch = 'single'
        elif roll == [3,3]:
            pitch = 'double'
        elif roll == [3,4]:
            pitch = 'DP'
        elif roll == [3,5]:
            pitch = 'single'
        elif roll == [3,6]:
            pitch = 'out'
        elif roll == [4,4]:
            pitch = 'double'
        elif roll == [4,5]:
            pitch = 'out'
        elif roll == [4,6]:
            pitch = 'out'
        elif roll == [5,5]:
            pitch = 'triple'
        elif roll == [5,6]:
            pitch = 'single'
        elif roll == [6,6]:
            pitch = 'sac'
        return pitch
    else:
        return pitch


# Series of pitches keeping track of balls and strikes, you can uncomment the print statements to see the count update

def at_bat():
    balls = 0
    strikes = 0
    
    while balls < 4 and strikes < 3:
        pitch()
        if pitch() == 'ball':
            balls += 1
            #print(f"{balls}-{strikes} count")
        elif pitch() == 'strike':
            strikes += 1
            #print(f"{balls}-{strikes} count")
        elif pitch() == 'out':
            return "Out"
        elif pitch() == 'DP':
            return "Double play!"
        elif pitch() == 'single':
            return "Single!"
        elif pitch() == 'double':
            return "Double!"
        elif pitch() == 'triple':
            return "Triple!"
        elif pitch() == 'HR':
            return "Homerun!"
        elif pitch() == 'sac':
            return "Sacrifice fly!"
        
    if strikes == 3:
        return "Strikeout!"
    elif balls == 4:
        return "Walk!"






