# Importing modules
from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
import json


# Database import
import mysql.connector
connexion_params = {
  'host': "85.215.156.4",
  'user': "tortue",
  'password': "tkt",
  'database': "tournoi"
}

# This module is used to display table containing the necessary informations.
def displayWelcomeMenu():
    # Defining the table
    print('''
            ___      _                                                               _    
    o O O  | _ )    (_)     ___    _ _     __ __    ___    _ _     _  _     ___     | |   
   o       | _ \\    | |    / -_)  | ' \\    \\ V /   / -_)  | ' \\   | +| |   / -_)    |_|   
  TS__[O]  |___/   _|_|_   \\___|  |_||_|   _\\_/_   \\___|  |_||_|   \\_,_|   \\___|   _(_)_  
 {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_| """ | 
./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'
    ''')

# This function is meant to display the list of all teams in the database.
def displayTeams():
    table = Table()
    console = Console()
    columns = ["Rank", "Nom d'équipe", "Ville", "Nombre de points"]

    #TODO: connect to mydsl db then save it
    
    for column in columns:
        table.add_column(column)

    with mysql.connector.connect(**connexion_params) as db:
      with db.cursor() as c:
        c.execute("SELECT * FROM equipe;")
        teams = c.fetchall() 
        for team in teams:
          table.add_row("0", team[1], team[2], str(team[3]))

    # Affichage du tableau
    console.print(table)  
    # Display the menu options

def displayMatchHistory():
  table = Table()
  console = Console()
  columns = ["ID du match", "Date", "Premère équipe", "Seconde équipe", "Arbitre", "Score de la première équipe", "Score de la seconde équipe" ]
  for column in columns:
      table.add_column(column)


  # Store in the Database
  with mysql.connector.connect(**connexion_params) as db:
    with db.cursor() as c:
      c.execute("SELECT * FROM matchs;")
      matchs = c.fetchall() 
      for match in matchs:
        console.log(match)
        # Get the two team names
        c.execute(f"SELECT name FROM equipe WHERE idEqp = '{match[1]}'")
        firstTeamName = c.fetchall()[0][0]
        c.execute(f"SELECT name FROM equipe WHERE idEqp = '{match[2]}'")
        secondTeamName = c.fetchall()[0][0]

        c.execute(f"SELECT nom FROM arbitre WHERE idArb = '{match[8]}'")
        arbitreName = c.fetchall()[0][0]
        table.add_row(str(match[0]), str(match[3]), str(firstTeamName), str(secondTeamName), str(arbitreName), str(match[4]), str(match[5]))
      
  # Affichage du tableau
  console.print(table)


def displayRank():
  table = Table()
  console = Console()
  columns = ["Classement", "Nom de l'équipe", "Nombre de points"]
  for column in columns:
    table.add_column(column)
  calculatePoints() 

  # Now we calculate the rALTER TABLE equipe ALTER COLUMN pronosticVote SET DEFAULT 0oank of each teams
  with mysql.connector.connect(**connexion_params) as db:
    with db.cursor() as c:
      c.execute("SELECT name, nb_points FROM equipe")
      result = c.fetchall()
      # Sorting the data based on nb_points
      sorted_data = sorted(result, key=lambda x: x[1], reverse=True)

      # Creating a dictionary with team names as keys and nb_points as values
      donnees_tries = {team[0]: team[1] for team in sorted_data}

      i = 1
      for name, score in donnees_tries.items():
        table.add_row(str(i), name, str(score))
        i+=1

  # Affichage du tableau
  console.print(table)

def calculatePoints():
  # We need to get throught each match and add a point to each teams on a win
  with mysql.connector.connect(**connexion_params) as db : 
    with db.cursor() as c:
      # First we set all values to 0 
      c.execute("UPDATE equipe SET nb_points = 0")

      # Then we find the winner of each match and add 3 to the number of points
      c.execute("SELECT idEqp1, idEqp2, score1, score2 FROM matchs")
      matchResults = c.fetchall()
      for matchResult in matchResults :
        firstTeamId = matchResult[0]
        firstTeamScore = matchResult[2]
        secondTeamId = matchResult[1]
        secondTeamScore = matchResult[3]

        if (firstTeamScore > secondTeamScore):
          print("Adding points to first team")
          c.execute(f"UPDATE equipe SET nb_points = nb_points + 3 WHERE idEqp = {firstTeamId}")
        elif (secondTeamScore > firstTeamScore):
          print("Adding points to second team")
          c.execute(f"UPDATE equipe SET nb_points = nb_points + 3 WHERE idEqp = {secondTeamId}")
        else:
          print("Adding points to booth teams")
          c.execute(f"UPDATE equipe SET nb_points = nb_points + 1 WHERE idEqp = {secondTeamId}")
          c.execute(f"UPDATE equipe SET nb_points = nb_points + 1 WHERE idEqp = {firstTeamId}")

        # Now we calculate the rank for each teams

      db.commit()
# Calculate pronostics
def displayProno():
  table = Table()
  console = Console()
  columns = ["Nom de l'équipe", "Nombre de votes"]
  for column in columns:
    table.add_column(column)

  with mysql.connector.connect(**connexion_params) as db:
    with db.cursor() as c:
      c.execute("SELECT name, pronosticVote from equipe")
      teamsRanks = c.fetchall()
      # get all in a single array instead of tuple
      donnees_tries = dict(sorted(teamsRanks, key=lambda item: item[1], reverse=True))
      print(donnees_tries)
      for key, value in donnees_tries.items():
          table.add_row(key, str(value))
      console.print(table)
