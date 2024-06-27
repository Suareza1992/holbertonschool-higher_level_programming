#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table of a specified table where name matches the argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    user, passwd, db_name, toMatch = sys.argv[1:5]
    db = MySQLdb.connect(user= user, password=passwd, database=db_name)
    cur = db.cursor()
    # Query ready
    cur.execute("SELECT * FROM states "
                "WHERE BINARY name='{}' "
                "ORDER BY id".format(state_name))
    for row in cur.fetchall():
        print(row)
    # Clean up
    cur.close()
    db.close()
