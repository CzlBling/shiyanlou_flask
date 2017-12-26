#!/usr/bin/env python3
from flask import Flask, render_template
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
	listdir = os.listdir('/home/shiyanlou/files/')
	index_dir = []
	for i in listdir:
		with open('/home/shiyanlou/files/' + i, 'r') as json_what:
			b = json.loads(json_what.read())
		index_dir.append(b['title'])
	return render_template('index.html', index_dir=index_dir)

@app.route('/files/<name>')
def files(name):
	if os.path.isfile('/home/shiyanlou/files/' + name + '.json'):
		with open('/home/shiyanlou/files/' + name + '.json', 'r') as json_what:
			a = json.loads(json_what.read())
		return render_template('base.html', a=a)
	else:	
		return render_template('404.html'), 404

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run()
