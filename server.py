import sys
import json
sys.path.append('./db/')
from Basketballdb import Basketballdb

from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
	return 'Welcome to the app.  Go to /query for the application home page.'

def filterByTeamName(players,theTeam):
        result = []
        if (theTeam != False):
        #return ateam
                for player in players:
                        if( not 'team_name' in player ):
                                continue
                        
                        if theTeam == player['team_name']:
                                result.append(player)
        else:
                return players

        if result:
                return result

def filterByPlayerLastName(players, lastName):
        result = []
        if (lastName != False):
                for player in players:
                        if lastName == player['lastname']:
                                result.append(player)
        else:
                return players

        if result:
                return result

def filterByPlayerFirstName(players, firstName):
        result = []
        if(firstName != False):
                for player in players:
                        if firstName == player['firstname']:
                                result.append(player)#build query to filter by first name ['firstname']
        else:
                return players

        if result:
                return result

def filterByYear(players, year):
        result = []
        if(year != False):
                for player in players:
                        if year == player['year']:
                                result.append(player) 
                        #build query to filter by year ['year']
        else:
                return players

        if result:
                return result

@app.route('/query', methods=['POST', 'GET'])
def query():
        #get full players and teams
        db = Basketballdb()
        teams = db.getTeams()
        players = db.getPlayers()

		#combine players with their team
        for player in players:
                for team in teams:
                    if player['team'] == team['team']:
                        player['team_league'] = team['leag']
                        player['team_location'] = team['location']
                        player['team_name'] = team['name']

        #start with full teams and players
        filterteams = teams
        filterplayers = players

        #TEAM NAME FILTER
        team_name = request.args.get('team', False)
        if( team_name ):
                if( team_name != 'Any' ):
                        filterplayers = filterByTeamName(filterplayers, team_name)

        #PLAYER LAST NAME 
        player_last_name = request.args.get('player_last_name', False)
        if( player_last_name ):
                filterplayers = filterByPlayerLastName(filterplayers, player_last_name)

        #PLAYER FIRST NAME
        player_first_name = request.args.get('player_first_name', False)
        if( player_first_name ):
                filterplayers = filterByPlayerFirstName(filterplayers, player_first_name)

        #FILTER BY YEAR
        player_year = request.args.get('player_year', False)
        if( player_year ):
                filterplayers = filterByYear(filterplayers, player_year)
                
        data = { 'teams' : teams, 'players' : players,
                 'filteredPlayers' : filterplayers[:100] }

        return render_template('main.html', data=data)
        #return json.dumps(filterteams)

if __name__ == '__main__':
	app.debug = True
	app.run()
