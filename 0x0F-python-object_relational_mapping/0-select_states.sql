# Connect to database
db = MySQLdb.connect(user=username, passwd=password, db=database)

# Create cursor to execute queries
cursor = db.cursor()

# Query to select all states
cursor.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all results
results = cursor.fetchall()

# Print results
for row in results:
    print(row)

# Close cursor and database
cursor.close()
db.close()
