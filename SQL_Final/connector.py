import mysql.connector


connection = mysql.connector.connect(host="localhost", user = "root", password = "Dawn1234")

#print("\nYou are now connected!")
#print(f"{connection}\n")

def createTable():
    cursor = connection.cursor()
    cursor.execute("USE menagerie")
    #cursor.execute("SHOW DATABASES")
    cursor.execute("CREATE TABLE pet(name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);")
    

    struct = ("DESCRIBE pet")
    cursor.execute(struct)


    for struct in cursor:
        print(f"{struct}")

#createTable()

def insertData():
    cursor = connection.cursor()
    cursor.execute("USE menagerie")
    cursor.execute("INSERT INTO pet (name,owner,species,sex,birth,death) VALUES \
    ('Fluffy','Harold', 'cat', 'f','1993-02-04',NULL),\
    ('Claws','Gwen', 'cat', 'm','1994-03-17',NULL),\
    ('Buffy','Harold', 'dog', 'f','1989-05-13',NULL),\
    ('Fang','Benny', 'dog', 'm','1990-08-27',NULL),\
    ('Bowser','Diane', 'dog', 'm','1979-08-31','1995-07-29'),\
    ('Chripy','Gwen', 'bird', 'f','1998-09-11',NULL),\
    ('Whistler','Gwen', 'bird', NULL ,'1997-12-09',NULL),\
    ('Slim','Benny', 'snake', 'm','1996-04-29',NULL),\
    ('Puffball','Diane', 'hamster', 'f','1999-03-30',NULL)")
    connection.commit()
    cursor.execute("SELECT * FROM pet")

    for struct in cursor:
        print(f"{struct}")

#insertData()

def dogQuery():
    cursor = connection.cursor()
    cursor.execute("USE menagerie")
    cursor.execute("SELECT * FROM pet WHERE sex = 'f' AND species = 'dog';")
    dog = cursor.fetchall()

    for i in dog:
        print(i[0], i[1], i[2], i[3], i[4], i[5])

#dogQuery()

def nameBirth():
    cursor = connection.cursor()
    cursor.execute("USE menagerie")
    cursor.execute("SELECT * FROM pet;")
    dog = cursor.fetchall()

    for i in dog:
        print(i[0], i[4])

#nameBirth()

def pets():
    cursor = connection.cursor()
    cursor.execute("USE menagerie")
    cursor.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner;")
    dog = cursor.fetchall()

    for i in dog:
        print(i[0], i[1])

#pets()

def month():
    cursor = connection.cursor()
    cursor.execute("USE menagerie")
    cursor.execute("SELECT name, birth, MONTH(birth) FROM pet;")
    dog = cursor.fetchall()

    for i in dog:
        print(i[0], i[1], i[2])

month()