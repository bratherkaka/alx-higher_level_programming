#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb


if __name__ == '__main__':
    # Check command line arguments
    if len(sys.argv) != 5:
        print('Usage: {} username password database state_name'.format(
            sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Construct SQL query with user input
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(
        state_name)

    # Execute SQL query
    cur.execute(query)

    # Print results
    for row in cur.fetchall():
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
