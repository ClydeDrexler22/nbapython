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
                for player in (name.lower() for name in players):
                        if lastName.lower() == player['lastname']:
                                result.append(player)
        else:
                return players
        
                

        
        return result

def filterByPlayerFirstName(players, firstName):
        result = []
        if(firstName != False):
                for player in players:
                        if firstName == player['firstname']:
                                result.append(player)#build query to filter by first name ['firstname']
        else:
                return players

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

        return result

def filterByPoints(players, points):
        result = []
        if(points != False):
                for player in players:
                        try:
                                if int(points) <= int(player['pts']):
                                        result.append(player)
                        except ValueError:
                                continue
                        
        else:
                return players

        return result

def filterByRebounds(players, rebounds):
        result = []
        if(rebounds != False):
                for player in players:
                        try:
                                if int(rebounds) <= int(player['reb']):
                                        result.append(player)
                        except:
                                continue

        else:
                return players
        
        return result

def filterByAsists(players, asists):
        result = []
        if(asists != False):
                for player in players:
                        try:
                                if int(asists) <= int(player['asts']):
                                        result.append(player)
                        except:
                                continue

        else:
                return players
        
        return result

def filterBySteals(players, steals):
        result = []
        if(steals != False):
                for player in players:
                        try:
                                if int(steals) <= int(player['stl']):
                                        result.append(player)
                        except:
                                continue

        else:
                return players
        
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
        player_year = request.args.get('year', False)
        if( player_year ):
                filterplayers = filterByYear(filterplayers, player_year)

        #Filter By Points
        player_points = request.args.get('points', False)
        if(player_points):
                filterplayers = filterByPoints(filterplayers, player_points)

        #Filter By Rebounds
        player_rebounds = request.args.get('rebounds', False)
        if(player_rebounds):
                filterplayers = filterByRebounds(filterplayers, player_rebounds)

        #Filter By Asists
        player_asists = request.args.get('asists', False)
        if(player_asists):
                filterplayers = filterByAsists(filterplayers, player_asists)

        #Filter By Steals
        player_steals = request.args.get('steals', False)
        if(player_steals):
                filterplayers = filterBySteals(filterplayers, player_steals)
        

        
        if(len(filterplayers) == 0):
                return 'No Players Match Your Query'
                
        data = { 'teams' : teams, 'players' : players,
                 'filteredPlayers' : filterplayers[:100] }

        return render_template('main.html', data=data)
        #return json.dumps(filterteams)

if __name__ == '__main__':
	app.debug = True
	app.run()
