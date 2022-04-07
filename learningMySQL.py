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


users = [("Timothy", "screwTimothyFromCanada", "2345", "iamjealousoftimothy@gmail.com"),
         ("Paul", "paulFromTheBeatles", "johnisdead1", "liveandletdie@gmail.com"),
         ("George", "georgeFromTheBeatles", "johnisdefinitelydead1", "nooneremembersmysongs@gmail.com"),
         ("Ringo", "ringoFromTheBeatles", "imissmyumbrella1", "whereismyumbrella@gmail.com"),
         ("John", "johnFromTheBeatles", "bulletinagun1", "thereisdefinitelynoheaven@gmail.com"),
         ("Jerry", "jerryFromSeinfeld", "passwordsareuseless", "kramerisannoying@gmail.com"),
         ("George", "georgeFromSeinfeld", "worldsarecolliding", "halfprice@gmail.com"),
         ("Elaine", "elaineFromSeinfeld", "johnfkennedyjunior", "laidoutforme@gmail.com"),
         ("Kramer", "kramerFromSeinfeld", "kosmokramer", "pigmanisoutthere@gmail.com"),
         ("Desiree", "emma_pfann1977", "Xah6chohSae", "paolo.zbonc@hotmail.com"),
         ("Nancy", "bryan", "aiThoh5och", "nasir2004@gmail.com"),
         ("Armando", "ceasar.med1974", "noh8Ujae", "garrick2007@hotmail.com"),
         ("Gary", "garywithausername1", "IeGah3iep5", "viviane2011@gmail.com"),
         ("Sandra", "Bivaliner", "shu7aYah", "gudrun_macejkov@gmail.com"),
         ("Christy", "andrew", "ahCh6eed9", "corine2009@hotmail.com"),
         ("Gary", "ultraspikes", "sojaro5Th", "ila_ryan1972@gmail.com"),
         ("John", "ashlee", "bee5Umud", "carolyn.torp@gmail.com"),
         ("Neal", "adelbert.p2008", "hooHee6eeVai", "darius1983@yahoo.com"),
         ("Johnny", "TheHollowCarter", "piquoh8Uong", "kasandra1981@hotmail.com"),
         ("Martha", "elia", "laht6IGohj1", "carli.oreil@gmail.com")]

userScores = [(54, 96),
              (63, 34),
              (11, 87),
              (83, 82),
              (90, 85),
              (8, 39),
              (23, 95),
              (23 ,43),
              (33, 94),
              (32 ,38),
              (74, 83),
              (21, 19),
              (54, 87),
              (45, 54),
              (37, 56),
              (89, 35),
              (98, 28),
              (54, 49),
              (28, 95),
              (39, 69)]

# Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), username VARCHAR(50), password VARCHAR(50), emailAddress VARCHAR(50))"
# Q2 = "CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"
Q3 = "INSERT INTO Users (name, username, password, emailAddress) VALUES (%s, %s, %s, %s)"
Q4 = "INSERT INTO Scores (userId, game1, game2) VALUES (%s, %s, %s)"

# for x, user in enumerate(users):
#     mycursor.execute(Q3, user)
#     lastId = mycursor.lastrowid
#     mycursor.execute(Q4, (lastId,) + userScores[x])

# db.commit()
# mycursor.execute(Q1)
# mycursor.execute(Q2)

# mycursor.executemany("INSERT INTO Users (name, username, password, emailAddress) VALUES (%s, %s, %s, %s)", users)
