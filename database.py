import sqlite3
from random import randrange

def create_a_marker(self):
    conn = sqlite3.connect('MainDataBase')
    c = conn.cursor()

    pass


def get_all_markers(self):
    conn = sqlite3.connect('MainDataBase')
    c = conn.cursor()



        #c.execute("""CREATE TABLE markers (
        #            name text,
        #            lat REAL,
        #            lon REAL
        #            )""")
        #c.execute("INSERT INTO markers VALUES('my rent home', 59.955370, 30.305982)")
    c.execute("SELECT * FROM markers")
    print(c.fetchall())
    conn.commit()
    conn.close()

def get_x_marker(self, x):
    conn = sqlite3.connect('MainDataBase')
    c = conn.cursor()

    c.execute("SELECT * FROM markers")
    list_of_markers = (c.fetchall())
    print(list_of_markers[x])


    conn.commit()
    conn.close()


def add_marker_to_database(lat='', lon=''):
    conn = sqlite3.connect('MainDataBase')
    c = conn.cursor()
    quiry=("INSERT INTO markers VALUES( ")
    lat=str(lat)
    lon=str(lon)
    name=randrange(0,100000)
    name="name:"+str(name)
    quiry=(quiry+"'"+name+"'"+', '+lat+', '+lon+')')
    print(quiry)
    c.execute(quiry)
    conn.commit()
    conn.close()

#item = database()

#item.get_all_markers()
#item.get_x_marker(1)


