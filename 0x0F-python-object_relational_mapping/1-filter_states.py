#!/usr/bin/python3
'''
1-filter_states module lists all states
from the database hbtn_0e_0_usa
basded on states that begin with 'N'
'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    # activate cursor
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    # print rows
    for row in cur.fetchall():
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
