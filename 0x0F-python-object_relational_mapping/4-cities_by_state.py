#!/usr/bin/python3
'''
4-cities_by_state module lists all cities
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
    query = """SELECT cities.id, cities.name, states.name
                 FROM cities
                 JOIN states
                   ON cities.state_id = states.id
                ORDER BY cities.id ASC;
            """
    cursor.execute(query)
    # print rows
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()
