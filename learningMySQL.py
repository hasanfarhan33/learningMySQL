import mysql.connector
from datetime import datetime

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
# mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("Faizan", 20))
# db.commit()

# mycursor.execute("SELECT * FROM Person")
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ("STEPHANIE", datetime.now(), 'F'))
# db.commit()

# mycursor.execute("SELECT id, name FROM Test WHERE gender = 'M' ORDER BY id DESC")
# for x in mycursor:
#     print(x)

# ALTERING TABLES
# mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")
mycursor.execute("ALTER TABLE Test DROP food")
mycursor.execute("DESCRIBE Test")
for x in mycursor:
    print(x)

