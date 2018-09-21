#!/usr/bin/python
# A simple script to pull some data from MySQL

import mysql.connector as mariadb

# Opens local file containing login information, appends it to a list
dbinfo = []
with open('login') as f:
    for i in f:
        dbinfo.append(i.strip())

# Tries to open a connection
connected = False
try:
    db = mariadb.connect(host=dbinfo[0], user=dbinfo[1], passwd=dbinfo[2], db=dbinfo[3])
    connected = True
    print("Successfully connected to database.")
except:
    print("Could not connect to server.")

# Defines schema
tables = {}
tables['items'] = (
    "CREATE TABLE items ("
    "  item_no int NOT NULL AUTO_INCREMENT,"
    "  name varchar(80) NOT NULL,"
    "  location varchar(160) NOT NULL,"
    "  quant int NOT NULL,"
    "  PRIMARY KEY (item_no)"
    ");")

# Starts connection loop. Currently no use, but will be required if more
# options are implimented. 
while connected:

    #create a cursor for the select
    cur = db.cursor()
    try:
        for i, x in tables.items():
            cur.execute(x)
            print("Table '{}' successfully created".format(i))
    except mariadb.Error as error:
        print("Error: {}".format(error.msg))

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
    
    print("Operations successful. Disconnecting...")
    cur.close()
    db.close()
    connected = False

print("Goodbye!")
