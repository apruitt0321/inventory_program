#!/usr/bin/python
# A python class wrapper for simply mysql interaction. 

import mysql.connector as mariadb

class Mary(object): 
    def __init__(self, login='login'):
        
        self.dbinfo = []
        self.connected = False
        self.db = None
        self.tables = {}
        self.cursor = None
        
        # Opens local file containing login information, appends it to a list
        with open(login) as f:
            for i in f:
                self.dbinfo.append(i.strip())

    # Opens connection to database.
    def connect_db(self):    
        try:
            self.db = mariadb.connect(host=self.dbinfo[0], user=self.dbinfo[1], passwd=self.dbinfo[2], db=self.dbinfo[3])
            self.connected = True
            print("Connected to database!")
        except:
            print("Could not connect to database Please check login info.")

        # Creates cursor if database connection was successful.    
        if self.connected:
            self.cursor = self.db.cursor()
        else:
            print("Not connected to database!")

    # Closes connection to database.
    def close_db(self):
        if self.connected:
            self.cursor.close()
            self.db.close()
            self.connected = False
            print("Database connection closed.")
        else:
            print("Not connected to database.")
    
    def define_schema(self, t={'default':"CREATE TABLE default (num int NOT NULL);"}):
        # Defines schema
        for i, x in t.items():
            self.tables[i] = (x)
    
    def push_schema(self):
        if self.connected:
            try:
                for i, x in self.tables.items():
                    self.cursor.execute(x)
                    print("Table '{}' successfully created.".format(i))
            except mariadb.Error as error:
                print("Error: {}".format(error.msg))
        else:
            print("Not connected to database.")

    def select_from(self, x, y):
        if self.connected:
            self.cursor.execute("SELECT {} FROM {};".format(x,y))
        else:
            print("Not connected to database.")

    def select_from_where(self, x, y, z):
        if self.connected:
            self.cursor.execute("SELECT {} FROM {} WHERE {};".format(x,y,z))

    def fetchall(self):
        if self.connected:
            return self.cursor.fetchall()

if __name__ == "__main__":
    t = {}
    t['items'] = ("CREATE TABLE items ("
                 "  item_no int(3) NOT NULL AUTO_INCREMENT,"
                 "  name varchar(80) NOT NULL,"
                 "  location varchar(160) NOT NULL,"
                 "  quant int NOT NULL,"
                 "  PRIMARY KEY (item_no));")
    mdb = Mary()
    mdb.connect_db()
    mdb.define_schema(t)
    mdb.push_schema()
    item_add = ("INSERT INTO items "
                "(item_no, name, location, quant) "
                "VALUES (001, 'hammer', 'A7', 1);")
    
    item_add2 = ("INSERT INTO items "
                 "(name, location, quant) "
                 "VALUES ('screwdriver', 'A7', 1);")
    item_add3 = ("INSERT INTO items "
                 "(name, location, quant) "
                 "VALUES ('ruler', 'A7', 1);")

    try:
        mdb.cursor.execute(item_add)
        print("Item added to database.")
        mdb.db.commit()
        print("Changes committed")
    except:
        print("Items not added to database.")
        
    try:
        mdb.cursor.execute(item_add2)
        print("Item added to database.")
        mdb.db.commit()
        print("Changes committed")
    except:
        print("Items not added to database.")


    mdb.select_from('*','items')
    for i in mdb.fetchall():
        print(i)
    mdb.select_from_where('*', 'items', 'name="hammer"')
    for i in mdb.fetchall():
        print(i)
#    # Execute an sql query
#    cur.execute("SELECT * FROM inventory.tools")
#    # Iterate over the selection
#    for row in cur.fetchall() :
#       #data from rows
#       tid = str(row[0])
#       tname = str(row[1])
#       tsize = str(row[2])
#       tquant = str(row[3])
#       tloc = str(row[4])
#       print "This tool's name is %s. It's size is %s. You currently have %s of this tool. It is located at %s. "% (tname, tsize, tquant, tloc)

    print("Operations finished. Disconnecting...")
    mdb.close_db()
    print("Goodbye!")
