#!/usr/bin/python3
'''
3-my_safe_filter_states module filters all states
from the database hbtn_0e_0_usa that correspond
with searched input while preventing SQL injections
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
    cursor.execute("""SELECT *
                      FROM states
                      WHERE name=%s
                      ORDER BY id ASC""", (argv[4],))
    # print rows
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    conn.close()
