#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves the names of
cities that belong to a specific state.
The script takes command line arguments for the MySQL username,
password, database name, and the name of the state.
It then executes a SQL query to select the names of cities that
belong to the specified state, ordered alphabetically.
The script prints the names of the cities separated by commas.
"""

import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "INNER JOIN states ON "
                "cities.state_id = "
                "states.id WHERE states.name = %s ORDER BY "
                "cities.id ASC", (sys.argv[4],))

    rows = cur.fetchall()

    print(", ".join(row[1] for row in rows))

    cur.close()
    db.close()
