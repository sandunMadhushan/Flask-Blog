import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
)

my_cursor = mydb.cursor()

# Uncomment the following line to create a database
# my_cursor.execute("CREATE DATABASE flask_blog_users")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)