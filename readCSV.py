'''
        Author: Keval Shah
        Task:   Append player and team attributes to the pre-final training data
'''

import csv

# Team mappings
teamNames = {
    'Blackpool' : 'Blackpool',
    'Wigan Athletic' : 'Wigan',
    'Bolton Wanderers' : 'Bolton',
    'Fulham' : 'Fulham',
    'Aston Villa' : 'Aston Villa',
    'West Ham United' : 'West Ham',
    'Blackburn Rovers' : 'Blackburn',
    'Everton' : 'Everton',
    'Watford' : 'Watford',
    'West Bromwich Albion' : 'West Brom',
    'Tottenham Hotspur' : 'Tottenham',
    'Queens Park Rangers' : 'QPR',
    'Arsenal' : 'Arsenal',
    'Norwich City' : 'Norwich',
    'Chelsea' : 'Chelsea',
    'Bournemouth' : 'Bournemouth',
    'Manchester United' : 'Man United',
    'Leicester City' : 'Leicester',
    'Newcastle United' : 'Newcastle',
    'Crystal Palace' : 'Crystal Palace',
    'Southampton' : 'Southampton',
    'Manchester City' : 'Man City',
    'Stoke City' : 'Stoke',
    'Sunderland' : 'Sunderland',
    'Swansea City' : 'Swansea',
    'Cardiff City' : 'Cardiff',
    'Burnley' : 'Burnley',
    'Hull City' : 'Hull',
    'Portsmouth' : 'Portsmouth',
    'Middlesbrough' : 'Middlesbrough',
    'Liverpool' : 'Liverpool',
    'Reading' : 'Reading',
    'Wolverhampton Wanderers' : 'Wolves',
    'Birmingham City' : 'Birmingham'
}

# Team mappings
teamNamesRev = {
    'Blackpool' : 'Blackpool',
    'Wigan' : 'Wigan Athletic',
    'Bolton' : 'Bolton Wanderers',
    'Fulham' : 'Fulham',
    'Aston Villa' : 'Aston Villa',
    'West Ham' : 'West Ham United',
    'Blackburn' : 'Blackburn Rovers',
    'Everton' : 'Everton',
    'Watford' : 'Watford',
    'West Brom' : 'West Bromwich Albion',
    'Tottenham' : 'Tottenham Hotspur',
    'QPR' : 'Queens Park Rangers',
    'Arsenal' : 'Arsenal',
    'Norwich' : 'Norwich City',
    'Chelsea' : 'Chelsea',
    'Bournemouth' : 'Bournemouth',
    'Man United' : 'Manchester United',
    'Leicester' : 'Leicester City',
    'Newcastle' : 'Newcastle United',
    'Crystal Palace' : 'Crystal Palace',
    'Southampton' : 'Southampton',
    'Man City' : 'Manchester City',
    'Stoke' : 'Stoke City',
    'Sunderland' : 'Sunderland',
    'Swansea' : 'Swansea City',
    'Cardiff' : 'Cardiff City',
    'Burnley' : 'Burnley',
    'Hull' : 'Hull City',
    'Portsmouth' : 'Portsmouth',
    'Middlesbrough' : 'Middlesbrough',
    'Liverpool' : 'Liverpool',
    'Reading' : 'Reading',
    'Wolves' : 'Wolverhampton Wanderers',
    'Birmingham' : 'Birmingham City'
}

playerD = {}
teamD = {}
matchD = {}

fv = {}

