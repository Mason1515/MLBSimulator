#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pitch import pitch, at_bat
from baseballgame import inning, fullGame
from mlbTeamsAndSchedule import teams_by_division, teams, team_names, all_games, teams_by_league


# Initialize dictionaries keeping track of team records and making sure the teams are in the right conference/divison

records_by_team = {}
for i in teams:
    records_by_team[team_names[i]] = [0,0]

division_winners = {}
for i in teams_by_division:
    division_winners[i] = ''
    
leagues = {}
for i in teams_by_division:
    leagues[i[0:2]] = []


# Play entire season and keep track of wins and losses as each game is played

def playSeason():
    for game in all_games:
        winner = fullGame(game[0],game[1])
        if winner == game[0]:
            records_by_team[winner][0] += 1
            records_by_team[game[1]][1] += 1
        else:
            records_by_team[winner][0] += 1
            records_by_team[game[0]][1] += 1


#playSeason()


# Use data from the season to determine which teams win their respective division

for i in teams_by_division:
    most_wins = 0
    current_best = ''
    for j in teams_by_division[i]:
        if j in team_names:
            if records_by_team[team_names[j]][0] > most_wins:
                current_best = team_names[j]
                most_wins = records_by_team[team_names[j]][0]
    division_winners[i] = current_best
    
for league in leagues:
    for division in division_winners:
        if division[0:2] == league:
            leagues[league].append(division_winners[division])

#Also have to find 2 wildcard teams per conference 

for league in leagues:
    while len(leagues[league]) < 5:
        
        most_wins = 0
        wildcard = ''
        for division in teams_by_division:
            if division[0:2] == league:
                for team in teams_by_division[division]:
                    if records_by_team[team_names[team]][0] > most_wins and team_names[team] not in leagues[league]:
                        most_wins = records_by_team[team_names[team]][0]
                        wildcard = team_names[team]
                    elif team_names[team] in leagues[league]:
                        continue
        leagues[league].append(wildcard)


# Initialize dictionaries containing each playoff team with their corresponding seed

al_seeding = {}
for i in range(1,6):
    al_seeding[i] = ''
    
nl_seeding = {}
for i in range(1,6):
    nl_seeding[i] = ''

# Use the team records to determine the seeding order of each team, starting with the division winners first then the wildcards

teams_used = []
for i in range(3):
    current_best = max(list(records_by_team[team][0] for team in leagues['AL'][:3] if team not in teams_used))
    for team in leagues['AL'][:3]:
        if records_by_team[team][0] == current_best and team not in teams_used:
            best_team = team
    if best_team not in al_seeding.values():
        al_seeding[min(list(i for i in al_seeding.keys() if al_seeding[i] == ''))] = best_team
        teams_used.append(best_team) 
for team in leagues['AL'][3:]:
    if team not in teams_used:
        al_seeding[min(list(i for i in al_seeding.keys() if al_seeding[i] == ''))] = team
        
for i in range(3):
    current_best = max(list(records_by_team[team][0] for team in leagues['NL'][:3] if team not in teams_used))
    for team in leagues['NL'][:3]:
        if records_by_team[team][0] == current_best and team not in teams_used:
            best_team = team
    if best_team not in nl_seeding.values():
        nl_seeding[min(list(i for i in nl_seeding.keys() if nl_seeding[i] == ''))] = best_team
        teams_used.append(best_team) 
for team in leagues['NL'][3:]:
    if team not in teams_used:
        nl_seeding[min(list(i for i in nl_seeding.keys() if nl_seeding[i] == ''))] = team
        
al_seeds = dict((val,key) for key,val in al_seeding.items())
nl_seeds = dict((val,key) for key,val in nl_seeding.items())
al_seeds.update(nl_seeds)
all_seeds = al_seeds


# Establish a global variable that will be used in the check_seed() function which is necessary for the playoff bracket logic

global teams_lost
teams_lost = []

# Wildcard teams play one game to decide who will play the 1 seed in the divisional round

def playWildcard():
    global teams_lost
    teams_lost = []
    
    
    games_won = [0,0]
    nl_wildcard = fullGame(nl_seeding[4],nl_seeding[5])
    al_wildcard = fullGame(al_seeding[4],al_seeding[5])
    if nl_wildcard == nl_seeding[4]:
        teams_lost.append(nl_seeding[5])
    else:
        teams_lost.append(nl_seeding[4])
        
    print(f"{nl_wildcard} move on!\n")
        
    if al_wildcard == al_seeding[4]:
        teams_lost.append(al_seeding[5])
    else:
        teams_lost.append(al_seeding[4])
        
    print(f"{al_wildcard} move on!\n")

# Best of 5 series in which the wildcard game winner plays the 1 seed in their conference while the 2 plays the 3    

