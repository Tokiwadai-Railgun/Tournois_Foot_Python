# Importing modules
from InquirerPy import prompt
from InquirerPy.validator import EmptyInputValidator
import time
import json
import random

# Database import
import mysql.connector
connexion_params = {
  'host': "85.215.156.4",
  'user': "tortue",
  'password': "tkt",
  'database': "tournoi"
}

teamms = { "0" : ["nom", "ville", 0]}

# custome modules
from functions.display import *

# There will be 2 types of menus: 
# First the nagivation menu, he's alone in this category and will only be used to switch between the other menus.
# Then the action menus, they will be used to display the informations and to interact with the user.

# This is the navigation menu
def navigationMenu():
    navigationMenu = [
        {
            "type": "list",
            "message": "Que voulez-vous faire ?", 
            "name": "navigation", 
            "choices": [
                "Voir le classement", 
                "Voir les matchs", 
                "Voir les équipes", 
                "Voir les pronostiques", 
                "Quitter"
            ]
        },
    ]

    displayWelcomeMenu()

    navigationAnswer = prompt(navigationMenu)

    match navigationAnswer["navigation"] :
        case "Voir les équipes":
            teamsActionMenu()
        case "Voir les matchs":
            matchHistoryMenu()
        case "Voir le classement":
          teamRankMenu()
        case "Voir les pronostiques":
          pronoMenu()
        case "Quitter":
            exit()


# And now the action menus


# -------------- TEAMS MENU --------------
def teamsActionMenu():
    actionsMenu = [
        {
            "type": "list", 
            "message": "Que voulez-vous faire ?", 
            "name": "action", 
            "choices": [
                "Ajouter une équipe", 
                "Modifier une équipe",
                "Changer de Menu",
                "Quitter"
            ]
        },
    ]

    displayTeams()

    response = prompt(actionsMenu)
    match(response["action"]) : 
        case "Ajouter une équipe":
            addTeam()
            # Créer une fonction pour ajouter une équipe dans un fichier JSON
        case "Modifier une équipe":
          editTeam()
            # Créer une fonction pour modifier une équipe dans un fichier JSON
        case "Changer de Menu" :
            navigationMenu()
        case "Quitter":
            exit()
    # Display the menu options

def addTeam() : 
    # Ask for user input and stock it in a dictionnary
    questions = [
        {
            "type": "input",
            "message": "Quel est le nom de l'équipe ?",
            "name": "teamName"
        },
        {
            "type" : "input",
            "message" : "d'ou viens l'équipe",
            "name" : "teamCity"
        },
    ]

    answer = prompt(questions)
    with open("datas/teams.json", 'r') as outfile:
      teams = json.load(outfile)

      teamValues = []
      for key, value in answer.items():
        teamValues.append(value)
      teamValues.append("0") # Correspond au nombre de votes pour les pronostiques, vide par défaut
      newTeam = {answer["teamName"] : teamValues }
      teams.update(newTeam)

    #TODO: Write in mysql instead of json
    with mysql.connector.connect(**connexion_params) as db:
      with db.cursor() as c:
        teamName = teamValues[0]
        teamCity = teamValues[1]
        teamScore = teamValues[2]
        req = f"""INSERT INTO equipe (name, ville) VALUES ('{teamName}', '{teamCity}')"""
        c.execute(req)
        db.commit()
    print("L'équipe a bien été ajoutée !")
    teamsActionMenu()
    # TODO: Créer une fonction pour ajouter une équipe dans un fichier JSON