csv_file = open('Data/players.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
player_cols = []
for row in csv_reader:
    if line_count == 0:
        player_cols = row
        print (player_cols)
        line_count += 1
    else:
        playerD[row[1]] = row
        line_count += 1
csv_file.close()

csv_file = open('Data/teamAll.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
team_cols = []
for row in csv_reader:
    if line_count == 0:
        team_cols = row
        print (team_cols)
        line_count += 1
    else:
        teamD[row[1]] = row
        line_count += 1
csv_file.close()

csv_file = open('Data/matchWithPlayers.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
match_cols = []
for row in csv_reader:
    if line_count == 0:
        match_cols = row
        print (match_cols)
        line_count += 1
    else:
        matchD[row[6]] = row
        line_count += 1
csv_file.close()

# print a match instance
# print (matchD[matchD.keys()[0]])

csv_file = open('Data/final_processed_1.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
fv_cols = []
for row in csv_reader:
    if line_count == 0:
        fv_cols = row
        print (fv_cols)
        line_count += 1
    else:
        fv[row[1]] = row
        line_count += 1
csv_file.close()

def printDataDetail(data, dataCols, idList):
    for item in idList:
        for i, val in enumerate(dataCols):
            print (val+" : "+data[data.keys()[item]][i])
        print ("\n")

# print data item details
# printDataDetail(fv, fv_cols, [0])
# printDataDetail(matchD, match_cols, [0])
# printDataDetail(teamD, team_cols, [0])


'''

READING AND PARSING DATA DONE!

Now, I want to replace the ids in 'matches' with values
    
    - 1.   Add/modify a column for team Attributes
    - 2.   Team ID -> Team Name (for both away and home)
    - 3.   Player ID -> Player Attributes (for all the 22 players)

'''

printDataDetail(matchD, match_cols, [10])

# 1. Generate overall team attributes and add a column to matches

teamOverall_id = {}
teamOverall_name = {}
for tID, aTeam in teamD.items():
    tScore = 0
    nScores = 0
    for iScore in [9, 11, 13, 16, 18, 20, 23, 25, 27]:
        aScore = aTeam[iScore]
        if aScore == '':
            tScore += 30    ## Giving a default value!
        else:
            tScore += int(aScore)
        nScores += 1
    # Take average or total?
    # tScore = tScore/nScores
    # print (aTeam[3], tScore)

    teamOverall_id[tID] = tScore
    teamOverall_name[aTeam[3]] = tScore

for mID, aMatch in matchD.items():
    # print (matchD[mID])
    matchD[mID].append(teamOverall_id[aMatch[7]])
    matchD[mID].append(teamOverall_id[aMatch[8]])
    # print (matchD[mID])

# 2. Team ID -> Team Name !! DONE
for mID, aMatch in matchD.items():
    aMatch[7] = teamD[aMatch[7]][3]
    aMatch[8] = teamD[aMatch[8]][3]

# 3. Player ID -> Player attribute !! DONE
for mID, aMatch in matchD.items():
    for pID in range(55,77):
        try:
            aMatch[pID] = playerD[aMatch[pID]][8]
        except Exception, e:
            # Give 45 if data not found
            aMatch[pID] = 45

printDataDetail(matchD, match_cols, [10])


''' CODE FOR EXTRACTING UNIQUE TEAMS '''
# uniq = []
# for key, val in matchD.items():
#     if val[2] == '1729' and val not in uniq:
#         uniq.append(val)

# uTeams = []
# for uid in uniq:
#     if uid[7] not in uTeams:
#         uTeams.append(uid[7])
#     if uid[8] not in uTeams:
#         uTeams.append(uid[8])
# print ((uTeams))

'''
The next and final step is to integrate the attributes from matches to the fv
For this I will create a new dictionary for matches with the key as (home_away_date)
'''

matchesWithKey = {}

for key, val in matchD.items():
    matchHomeT = teamNames[val[7]]
    matchAwayT = teamNames[val[8]]
    matchDate = val[5][:10]
    key = matchHomeT+'_'+matchAwayT+'_'+matchDate
    matchesWithKey[key] = val

# print (matchesWithKey.keys()[0])

#Print an item from the feature vector
# oneItem  = fv[fv.keys()[0]]
# thisDate = oneItem[1]
# print (oneItem)

# Add the column names to the header
for i in range(1, 12):
    fv_cols.append("home_player_"+str(i))
for i in range(1, 12):
    fv_cols.append("away_player_"+str(i))
fv_cols.append("home_team_overall")
fv_cols.append("away_team_overall")
# print (fv_cols)

# Finally append the attributes!
for key, val in fv.items():
    add22Players = matchesWithKey[key]
    homeAttr = teamOverall_name[teamNamesRev[val[2]]]
    awayAttr = teamOverall_name[teamNamesRev[val[3]]]
    fv[key] += add22Players[55:77] + [str(homeAttr)] + [str(awayAttr)]

import csv

enhancedDataFile = open('final_processed_2.csv', mode='w')
enhancedDataFile = csv.writer(enhancedDataFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

enhancedDataFile.writerow(fv_cols)
for val in fv.values():
    enhancedDataFile.writerow(val)