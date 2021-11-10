import random
from collections import Counter

def playoffs(teams_record):

    print("Playoffs: ")
    print (" ")
    a = {}
    a = dict(Counter(teams_record).most_common(8))
    playoff_teams = list(a.keys())

    counter = len(playoff_teams)
    week1_winners = []
    print("Playoffs Week 1: ")
    for i in range(len(playoff_teams)):
        if counter == 0:
            break
        team1 = random.choice(playoff_teams)
        playoff_teams.remove(team1)
        team2 = random.choice(playoff_teams)
        playoff_teams.remove(team2)

        #determines a winner between two teams
        matchup = [team1, team2]
        winner = random.choice(matchup)
        week1_winners.append(winner)

        score = 7*random.randint(1,4)+ 3*random.randint(0,2)
        score2 = 7*random.randint(1,4)+ 3*random.randint(0,2)
        holder = 0

        if score == score2:
            score = score + 3
        if score2 > score:
            holder = score2
            score2 = score
            score = holder

        counter = counter - 2
        print(team1 + " at " + team2 + " -- Winner = " + winner + " -- Score = " + str(score) + "-" + str(score2))

    print(" ")

    counter = len(week1_winners)
    week2_winners = []
    print("Playoffs Week 2: ")
    for i in range(len(week1_winners)):
        if counter == 0:
            break
        team1 = random.choice(week1_winners)
        week1_winners.remove(team1)
        team2 = random.choice(week1_winners)
        week1_winners.remove(team2)

        #determines a winner between two teams
        matchup = [team1, team2]
        winner = random.choice(matchup)
        week2_winners.append(winner)

        score = 7*random.randint(1,4)+ 3*random.randint(0,2)
        score2 = 7*random.randint(1,4)+ 3*random.randint(0,2)
        holder = 0

        if score == score2:
            score = score + 3
        if score2 > score:
            holder = score2
            score2 = score
            score = holder

        counter = counter - 2
        print(team1 + " at " + team2 + " -- Winner = " + winner + " -- Score = " + str(score) + "-" + str(score2))

    print(" ")

#Super Bowl Winner
    print("Super Bowl Weekend: ")
    team1 = week2_winners[0]
    team2 = week2_winners[1]

    #determines a winner between two teams
    matchup = [team1, team2]
    winner = random.choice(matchup)

    score = 7*random.randint(1,4)+ 3*random.randint(0,2)
    score2 = 7*random.randint(1,4)+ 3*random.randint(0,2)
    holder = 0

    if score == score2:
        score = score + 3
    if score2 > score:
        holder = score2
        score2 = score
        score = holder

    print("THE " + winner.upper() + " WIN THE SUPER BOWL" + " -- Score = " + str(score) + "-" + str(score2))
    print(" ")


def weekMaker(teams, teams_record, week):
    counter = len(teams)
    print(" ")
    print(week)
    used_teams = []
    for i in range(len(teams)):
        if counter == 0:
            break
        team1 = random.choice(teams)
        teams.remove(team1)
        team2 = random.choice(teams)
        teams.remove(team2)

        #determines a winner between two teams
        matchup = [team1, team2]
        winner = random.choice(matchup)

        # sets the teams record
        teams_record[winner] += 1
        if winner == team1:
            teams_record[team2] -= 1
        else:
            teams_record[team1] -= 1

        score = 7*random.randint(1,4)+ 3*random.randint(0,2)
        score2 = 7*random.randint(1,4)+ 3*random.randint(0,2)
        holder = 0

        if score == score2:
            score = score + 3
        if score2 > score:
            holder = score2
            score2 = score
            score = holder

        counter = counter - 2
        print(team1 + " at " + team2 + " -- Winner = " + winner + " " + str(teams_record[winner]) + " -- Score = " + str(score) + "-" + str(score2))

    print(" ")

teams_record = {"Arizona Cardinals" : 0, "Baltimore Ravens" : 0, "Atlanta Falcons" : 0, "Buffalo Bills" : 0, "Carolina Panthers" : 0, "Cincinnati Bengals" : 0, "Chicago Bears" : 0, "Cleveland Browns" : 0, "Dallas Cowboys" : 0, "Denver Broncos" : 0, "Detroit Lions" : 0, "Houston Texans" : 0, "Green Bay Packers" : 0, "Indianapolis Colts" : 0, "Los Angeles Rams" : 0, "Jacksonville Jaguars" : 0, "Minnesota Viking" : 0, "Kansas City Chiefs" : 0, "New Orleans Saints" : 0, "Las Vegas Raiders" : 0, "New York Giants" : 0, "Los Angeles Chargers" : 0, "Philadelphia Eagles" : 0, "Miami Dolphins" : 0, "San Francisco 49ers" : 0, "New England Patriots" : 0, "Seattle Seahawks" : 0, "New York Jets" : 0, "Tampa Bay Buccaneers" : 0, "Pittsburgh Steelers" : 0, "Washington Football Team" : 0, "Tennessee Titans" : 0}

teams = ["Arizona Cardinals", "Baltimore Ravens", "Atlanta Falcons", "Buffalo Bills", "Carolina Panthers", "Cincinnati Bengals", "Chicago Bears", "Cleveland Browns", "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Houston Texans", "Green Bay Packers", "Indianapolis Colts", "Los Angeles Rams", "Jacksonville Jaguars", "Minnesota Viking", "Kansas City Chiefs", "New Orleans Saints", "Las Vegas Raiders", "New York Giants", "Los Angeles Chargers", "Philadelphia Eagles", "Miami Dolphins", "San Francisco 49ers", "New England Patriots", "Seattle Seahawks", "New York Jets", "Tampa Bay Buccaneers", "Pittsburgh Steelers", "Washington Football Team", "Tennessee Titans"]

teams_backup = ["Arizona Cardinals", "Baltimore Ravens", "Atlanta Falcons", "Buffalo Bills", "Carolina Panthers", "Cincinnati Bengals", "Chicago Bears", "Cleveland Browns", "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Houston Texans", "Green Bay Packers", "Indianapolis Colts", "Los Angeles Rams", "Jacksonville Jaguars", "Minnesota Viking", "Kansas City Chiefs", "New Orleans Saints", "Las Vegas Raiders", "New York Giants", "Los Angeles Chargers", "Philadelphia Eagles", "Miami Dolphins", "San Francisco 49ers", "New England Patriots", "Seattle Seahawks", "New York Jets", "Tampa Bay Buccaneers", "Pittsburgh Steelers", "Washington Football Team", "Tennessee Titans"]

for i in range(1,19):
    if not teams:
        teams.extend(teams_backup)
    season = "Week " + str(i)
    weekMaker(teams, teams_record, season)

playoffs(teams_record)
