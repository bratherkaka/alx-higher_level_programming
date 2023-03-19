#!/usr/bin/python3
"""
This module lists all cities of a given state
"""

import MySQLdb
import sys


def filter_cities():
    """
    This function filters and displays all cities of a given state
    """
    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    # Create a cursor to navigate the database
    cursor = db.cursor()

    # Execute SQL query to select all cities of the given state
    cursor.execute("SELECT cities.name FROM cities JOIN states ON \
                    cities.state_id = states.id WHERE states.name = %s \
                    ORDER BY cities.id ASC", (sys.argv[4], ))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Close cursor and database
    cursor.close()
    db.close()

    # Join the results into a string
    cities = ', '.join(row[0] for row in rows)

    # Print the results
    print(cities)


if __name__ == '__main__':
    filter_cities()
