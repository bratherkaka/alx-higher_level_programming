#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to database
    db = MySQLdb.connect(user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    # Execute query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Display results
    for row in cursor.fetchall():
        print(row)

    # Close connection
    cursor.close()
    db.close()
