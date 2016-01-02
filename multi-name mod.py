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

def filterByTeamName(teams,theTeam):
        result = False
        if (theTeam != False):
        #return ateam
                for team in teams:
                        if theTeam == team['name']:
                                result = team
                                break
        else:
                return False

        if result:
                return [result]

def filterByPlayerName(players, thePlayer):
        a = [];
        result = False
        while (thePlayer != False):
                for player in players:
                        if thePlayer == player['lastname']:
                                result = player
                                a.append(result)
                                break
                                
        else:
                return False

        if result:
                return a
                
        
        
        
@app.route('/query', methods=['POST', 'GET'])
def query():
        #get full players and teams
        db = Basketballdb()
        teams = db.getTeams()
        players = db.getPlayers()

        #start with full teams and players
        filterteams = teams
        filterplayers = players

        #filters
        if( request.args.get('team', False) ):
            filterteams = filterByTeamName(filterteams, request.args.get('team', False))

        if( request.args.get('player_last_name', False) ):
            filterplayers = filterByPlayerName(players, request.args.get('player_last_name', False))
                
        data = { 'teams' : teams, 'players' : players,
                 'filteredTeams' : filterteams[:50],
                 'filteredPlayers' : filterplayers[:50] }
        
        return render_template('main.html', data=data)
        #return json.dumps(filterteams)

if __name__ == '__main__':
	app.debug = True
	app.run()
