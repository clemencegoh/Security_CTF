from flask import Flask, request, abort, send_file, send_from_directory
import os
import mysql.connector

app = Flask(__name__, static_url_path='/static')


#mydb = mysql.connector.connect(
#    host='localhost',
#    user='clemence',
#    passwd='clemence1',
#)

@app.route('/', methods=['GET'])
def base_root():
    return ''


@app.route('/addstuff/<stuff>', methods=['GET'])
def addStuff_test(stuff):
    return str(stuff)


if __name__=='__main__':
    app.run(port='8080')
