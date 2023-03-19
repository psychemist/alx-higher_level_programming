#!/usr/bin/python3
'''
5-filter_cities module lists all cities
from the database hbtn_0e_0_usa
while preventing SQL injections
'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # connect to database
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    # activate cursor and execute query
    cursor = conn.cursor()
    query = """SELECT cities.name
                 FROM cities
                 JOIN states
                   ON cities.state_id = states.id
                WHERE states.name = '{:s}'
            """.format(argv[4])
    cursor.execute(query)
    # print rows
    print(', '.join(row[0] for row in cursor.fetchall()))
    cursor.close()
    conn.close()