def editTeam(): 
  # Ask for user input and stock it in a dictionnary
  newTeam = {
      "teamName": "",
      "teamMembers": [],
      "teamRank": "",
      "teamLastMatch": "",
      "teamNextMatch": ""
  }
  print("Modification d'une équipe")
  # First get all teams names
  with mysql.connector.connect(**connexion_params) as db:
    with db.cursor() as c:
      c.execute("SELECT name from equipe")
      teams = c.fetchall()

      teamsNames = []
      for team in teams:
        teamsNames.append(team[0])
  teamSelectionQuestions = [
    {
      "type": "fuzzy",
      "message" : "Sélectionner une équipe",
      "choices": teamsNames,
    },
  ]
  modifierQuestions = [
    {
      "type": "input",
      "message": "Quel est le nom de l'équipe ? (laisser vide si inchangé)",
      "name": "name"
    },
    {
      "type" : "input",
      "message" : "D'où viens l'équipe ? (laisser vide si inchangé)",
      "name" : "ville"
    }
  ]

  choosenTeam = prompt(teamSelectionQuestions)

  selectedTeamName = choosenTeam[0]
  modifications = prompt(modifierQuestions)
  # First we check each response and set the correct values 
  with mysql.connector.connect(**connexion_params) as db :
    with db.cursor() as c:

      for key, value in modifications.items():
        if value == "" : 
          c.execute(f"SELECT {key} FROM equipe WHERE name = '{selectedTeamName}'") 
          value = c.fetchall()[0][0]


      # Then we push to the database
      c.execute(f"UPDATE equipe SET name = '{modifications['name']}', ville = '{modifications['ville']}' WHERE name ='{selectedTeamName}'")
      db.commit()

  # Now we upate the database  
  print("L'équipe a bien été modifiée !")
  # TODO: Faire une fonction permettant de modifier une équipe dans un fichier JSON
  teamsActionMenu()

def deleteTeam():
    # Ask for user input and stock it in a dictionnary
    team = {
        "type": "input",
        "message": "Quel est le nom de l'équipe ?",
        "name": "teamName"
    }

    print("Suppression d'une équipe")
    answer = prompt(team)
    # TODO: Créer une fonction pour supprimer une équipe dans un fichier JSON avec comme argument le nom de cette dernière
    teamsActionMenu()

# -------------- MATCH HISTORY --------------
def matchHistoryMenu():
    # Display the menu options
    actions = [{ 
        "type": "list", 
        "message": "Que voulez-vous faire ?", 
        "name": "action", 
        "choices": [
            "Ajouter un match",
            "Mettre à jours les scores d'un match",
            "Changer de Menu", 
            "Quitter"
        ]
    }]

    displayMatchHistory()
    response = prompt(actions)
    match response["action"] :
      case "Ajouter un match" : 
          addMatch()
      case "Mettre à jours les scores d'un match":
        editMatchScore()
      case "Changer de Menu" :
          navigationMenu()
      case "Quitter":
          exit()

def addMatch():
  with mysql.connector.connect(**connexion_params) as db :
    with db.cursor() as c:
      c.execute("SELECT name FROM equipe")
      teamNames = [] 
      for team in c.fetchall():
        teamNames.append(team[0])

      arbitresNames = []
      c.execute("SELECT nom FROM arbitre")
      for arbitre in c.fetchall():
        arbitresNames.append(arbitre[0])

      questions = [
        {
          "type": "fuzzy",
          "message": "Quel est le nom la première équipe ?",
          "name": "teamName1",
          "choices": teamNames
        },
        {
          "type" : "fuzzy",
          "message" : "Quel est le nom de la deuxième équipe",
          "name" : "teamName2",
          "choices": teamNames
        },
        {
          "type" : "input",
            "message" : "Quand a lieu de match ?",
            "name" : "matchDate"
        }, 
        {
          "type" : "number",
          "message" : "Quel est le score de la première équipe ?",
          "min_allowed": 0,
          "validate": EmptyInputValidator(),
          "name" : "score1"
        }, 
        {
          "type" : "number",
          "message" : "Quel est le score de la deuxième équipe ?",
          "min_allowed": 0,
          "validate": EmptyInputValidator(),
          "name" : "score2"
        }, 
        {
          "type" : "fuzzy",
          "message" : "Quel est le nom de l'arbitre ?",
          "name" : "arbitre",
          "choices": arbitresNames
        }, 
      ]

      answer = prompt(questions)
      
      # First we need to get the two teams IDs 
      c.execute(f"SELECT idEqp FROM equipe WHERE name = '{answer['teamName1']}'")
      firstTeamId = c.fetchall()[0][0]
      c.execute(f"SELECT idEqp FROM equipe WHERE name = '{answer['teamName2']}'")
      secondTeamId = c.fetchall()[0][0]
      c.execute(f"SELECT idArb FROM arbitre WHERE nom = '{answer['arbitre']}'")
      arbitreId = c.fetchall()[0][0]

      c.execute(f"INSERT INTO matchs (idEqp1, idEqp2, dateMatch, score1, score2, arbitre) VALUES ('{firstTeamId}', '{secondTeamId}', '{answer['matchDate']}', '{answer['score1']}', '{answer['score2']}', '{arbitreId}')")
      db.commit()

  

  with open("datas/matchs.json", 'r') as outfile:
    matchs = json.load(outfile)

    matchValues = []
    for key, value in answer.items():
      matchValues.append(value)
    newMatch = {str(random.randint(1, 999)): matchValues }
    matchs.update(newMatch)

  with open("datas/matchs.json", "w") as outfile:
    json.dump(matchs, outfile)

  print("L'équipe a bien été ajoutée !")
  matchHistoryMenu()


