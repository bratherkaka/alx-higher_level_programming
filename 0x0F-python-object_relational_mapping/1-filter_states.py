#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=db_name)

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows and print them as tuples
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close all cursors and the database connection
    cur.close()
    db.close()
