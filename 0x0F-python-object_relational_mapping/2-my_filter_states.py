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
    # activate cursor and execute query
    cursor = conn.cursor()
    query = """SELECT * FROM states
               WHERE name = '{:s}'
               ORDER BY id ASC""".format(argv[4])
    cursor.execute(query)
    # print rows
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    conn.close()
