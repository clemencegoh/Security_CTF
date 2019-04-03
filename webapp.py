from flask import Flask, request, abort, send_file, send_from_directory, render_template
import os
import sqlite3
import random
import os
from vignere import vignere

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
    file_content = vignere(text.encode(), key.encode())
    if not os.path.isfile('static/copypasta_encrypted.txt'):
        print('writing...')
        with open('static/copypasta_encrypted.txt', 'wb') as f:
            f.write(file_content)
    return file_content


@app.route('/', methods=['GET', 'POST'])
def home():
    query = ""

    if request.method == "POST":
        # tablename = request.form['tablename']
        imagename = request.form['imagename']

        print('received:', imagename)
        try:
            c = connectDB()
            if "drop" in imagename.lower():
                raise ValueError

            c.execute('''SELECT * 
                         FROM rick WHERE name LIKE '{}%' '''.format(imagename))
            query = c.fetchall()
            if len(query) > 10:
                query = query[0:10]
            print(query)

        except ValueError:
            query = [("dropping?","/static/data/no_drop.png")]

        except Exception as e:
            print(e)
            query = [("/static/data/ohno.png","Image not found")]

    ct = ""
    with open('copypasta.txt', 'r') as file:
        ct = createCipherText("MORTY", file.read())

    return render_template('index.html',
                           ciphertext=ct,
                           query=query)


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
    # app.run(host='0.0.0.0', port=80)
