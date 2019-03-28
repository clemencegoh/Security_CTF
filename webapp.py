from flask import Flask, request, abort, send_file, send_from_directory, render_template
import os
import sqlite3
import random

app = Flask(__name__, static_url_path='/static')
DB_PATH = "./database/database.db"
DATA_PATH = "./static/data"


def connectDB():
    return sqlite3.connect(DB_PATH)


def createTables():
    conn = connectDB()
    cur = conn.cursor()
    cur.execute("")


def createCipherText(key, text):
    """
    Placeholder for now, turns plaintext into ciphertext using key
    :param key: key for encrypting the text
    :param text: plaintext used
    :return: Ciphertext
    """
    return "hello world!"


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html',
                           ciphertext=createCipherText("", ""))


@app.route('/addstuff/<stuff>', methods=['GET'])
def addStuff_test(stuff):
    return str(stuff)


@app.route('/database', methods=['POST'])
def searchDB():
    return ""


@app.route('/test', methods=['GET'])
def testDB():
    return ""


############# Fun Red Herrings #########################
@app.route('/next/<number>', methods=['GET'])
def getNext(number):
    if int(number) < 1121 or int(number) > 92901:
        return "<a href='/'>Go back home</a>"

    BASIC_STRING = "The next number is: "
    BASIC_STRING += str(random.randrange(1121, 92901))
    return BASIC_STRING


if __name__=='__main__':
    app.run(port='8080')
