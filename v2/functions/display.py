# Importing modules
from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
import json


# Database import
import mysql.connector
connexion_params = {
  'host': "localhost",
  'user': "root",
  'password': "Walendithas",
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



def displayPlanning():
    table = Table()
    console = Console()
    columns = ["Date", "Premère équipe", "Seconde équipe", "Arbitre", "Pronostique" ]
    rows = []
    for column in columns:
        table.add_column(column)

    # Afficage du titre en ASCII art
    #
    # Affichage du tableau
    console.print(table)


def displayMatchHistory():
  table = Table()
  console = Console()
  columns = ["ID du match", "Date", "Premère équipe", "Seconde équipe", "Arbitre", "Score de la première équipe", "Score de la seconde équipe" ]
  for column in columns:
      table.add_column(column)

  # Afficage du titre en ASCII art
  with open("datas/matchs.json", "r") as openfile:
    # Reading from json file
    json_object = json.load(openfile)
    for key, value in json_object.items():
      table.add_row(key, value[2], value[0], value[1], value[5], value[3], value[4])

  # Affichage du tableau
  console.print(table)


def displayRank():
  table = Table()
  console = Console()
  columns = ["Classement", "Nom de l'équipe", "Nombre de points"]
  for column in columns:
    table.add_column(column)
   
    
    # Changing JSON to Mysql
    with open('datas/teams.json', 'r') as teamsJson:
      team_json_object = json.load(teamsJson)
      calculatePoints()
      # Afficher par ordre croissant
      donnees_tries = dict(sorted(team_json_object.items(), key=lambda item: int(item[1][2]), reverse = True))
      i = 1
      for _, value in donnees_tries.items():
        table.add_row(str(i), value[0], value[2])
        i += 1
  
          

  # Affichage du tableau
  console.print(table)

def calculatePoints():
  with open("datas/matchs.json", "r") as matchsJson:
    with open('datas/teams.json', 'r') as teamsJson:
      # Reading from json file
      matchs_json_object = json.load(matchsJson)
      teams_json_object = json.load(teamsJson)
      for key, value in matchs_json_object.items():
        if int(value[3]) == max(value[3], value[4]):
          teams_json_object[value[0]][2] = str( int(teams_json_object[value[0]][2]) + 3 )
        elif int(value[4]) == max(value[3], value[4]):
          teams_json_object[value[1]][2] = str( int(teams_json_object[value[1]][2]) + 3 )
        else :
          teams_json_object[value[0]][2] = str( int(teams_json_object[value[0]][2]) + 1 )
          teams_json_object[value[0]][2] = str( int(teams_json_object[value[0]][2]) + 1 )

# Calculate pronostics
def displayProno():
  table = Table()
  console = Console()
  columns = ["Nom de l'équipe", "Nombre de votes"]
  for column in columns:
    table.add_column(column)
  


  console.print(table)
  with open('datas/teams.json', 'r') as teamsJson:
    team_json_object = json.load(teamsJson)
    # Afficher par ordre croissant
    donnees_tries = dict(sorted(team_json_object.items(), key=lambda item: int(item[1][2])))
    for _, value in donnees_tries.items():
        table.add_row(value[0], value[3])

  console.print(table)
