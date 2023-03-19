#!/usr/bin/python3
"""Module to filter states by name using MySQLdb"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 4:
        user = args[0]
        password = args[1]
        db_name = args[2]
        state_name = args[3]

        db = MySQLdb.connect(
            host="localhost",
            user=user,
            passwd=password,
            db=db_name,
            port=3306
        )
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(state_name)
        cursor.execute(query)

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        db.close()
