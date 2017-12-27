#!/usr/bin/env python3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql"//root@localhost/shiyanlou'
db = SQLAlchemy（app）

class File(db.Model):
	__tablename__ = 'files'
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(80))
	created_time = db.Column(db.DateTime)
	category_id = db.Column(db.Integer, db.ForeignKey(categorys.id))
	category = db.relationship('Category', uselist = False)
	content = db.Column(db.Text)

	def __init__(self, title, created_time, category, content):
		self.title = title
		self.created_time = created_time
		self.category = category
		self.content = content

class Category(db.Model):
	__tablename__ = 'categorys'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(80))
	files = db.relationship('File')

	def __init__(self, name):
		self.name = name

def write_datas():
	java = Category('Java')
	python = Category('Python')
	file1 = File('hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
	file2 = File('hello Python', datetime.utcnow(), java, 'File Content - Python is cool!')
	db.session.add(java)
	db.session.add(python)
	db.session.add(file1)
	db.session.add(file2)
	db.session.commit()

@app.route('/')
def index():


@app.route('/files/<file_id>')
def files(file_id):


@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run()
