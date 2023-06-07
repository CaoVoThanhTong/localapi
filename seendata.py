import sqlite3

# Connect to the database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Get the search keyword from the user
keyword = input("Enter the product name to search: ")

# Execute the SELECT query with the WHERE clause
cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + keyword + '%',))

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the connection to the database
conn.close()
