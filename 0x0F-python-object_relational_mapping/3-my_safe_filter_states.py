#!/usr/bin/python3
"""
This script displays all values in the states table of hbtn_0e_0_usa where
name matches the argument. It is safe from SQL injections.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM states WHERE name=%s ORDER BY id ASC",
            (state_name,)
        )
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
    else:
        print("Usage: {:s} username password database_name state_name".format(
            sys.argv[0]))
