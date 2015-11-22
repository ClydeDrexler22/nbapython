import sys
import json
sys.path.append('./db/')
from Basketballdb import Basketballdb

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
	return 'Welcome to the app'

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
                return result

#did we get team at all?
def filterByPositionName(positions, thePosition):
        result = False
        if (thePostition != False):
                for position in positions:
                        if thePosition == position['name']:
                                result = position
                                break
        else:
                return False
        
        if result:
                return result

@app.route('/query', methods=['POST', 'GET'])
def query():
        db = Basketballdb()
        theTeam = request.args.get('team', False)
        teams = db.getTeams()
        filterteams = filterByTeamName(teams,theTeam)
        thePosition = request.args.get('position', False)
        positions = db.getPositions() 
        filterpositions = filterByPositionName(positions,thePosition)
        return json.dumps(filterteams)
        return json.dumps(filerpositions)

if __name__ == '__main__':
	app.debug = True
	app.run()


        
