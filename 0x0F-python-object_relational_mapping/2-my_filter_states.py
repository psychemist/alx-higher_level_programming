#!/usr/bin/python3
'''
2-my_filter_states module filters all states
from the database hbtn_0e_0_usa
that correspond with the searched name input
'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # connect to database
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    # activate cursor and execute query
    cursor = conn.cursor()
    query = """SELECT *
               FROM states
               WHERE name = '{:s}'
               ORDER BY id ASC""".format(argv[4])
    cursor.execute(query)
    # print rows
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    conn.close()
