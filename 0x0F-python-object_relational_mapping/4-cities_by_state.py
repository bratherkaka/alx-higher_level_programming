#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Connects to the MySQL server
    args = sys.argv
    user = args[1]
    password = args[2]
    db_name = args[3]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user,
                         passwd=password,
                         db=db_name)

    # Performs the SQL query
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
                      FROM cities
                      JOIN states ON cities.state_id = states.id
                      ORDER BY cities.id ASC""")
    rows = cursor.fetchall()

    # Prints the results
    for row in rows:
        print(row)

    # Closes the cursor and database connection
    cursor.close()
    db.close()
