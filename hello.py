from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
	return 'Welcome to the app'

@app.route('/query', methods=['POST', 'GET'])
def query():
	return request.args.get('team', 'default')

if __name__ == '__main__':
	app.debug = True
	app.run()
