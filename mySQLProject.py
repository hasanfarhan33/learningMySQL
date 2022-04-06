import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="hasanfarhan33",
    password="Farhan@1998",
    database="rezoAiProjectDatabase"
)

mycursor =  db.cursor()
# mycursor.execute("CREATE DATABASE rezoAiProjectDatabase")

# DROPPING THE TABLES
# mycursor.execute("DROP TABLE entityProperties")
# mycursor.execute("DROP TABLE summaryData")

# TODO: FIX CURRENT TIMESTAMP ON UPDATE AND DEFAULT CHARSET
# mycursor.execute("CREATE TABLE entityProperties (id INT(11) NOT NULL AUTO_INCREMENT, "
#                  "modelName VARCHAR(50) NOT NULL, "
#                  "fieldName VARCHAR(50) DEFAULT NULL, "
#                  "entityName VARCHAR(45) DEFAULT NULL,"
#                  "PRIMARY KEY(`id`),"
#                  "UNIQUE KEY `id_UNIQUE`(`id`),"
#                  "UNIQUE KEY `field_model_uq`(`modelName`, `fieldName`))"
#                  "ENGINE=InnoDB "
#                  "AUTO_INCREMENT=14")

mycursor.execute("CREATE TABLE summaryData (id INT(11) NOT NULL, "
                 "modelName VARCHAR(45) NOT NULL, "
                 "sessionId VARCHAR(50) NOT NULL,"
                 "funnelState VARCHAR(500) DEFAULT NULL,"
                 "intentJourney VARCHAR(100) DEFAULT NULL, "
                 "message text,"
                 "nonPredFirstMessage VARCHAR(150) DEFAULT NULL,"
                 "handoverMessage VARCHAR(150) DEFAULT NULL,"
                 "intentMessage VARCHAR(150) DEFAULT NULL,"
                 "startAt timestamp NULL DEFAULT NULL,"
                 "endAt timestamp NULL DEFAULT NULL,"
                 "lastUpdateAt timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,"
                 "cdr float DEFAULT NULL,"
                 "handover TINYINT(1) DEFAULT NULL,"
                 "handoverDesc VARCHAR(45) DEFAULT NULL,"
                 "recURL VARCHAR(200) DEFAULT NULL,"
                 "qcType VARCHAR(45) DEFAULT NULL,"
                 "length int(5) DEFAULT NULL,"
                 "silenceCount int(3) DEFAULT NULL,"
                 "journeyState VARCHAR(3) DEFAULT NULL,"
                 "g1 VARCHAR(45) DEFAULT NULL,"
                 "g2 VARCHAR(45) DEFAULT NULL,"
                 "g3 VARCHAR(45) DEFAULT NULL,"
                 "g4 VARCHAR(45) DEFAULT NULL,"
                 "g5 VARCHAR(45) DEFAULT NULL,"
                 "g6 VARCHAR(45) DEFAULT NULL,"
                 "g7 VARCHAR(45) DEFAULT NULL,"
                 "g8 VARCHAR(45) DEFAULT NULL,"
                 "g9 VARCHAR(45) DEFAULT NULL,"
                 "g10 VARCHAR(45) DEFAULT NULL,"
                 "userId VARCHAR(45) DEFAULT NULL,"
                 "tag1 VARCHAR(45) DEFAULT NULL,"
                 "tag2 VARCHAR(45) DEFAULT NULL,"
                 "comment VARCHAR(50) DEFAULT NULL,"
                 "PRIMARY KEY(`id`),"
                 "UNIQUE KEY `id_UNIQUE`(`id`),"
                 "KEY `modelName`(`modelName`),"
                 "KEY `startAt`(`startAt`),"
                 "KEY `endAt`(`endAt`),"
                 "KEY `lastUpdatedAt`(`lastUpdatedAt)) "
                 "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4")