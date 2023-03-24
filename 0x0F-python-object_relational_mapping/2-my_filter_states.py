#!/usr/bin/python3
"""2-my_filter_states.py - Displays all values in the states table where name matches the argument"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{2}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
