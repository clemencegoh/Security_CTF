import sqlite3
import json


DB_PATH = "./database.db"


def createConn():
    return sqlite3.connect(DB_PATH)


def Preprocess():
    """
    Example only, not meant to be used
    """

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS stocks
                 (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Never do this -- insecure!
    symbol = 'RHAT'
    c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

    # Do this instead
    t = ('RHAT',)
    c.execute('SELECT * FROM stocks WHERE symbol=?', t)
    print(c.fetchone())

    # Larger example that inserts many records at a time
    purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                 ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                 ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                 ]
    c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)


def cleanup(tables):
    """
    Used to clean up the database
    """
    conn = createConn()
    c = conn.cursor()
    for i in tables:
        c.execute('''DELETE FROM {};'''.format(i))
    conn.commit()

    # checking
    for i in tables:
        c.execute('''SELECT * FROM {}; '''.format(i))
        items = c.fetchall()
        if items != []:
            print('not empty for table {}, {}'.format(i, items))


def insertData():
    conn = createConn()
    c = conn.cursor()

    # create table
    c.execute('''CREATE TABLE IF NOT EXISTS rick
                (name text, path text)
    ''')

    content = []
    with open('images.txt', 'r') as imagefile:
        with open('names.txt', 'r') as namefile:
            images = imagefile.readlines()
            names = namefile.readlines()
            for i in range(len(images)):
                content.append((names[i].strip().lower(), images[i].strip()))

    # Insert into table here
    c.executemany('INSERT INTO rick values (?,?)', content[0:int(len(images)/2)])
    conn.commit()


    # custom images here
    custom = [
        ('morty', 'static/data/Morty.jpg'),
        ('maybe', 'static/data/maybe_neigh.jpg'),
        ('help', 'static/data/union.jpg'),
        ('hint', 'static/data/next_hint.jpg'),

    ]

    c.executemany('INSERT INTO rick values (?,?)', custom)
    conn.commit()

    c.executemany('INSERT INTO rick values (?,?)', content[int(len(images) / 2):int(len(images)/2) + 1])
    conn.commit()

    # final image for steg
    c.execute('''CREATE TABLE IF NOT EXISTS morty
                    (name text, path text)
        ''')
    finalImage = [('illusion', 'static/data/illusion.png')]
    c.executemany('INSERT INTO morty values (?,?)', finalImage)
    conn.commit()

    # fetch table and print
    c.execute(''' SELECT * FROM rick where name='velvet'; ''')
    print(len(c.fetchall()))


def trying():
    conn = createConn()
    c = conn.cursor()
    c.execute(''' SELECT * FROM rick where name='velvet'; ''')
    print(c.fetchall())



if __name__ == '__main__':
    # Preprocess()
    cleanup(['rick', 'morty'])
    insertData()

    # trying()