def editMatchScore():
  # Prompt the user to choose a match with it ID
  matchsIds = []
  with mysql.connector.connect(**connexion_params) as db:
    with db.cursor() as c:
      c.execute("SELECT idMatch FROM matchs")
      for match in c.fetchall():
        matchsIds.append(match[0]) # On ajoute l'Id du match dans la table pour les afficher par la suite

      
      questions = [
        {
          "type": "fuzzy",
          "message" : "Sélectionner un match",
          "choices": matchsIds 
        }
      ]

      editingMatch = prompt(questions)[0]

      # Now we prompt the score of the two new teams
      scoreQuestions = [
        {
            "type" : "number",
            "message" : "Quel est le score de la première équipe ?",
            "min_allowed": 0,
            "validate": EmptyInputValidator(),
            "name" : "score1"
        }, 
        {
            "type" : "number",
            "message" : "Quel est le score de la seconde équipe ?",
            "min_allowed": 0,
            "validate": EmptyInputValidator(),
            "name" : "score2"
        }, 
      ]
      newScore = prompt(scoreQuestions)

      c.execute(f"UPDATE matchs SET score1 = {newScore['score1']}, score2 = {newScore['score2']} WHERE idMatch = {editingMatch};")
      db.commit()


  matchHistoryMenu()

# ------------------- Classement Menu ---------------------
def teamRankMenu():
  actions = [{ 
      "type": "list", 
      "message": "Que voulez-vous faire ?", 
      "name": "action", 
      "choices": [
          "Changer de Menu", 
          "Quitter"
      ]
  }]
  
  displayRank()
  response = prompt(actions)
  match response["action"] :
    case "Changer de Menu" :
        navigationMenu()
    case "Quitter":
        exit()


# Pronostics
def pronoMenu():
  actions = [{ 
    "type": "list", 
    "message": "Que voulez-vous faire ?", 
    "name": "action", 
    "choices": [
        "Voter",
        "Changer de Menu", 
        "Quitter"
    ]
  }]

  displayProno()
  response = prompt(actions)
  match response["action"] :
    case "Voter":
      vote()
    case "Changer de Menu" :
        navigationMenu()
    case "Quitter":
        exit()

def vote():
  with mysql.connector.connect(**connexion_params) as db:
    with db.cursor() as c:
      c.execute("SELECT name FROM equipe;")

      teamsIds = []
      for team in c.fetchall():
        teamsIds.append(team[0])

      questions = [
        {
          "type": "fuzzy",
          "message" : "Sélectionner la première équipe",
          "choices": teamsIds 
        },
        {
          "type": "fuzzy",
          "message" : "Sélectionner la deuxième équipe",
          "choices": teamsIds 
        },
        {
          "type": "fuzzy",
          "message" : "Sélectionner la troisième équipe",
          "choices": teamsIds 
        },
      ]

      votedTeams = prompt(questions)
      for _, team in votedTeams.items():
        c.execute(f"UPDATE equipe SET pronosticVote = pronosticVote + 1 WHERE name = '{team}'")
      db.commit()

  pronoMenu()
