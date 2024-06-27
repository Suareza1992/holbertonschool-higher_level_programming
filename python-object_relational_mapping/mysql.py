import mysql.connector

# Establish connection to MySQL
cnx = mysql.connector.connect(
    user='your_username',
    password='your_password',
    host='localhost',
    database='your_database_name'
)

# Perform operations (e.g., execute queries)
cursor = cnx.cursor()
cursor.execute("SELECT * FROM your_table")
for row in cursor:
    print(row)

# Close cursor and connection
cursor.close()
cnx.close()

