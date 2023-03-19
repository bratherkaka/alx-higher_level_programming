#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Take in four arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server running on localhost at port 3306
    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password, db=db_name, charset="utf8")
    cur = conn.cursor()

    # Execute SQL query to retrieve values
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                (state_name,))
    rows = cur.fetchall()

    # Display results as they are in the example
    for row in rows:
        print(row)

    # Close all cursors and database connections
    cur.close()
    conn.close()
