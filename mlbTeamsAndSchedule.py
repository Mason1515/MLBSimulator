#!/usr/bin/env python
# coding: utf-8

# In[24]:


import csv


# Use the teams csv file to grab the correct name of each team


data = open('mlbteams.csv')
csv_data = csv.reader(data)
data_lines = list(csv_data)


# Make sure the teams are in the right league


teams = list(set(line[1] for line in data_lines[1:]))
two_leagues = list(set(line[5] for line in data_lines[1:]))

# Make sure the teams are in the right division


divisions = set(line[6] for line in data_lines[1:])
teams_by_division = {}
for i in divisions:
    teams_by_division[i] = []
for line in data_lines[1:]:
    if line[6] in divisions:
        teams_by_division[line[6]].append(line[1])





team_names = {}
for team in teams:
    team_names[team] = ''
for line in data_lines[1:]:
    if line[1] in team_names:
        team_names[line[1]] = line[0]


teams_by_league = {}
for i in two_leagues:
    teams_by_league[i] = []
for league in teams_by_league:
    for line in data_lines[1:]:
        if line[5] == league:
            teams_by_league[league].append(line[0])


schedule = open('mlb-2021-UTC.csv')
game_data = csv.reader(schedule)
games = list(game_data)


# Use the schedule csv file to grab the 2021 schedule


all_games = list([line[4],line[5]] for line in games[1:])


# This function takes 2 team names and finds their abbreviation but i don't think it proved to be necessary

def find_abb(home_team,away_team):
    for key, val in team_names.items():
        if val == home_team:
            home_team_name = key
        elif val == away_team:
            away_team_name = key
    return [home_team_name,away_team_name]







