#!/usr/bin/python
# a simple script to pull some data from MySQL

import MySQLdb

db = MySQLdb.connect(host="", user="", passwd="", db="")

#create a cursor for the select
cur = db.cursor()

#execute an sql query
cur.execute("SELECT * FROM inventory.tools")

##Iterate
for row in cur.fetchall() :
    #data from rows
    tid = str(row[0])
    tname = str(row[1])
    tsize = str(row[2])
    tquant = str(row[3])
    tloc = str(row[4])
    #print
    print "This tool's name is %s. It's size is %s. You currently have %s of this tool. It is located at %s. "% (tname, tsize, tquant, tloc)

# close the cursor
cur.close()
# close the connection
db.close ()
