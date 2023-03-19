#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb


if __name__ == '__main__':
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Construct SQL query
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id".format(state_name)

    # Execute query
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close database connection
    db.close()
