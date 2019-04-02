from flask import Flask, request, abort, send_file, send_from_directory, render_template
import os
import sqlite3
import random

app = Flask(__name__, static_url_path='/static')
DB_PATH = "./database/database.db"
DATA_PATH = "./static/data"


def connectDB():
    conn = sqlite3.connect(DB_PATH)
    return conn.cursor()


def createCipherText(key, text):
    """
    Placeholder for now, turns plaintext into ciphertext using key
    :param key: key for encrypting the text
    :param text: plaintext used
    :return: Ciphertext
    """
    return "Cipher_Text_Here"


@app.route('/', methods=['GET', 'POST'])
def home():
    imagepath = ""
    imagename = ""
    description = ""

    if request.method == "POST":
        tablename = request.form['tablename']
        imagename = request.form['imagename']

        print('received:', tablename, imagename)
        try:
            c = connectDB()
            c.execute('''SELECT * FROM {} WHERE name='{}'; '''.format(tablename, imagename))
            query = c.fetchone()
            print(query)
            imagename = query[1]
            imagepath = query[2]
            description = query[3]

        except:
            imagename = "Oh no"
            imagepath = "/static/data/ohno.png"
            description = "Something went wrong"

    print('imagepath:', imagepath)

    return render_template('index.html',
                           ciphertext=createCipherText("", ""),
                           imagepath=imagepath,
                           imagename=imagename,
                           description=description)


############# Fun Red Herrings #########################
@app.route('/next/<number>', methods=['GET'])
def getNext(number):
    if int(number) < 1121 or int(number) > 92901:
        return "<a href='/'>Go back home</a>"

    BASIC_STRING = "The next number is: "
    BASIC_STRING += str(random.randrange(1121, 92901))
    return BASIC_STRING


def checkDB():
    c = connectDB()
    c.execute(''' SELECT * FROM adam; ''')
    print(c.fetchall())


if __name__=='__main__':
    # checkDB()
    app.run(port='8080')
