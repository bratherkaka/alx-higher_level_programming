#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


if __name__ == '__main__':
    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object
    cur = db.cursor()

    # Execute SQL query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows and print them line by line
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connections
    cur.close()
    db.close()
