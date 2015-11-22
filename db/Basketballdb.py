import csv

class Basketballdb(object):
    """Retrieve basketball information"""
    players = None;
    teams = None;
    def __init__(self):
        self.dbloc = './db/player_regular_season.csv'
    def getPlayers(self):
        players = []
        if(not self.players):
            with open('./db/player_regular_season.csv') as playerscsv:
                reader = csv.DictReader(playerscsv)
                for idx,row in enumerate(reader):
                    player = row
                    players.append(player)
            self.players = players
        return self.players
    def getTeams(self):
        teams = []
        if(not self.teams):
            with open('./db/teams.csv') as teamscsv:
                reader = csv.DictReader(teamscsv)
                for idx,row in enumerate(reader):
                    team = row
                    teams.append(team)
            self.teams = teams
        return self.teams
