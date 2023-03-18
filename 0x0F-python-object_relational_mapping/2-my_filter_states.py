#!/usr/bin/python3
'''0-select_states module lists all states from the database hbtn_0e_0_usa
'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # connect to database
    conn = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])
    # activate cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
                .format(argv[4]))
    # print rows
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