def playDivisional():
    games_won = [0,0]
    while games_won[0] < 3 and games_won[1] < 3:
        nl_game_winner = fullGame(nl_seeding[1],nl_seeding[max(check_seed()[0])])
        print(f"{nl_game_winner} win game {sum(games_won) + 1}\n")
        if nl_game_winner == nl_seeding[1]:
            games_won[0] += 1
        else:
            games_won[1] += 1
    if games_won[0] == 3:
        teams_lost.append(nl_seeding[max(check_seed()[1])])
        print(f"{nl_seeding[1]} move on!\n")
    else:
        teams_lost.append(nl_seeding[1])
        print(f"{nl_seeding[max(check_seed()[0])]} move on!\n")
        
    
    
    games_won = [0,0]
    while games_won[0] < 3 and games_won[1] < 3:
        al_game_winner = fullGame(al_seeding[1],al_seeding[max(check_seed()[1])])
        print(f"{al_game_winner} win game {sum(games_won) + 1}\n")
        if al_game_winner == al_seeding[1]:
            games_won[0] += 1
        else:
            games_won[1] += 1
    if games_won[0] == 3:
        teams_lost.append(al_seeding[max(check_seed()[1])])
        print(f"{al_seeding[1]} move on!\n")
    else:
        teams_lost.append(al_seeding[1])
        print(f"{al_seeding[max(check_seed()[1])]} move on!\n")
        
    
    games_won = [0,0]
    while games_won[0] < 3 and games_won[1] < 3:
        al_game_winner = fullGame(al_seeding[2],al_seeding[3])
        print(f"{al_game_winner} win game {sum(games_won) + 1}\n")
        if al_game_winner == al_seeding[2]:
            games_won[0] += 1
        else:
            games_won[1] += 1
    if games_won[0] == 3:
        teams_lost.append(al_seeding[3])
        print(f"{al_seeding[2]} move on!\n")
    else:
        teams_lost.append(al_seeding[2])
        print(f"{al_seeding[3]} move on!\n")
        
    games_won = [0,0]
    while games_won[0] < 3 and games_won[1] < 3:
        nl_game_winner = fullGame(nl_seeding[2],nl_seeding[3])
        print(f"{nl_game_winner} win game {sum(games_won) + 1}\n")
        if nl_game_winner == nl_seeding[2]:
            games_won[0] += 1
        else:
            games_won[1] += 1
    if games_won[0] == 3:
        teams_lost.append(nl_seeding[3])
        print(f"{nl_seeding[2]} move on!\n")
    else:
        teams_lost.append(nl_seeding[2])
        print(f"{nl_seeding[3]} move on!\n")        

# Best of 7 series in which the worst remaining seed plays @ the best remaining seed in each conference

def playChampionshipSeries():
    games_won = [0,0]
    while games_won[0] < 4 and games_won[1] < 4:
        nl_game_winner = fullGame(nl_seeding[min(check_seed()[0])], nl_seeding[max(check_seed()[0])])
        print(f"{nl_game_winner} win game {sum(games_won) + 1}\n")
        if nl_game_winner == nl_seeding[min(check_seed()[0])]:
            games_won[0] += 1
        else:
            games_won[1] += 1
    if games_won[0] == 4:
        teams_lost.append(nl_seeding[max(check_seed()[0])])
        print(f"{nl_seeding[min(check_seed()[0])]} move on!\n")
    else:
        teams_lost.append(nl_seeding[min(check_seed()[0])])
        print(f"{nl_seeding[max(check_seed()[0])]} move on!\n")
              
    games_won = [0,0]
    while games_won[0] < 4 and games_won[1] < 4:
        al_game_winner = fullGame(al_seeding[min(check_seed()[1])], al_seeding[max(check_seed()[1])])
        print(f"{al_game_winner} win game {sum(games_won) + 1}\n")
        if al_game_winner == al_seeding[min(check_seed()[1])]:
            games_won[0] += 1
        else:
            games_won[1] += 1
    if games_won[0] == 4:
        teams_lost.append(al_seeding[max(check_seed()[1])])
        print(f"{al_seeding[min(check_seed()[1])]} move on!\n")
    else:
        teams_lost.append(al_seeding[min(check_seed()[1])])
        print(f"{al_seeding[max(check_seed()[1])]} move on!\n")    

# Best of 7 series in which the last remaining AL team plays the last remaining NL team
        
def playWorldSeries():
    games_won = [0,0]
    while games_won[0] < 4 and games_won[1] < 4:
        ws_game_winner = fullGame(al_seeding[min(check_seed()[1])],nl_seeding[min(check_seed()[0])])
        if ws_game_winner == al_seeding[min(check_seed()[1])]:
            print(f"{ws_game_winner} win game {sum(games_won) + 1}\n")
            games_won[0] += 1
        else:
            print(f"{ws_game_winner} win game {sum(games_won) + 1}\n")
            games_won[1] += 1
    
    if games_won[0] == 4:
        print(f"{al_seeding[min(check_seed()[1])]} win World Series!")
    else:
        print(f"{nl_seeding[min(check_seed()[0])]} win World Series!")
    
#In case you want to play the entire postseason all at once instead of taking it round by round
    
def playPostseason():
    playWildcard()
    playDivisional()
    playChampionshipSeries()
    playWorldSeries()


# This function checks the seed of each remaining team to determine matchups in later rounds of the playoffs
    
def check_seed():
    nl = [all_seeds[i] for i in leagues['NL'] if i not in teams_lost] 
    al = [all_seeds[j] for j in leagues['AL'] if j not in teams_lost]
    nl.sort()
    al.sort()
    return nl,al





