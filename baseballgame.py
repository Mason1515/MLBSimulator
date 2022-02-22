#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pitch import pitch, at_bat


# Using the at_bat() function to simulate a series of at bats while keeping track of outs, baserunners and runs scored
# You can uncomment the print statements to get a representation of the inner working of how each inning is played


def inning():
    bases = [0,0,0]
    outs = 0
    runs = 0
    
    while outs < 3:
        at_bat()
        #if sum(bases) > 0:
            #print(bases)
            #print("\n")
        
        #print(f"{outs} outs")
        
        
        if at_bat() == 'Out':
            #print('groundout')
            outs += 1
        elif at_bat() == 'Strikeout!':
            #print('strikeout')
            outs += 1
        elif at_bat() == 'Single!':
            #print('single')
            if bases == [0,0,0]:
                bases[0] = 1
            elif bases == [1,0,0]:
                bases[1] = 1
            elif bases == [1,1,0]:
                runs += 1
                bases = [1,1,0]
                #print('run scores')
            elif bases == [1,1,1]:
                runs += 2
                bases = [1,1,0]
            elif bases == [1,0,1]:
                runs += 1
                bases = [1,1,0]
                #print('run scores')
            elif bases == [0,1,1]:
                runs += 2
                bases = [1,0,0]
                #print('2 runs score')
            elif bases == [0,0,1]:
                runs += 1
                bases = [1,0,0]
                #print('run scores')
            elif bases == [0,1,0]:
                runs += 1
                bases = [1,0,0]
                #print('run scores')
        elif at_bat() == 'Double!':
            #print('double')
            if bases == [0,0,0]:
                bases = [0,1,0]
            elif bases == [1,0,0]:
                bases = [0,1,1]
            elif bases == [1,1,0]:
                runs += 1
                bases = [0,1,1]
                #print('run scores')
            elif bases == [1,1,1]:
                runs += 2
                bases = [0,1,1]
                #print('2 runs score')
            elif bases == [1,0,1]:
                runs += 1
                bases = [0,1,1]
                #print('run scores')
            elif bases == [0,1,1]:
                runs += 2
                bases = [0,1,0]
                #print('2 runs score')
            elif bases == [0,1,0]:
                runs += 1
                bases = [0,1,0]
                #print('run scores')
            elif bases == [0,0,1]:
                runs += 1
                bases = [0,1,0]
                #print('run scores')
        elif at_bat() == 'Triple!':
            #print('triple')
            if bases == [0,0,0]:
                bases = [0,0,1]
            elif bases == [1,0,0] or bases == [0,1,0] or bases == [0,0,1]:
                runs += 1
                bases == [0,0,1]
            elif bases == [1,1,0] or bases == [0,1,1] or bases == [1,0,1]:
                runs += 2
                bases = [0,0,1]
            elif bases == [1,1,1]:
                runs += 3
                bases = [0,0,1]
        elif at_bat() == 'Homerun!':
            #print('homerun')
            if sum(bases) == 0:
                runs += 1
            elif sum(bases) == 1:
                runs += 2
                bases = [0,0,0]
            elif sum(bases) == 2:
                runs += 3
                bases = [0,0,0]
            elif sum(bases) == 3:
                runs += 4
                bases = [0,0,0]
        elif at_bat() == 'Sacrifice Fly!':
            #print('sac fly')
            if outs < 2 and bases == [0,0,1]:
                outs += 1
                runs += 1
                bases = [0,0,0]
            elif outs < 2 and bases == [0,1,1]:
                outs += 1
                runs += 1
                bases = [0,0,1]
            elif outs == 2:
                runs += (sum(bases) + 1)
                bases = [0,0,0]
            else:
                outs += 1
        elif at_bat() == 'Double play!':
            #print('Double play')
            if outs > 0 and bases == [1,0,0] or bases == [1,0,1] or bases == [1,1,0] or bases == [1,1,1]:
                outs += 2
            elif bases == [0,0,0]:
                outs += 1
            elif bases == [1,0,0]:
                outs += 2
                bases = [0,0,0]
            elif bases == [1,1,0]:
                outs += 2
                bases = [0,0,1]
            elif bases == [1,1,1] and outs == 0:
                outs += 2
                runs += 1
                bases = [0,1,1]
            elif bases == [0,1,1]:
                outs += 1
                runs += 1
                bases = [1,0,1]
            elif bases == [1,0,1] and outs == 0:
                outs += 2
                runs += 1
                bases = [1,1,0]
            elif bases == [0,0,1]:
                outs += 1
                runs += 1
                bases = [1,0,0]
            elif bases == [0,1,0]:
                outs += 1
                bases = [0,1,1]
        elif at_bat() == 'Walk!':
            #print('walk')
            if bases == [0,0,0]:
                bases = [1,0,0]
            elif bases == [1,0,0]:
                bases = [1,1,0]
            elif bases == [1,1,0]:
                bases = [1,1,1]
            elif bases == [1,1,1]:
                runs += 1
            elif bases == [0,1,1]:
                bases = [1,1,1]
            elif bases == [1,0,1]:
                bases = [1,1,1]
            elif bases == [0,0,1]:
                bases = [1,0,1]
            elif bases == [0,1,0]:
                bases = [1,1,0]
                
    return runs   
            


# Play a full game consisting of at least 9 innings for each team, more if necessary
# Also keeping track of the box score

def fullGame(home,away):
    innings = 18
    home_score = 0
    home_box_score = []
    away_score = 0
    away_box_score = []
    
    while innings > 0:
        
        score = inning()
        away_score += score
        away_box_score.append(score)
        innings -= 1
        
        
        score = inning()
        home_score += score
        home_box_score.append(score)
        innings -= 1
    
    
    if home_score == away_score:
        home_extra = inning()
        home_score += home_extra
        home_box_score.append(home_extra)
        
        away_extra = inning()
        away_score += away_extra
        away_box_score.append(away_extra)
        
        while home_extra == away_extra:
            home_extra = inning()
            home_score += home_extra
            home_box_score.append(home_extra)
        
            away_extra = inning()
            away_score += away_extra
            away_box_score.append(away_extra) 
    
    if home_score > away_score:
        print(f"{home} win {home_score}-{away_score}")
        print(home_box_score)
        print(away_box_score)
        return home
    elif away_score > home_score:
        print(f"{away} win {away_score}-{home_score}")
        print(home_box_score)
        print(away_box_score)
        return away
    
        





