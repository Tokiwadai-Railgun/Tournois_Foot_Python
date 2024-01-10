# Importing modules
from InquirerPy import prompt
import json


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
                "Voir les matches", 
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
        case "Voir le planning":
            planningActionMenu()
        case "Voir les anciens matches":
            matchHistoryMenu()
        case "Voir le staff":
            print("Staff")
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
                "Supprimer une équipe",
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
            print("Modification d'une équipe")
            # Créer une fonction pour modifier une équipe dans un fichier JSON
        case "Supprimer une équipe":
            print("Suppression d'une équipe")
            # Créer une fonction pour supprimer une équipe dans un fichier JSON
        case "Changer de Menu" :
            navigationMenu()
        case "Quitter":
            exit()
    # Display the menu options

def addTeam() : 
    # Ask for user input and stock it in a dictionnary
    newTeam = {
        "teamName": "",
        "teamMembers": [],
        "teamRank": "",
        "teamLastMatch": "",
        "teamNextMatch": ""
    }
    print("Ajout d'une équipe")
    questions = [
        {
            "type": "input",
            "message": "Quel est le nom de l'équipe ?",
            "name": "teamName"
        },
        {
            "type" : "input",
            "message" : "Quel est le rang de l'équipe ?",
            "name" : "teamRank"
        },
        {
            "type" : "input",
            "message" : "Quand a été le dernier match de l'équipe ? (JJ/MM/AAAA)",
            "name" : "teamLastMatch"
        }, 
        {
            "type": "input",
            "message": "Quand sera le prochain match de l'équipe ? (JJ/MM/AAAA)",
            "name": "teamNextMatch"
        }
    ]

    answer = prompt(questions)
    for key, value in answer.items():
        newTeam[key] = value
    jsonVer = json.dumps(newTeam, indent=4)
    with open("datas/teams.json", "w") as outfile:
      outfile.write(jsonVer)

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
    questions = [
        {
            "type": "input",
            "message": "Quel est le nom de l'équipe ?",
            "name": "teamName"
        },
        {
            "type" : "input",
            "message" : "Quel est le rang de l'équipe ? [\"disc\" si discalifiée]",
            "name" : "teamRank"
        },
        {
            "type" : "input",
            "message" : "Quand a été le dernier match de l'équipe ? (JJ/MM/AAAA)",
            "name" : "teamLastMatch"
        }, 
        {
            "type": "input",
            "message": "Quand sera le prochain match de l'équipe ? (JJ/MM/AAAA ) [\"none\" si aucun]",
            "name": "teamNextMatch"
        }
    ]
    answer = prompt(questions)
    for key, value in answer.items():
        newTeam[key] = value
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

# -------------- PLANNING MENU --------------
def planningActionMenu():
    displayPlanning()
    # Display the menu options

    actions = [{ 
        "type": "list", 
        "message": "Que voulez-vous faire ?", 
        "name": "action", 
        "choices": [
            "Ajouter un match", 
            "Modifier un match", 
            "Supprimer un match", 
            "Changer de Menu", 
            "Quitter"
        ]
    }]
    response = prompt(actions)

    match response["action"] :
        case "Ajouter un match":
            matchAdd()
        case "Modifier un match":
            print("Modification d'un match")
            # Créer une fonction pour modifier un match dans un fichier JSON
        case "Supprimer un match":
            print("Suppression d'un match")
            # Créer une fonction pour supprimer un match dans un fichier JSON
        case "Changer de Menu" :
            navigationMenu()


def matchAdd():
    # Ask for user input and stock it in a dictionnary
    newMatch = {
        "matchDate": "",
        "matchTeam1": "",
        "matchTeam2": "",
        "matchArbitre": ""
    }
    print("Ajout d'un match")

    questions = [
        {
            "type": "input",
            "message": "Quand est le match ? (JJ/MM/AAAA)",
            "name": "matchDate"
        },
        {
            "type": "input",
            "message": "Quelle est la première équipe ?",
            "name": "matchTeam1"
        },
        {
            "type": "input",
            "message": "Quelle est la deuxième équipe ?",
            "name": "matchTeam2"
        },
        {
            "type": "input",
            "message": "Quel est le nom de l'arbitre ?",
            "name": "matchArbitre"
        },
    ]
    
    answers = prompt(questions)

    for key, value in answers.items():
        newMatch[key] = value

    # TODO: Créer une fonction pour ajouter un match dans un fichier JSON
    print("Le match a bien été ajouté !")

    planningActionMenu()

def matchEdit():
    match = {
        "matchDate": "",
        "matchTeam1": "",
        "matchTeam2": "",
        "matchArbitre": ""
    }
   
    # Ask for user input and stock it in a dictionnary
    questions = [
        {
            "type": "input",
            message: "Quand est le match ? (JJ/MM/AAAA)",
            name: "matchDate"
        },
        {
            "type": "input",
            message: "quelle est la première équipe ?",
            name: "matchTeam1"
        },
        {
            "type": "input",
            message: "quelle est la seconde équipe ?",
            name: "matchTeam2"
        },
        {
            "type": "input",
            message: "quelle est la seconde équipe ?",
            name: "matchArbitre"
        },
    ]

    anwser = prompt(questions)
    for key, value in anwser.items():
        match[key] = value

    # TODO: Créer une fonction pour modifier un match dans un fichier JSON
    print("Modification d'un match")
    planningActionMenu()

def matchDelete():
    # Ask for user input and stock it in a dictionnary
    match = {
        "type": "input",
        "message": "Quel est le nom du match ?",
        "name": "matchName"
    }
    print("Suppression d'un match")
    # TODO: Créer une fonction pour supprimer un match dans un fichier JSON avec comme argument le nom de cette dernière
    answer = prompt(match)

    planningActionMenu()

# -------------- MATCH HISTORY --------------
def matchHistoryMenu():
    # Display the menu options
    actions = [{ 
        "type": "list", 
        "message": "Que voulez-vous faire ?", 
        "name": "action", 
        "choices": [
            "Changer de Menu", 
            "Quitter"
        ]
    }]

    displayMatchHistory()
    response = prompt(actions)
    match response["action"] :
        case "Changer de Menu" :
            navigationMenu()
        case "Quitter":
            exit()
