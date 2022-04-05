import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="hasanfarhan33",
    password="Farhan@1998",
    database="testDatabase"
)

mycursor = db.cursor()

# CREATING A TABLE
# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# DISPLAYING A TABLE
# mycursor.execute("DESCRIBE Person")
# for x in mycursor:
#     print(x)

# ADDING THINGS IN THE TABLE
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("Faizan", 20))
db.commit()

mycursor.execute("SELECT * FROM Person")
for x in mycursor:
    print(x)
