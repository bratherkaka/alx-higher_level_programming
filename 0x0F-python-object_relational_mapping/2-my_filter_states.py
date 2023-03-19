#!/usr/bin/python3
"""Module for filtering states by name"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(
            sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
                .format(state_name))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
