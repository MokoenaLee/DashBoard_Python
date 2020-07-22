from flask import Flask, render_template, request
from pusher import Pusher
import os

app = Flask(__name__)

#configure puher object

pusher = Pusher(
app_id= '1042883',
key= 'bed9d59bf5e0a729296e',
secret= '6ff7ed7d1573ca20e013',
cluster= 'us3',
ssl= True )


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')


@app.route('/orders', methods=['POST'])
def order():
	data = request.form 
	pusher.trigger(u'order', u'place',
	{
	 u'units': data['units']
	
	})
	return "units logged"

@app.route('/message', methods=['POST'])
def message():
	data  = request.form
	pusher.trigger(u'message', u'send', {
		u'name' : data['name'],
		u'message' : data['message']
		})
	return 'message sent'

@app.route('/customer', methods=['POST'])
def customer():
	data = request.form 
	pusher.trigger(u'customer', u'add', {
		u'name'  : data['name'],
		u'title' : data['title'],
		u'office': data['office'],
		u'cost'  : data['cost'],
	})
	return "customer added"

if __name__ == '__main__':
	app.run(debug=True)