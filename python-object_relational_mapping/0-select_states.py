#!/usr/bin/python3
# Lists all states from a specified database.
import sys
import MySQLdb

if __name__ == '__main__':
    user, passwd, db_name = sys.argv[1:4]
    db = MySQLdb.connect(user=user, password=passwd, database=db_name)
    cur = db.cursor()
    # Ready for a query.
    cur.execute("SELECT * FROM states ORDER BY id ASC limit 5")
    rows = cur.fetchall()
    for row in rows:
        print("({}, '{}')".format(*row))
    # Clean Up
    cur.close
    db.close()
