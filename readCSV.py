'''
        Author: Keval Shah
        Task:   Append player and team attributes to the pre-final training data
'''

import csv

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

csv_file = open('Data/finalData.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
fv_cols = []
for row in csv_reader:
    if line_count == 0:
        fv_cols = row
        print (fv_cols)
        line_count += 1
    else:
        fv[row[1]+row[2]+row[3]] = row
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

printDataDetail(teamD, team_cols, [10])


'''
Print an item from the feature vector

oneItem  = fv[fv.keys()[0]]
thisDate = oneItem[1]

print (oneItem)
'''