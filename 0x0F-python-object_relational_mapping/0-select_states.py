#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Open database connection
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to fetch all the states with name starting with N
    sql = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print("Error: unable to fetch data")
        print(e)

    # disconnect from server
    db.close()
