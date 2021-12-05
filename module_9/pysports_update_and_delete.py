# Marlene Fuller
#CSD310-352A Database Development and Use (2221-DD)
#Module 9
#Assignment  Module 9.3
#Assignment: PySports: Update & Deletes

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
   
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    

    sql = "INSERT INTO player (first_name, last_name, team_id) VALUES (%s, %s, %s)"
    val = ("Smeagol", "Shire Folk", 1)
    cursor.execute(sql, val)

    db.commit()

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player inner join team on player.team_id = team.team_id")

    players = cursor.fetchall()

    print("\n -- DISPLAYING PLAYER RECORDS AFTER INSERT -- ")

    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))   
      
    cursor.execute("update player set team_id = 2,first_name = 'Gollum',last_name = 'Ring Stealer' WHERE first_name='Smeagol'")    
   
    db.commit()

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player inner join team on player.team_id = team.team_id")

    players = cursor.fetchall()

    print("\n -- DISPLAYING PLAYER RECORDS AFTER UPDATE -- ")

    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))   



    cursor.execute("delete from player where first_name='Gollum'")    
   
    db.commit()

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player inner join team on player.team_id = team.team_id")

    players = cursor.fetchall()

    print("\n -- DISPLAYING PLAYER RECORDS AFTER DELETE -- ")

    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))   


  
    input("\n\n Press any key to continue... ")

    

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist.")

    else:
        print(err)
    
finally:
    db.close()
