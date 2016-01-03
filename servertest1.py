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
	return 'Welcome to the app'

def filterByPoints(points):
        result = False
        if points == 'pts':
                return [result]
        else:
                return False
        
def filterByrebounds(rebounds):
        result = False
        if rebounds == 'rebs':
                return [result]
        else:
                return False
def filterByasists(asists):
        result = False
        if asists == 'asts':
                return [result]
        else:
                return False
def filterBysteals(steals):
        result = False
        if steals == 'stls':
                return [result]
        else:
                return False
def filterByblocks(blocks):
        result = False
        if blocks == 'blk':
                return [result]
        else:
                return False
def filterByturnovers(turnovers):
        result = False
        if turnovers == 'turnovers':
                return [result]
        else:
                return False
 
        
        
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
        result = False
        if (thePlayer != False):
                for player in players:
                        if thePlayer == player['lastname']:
                                result = player
                                break
        else:
                return False

        if result:
                return [result]
        
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
                
        data = { 'teams' : teams, 'players' : players,
                 'filteredTeams' : filterteams[:50],
                 'filteredPlayers' : filterplayers[:50] }
        
        return render_template('main.html', data=data)
        #return json.dumps(filterteams)

if __name__ == '__main__':
	app.debug = True
	app.run()
