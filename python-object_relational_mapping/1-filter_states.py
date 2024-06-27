#!/usr/bin/python3
"""
    Lists all the states that starts with the letter 'N' from a specified databse.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    user, passwd, db_name = sys.argv[1:4]
    db = MySQLdb.connect(user=user, password=passwd, database=db_name)
    cur = db.cursor()
    # Query ready.
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' COLLATE utf8_general_ci ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Clean up.
    cur.close
    db.close()
