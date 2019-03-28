from flask import Flask, request, abort, send_file, send_from_directory, render_template
import os
import mysql.connector
import sqlite3

app = Flask(__name__, static_url_path='/static')
DATABASE_PATH = "./database/database.db"


def connectDB():
    return sqlite3.connect(DATABASE_PATH)


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
    return render_template('index.html', ciphertext=createCipherText("",""))


@app.route('/addstuff/<stuff>', methods=['GET'])
def addStuff_test(stuff):
    return str(stuff)


@app.route('/database', methods=['POST'])
def searchDB():
    return ""


if __name__=='__main__':
    app.run(port='8080')
