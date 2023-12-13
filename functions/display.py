# Importing modules
from InquirerPy import prompt
from rich.console import Console
from rich.table import Table

# This module is used to display table containing the necessary informations.


# First function: navigationMenu
def nagivationMenu():
    navigationMenu = [
        {"type": "list", "message": "Que voulez-vous faire ?", "name": "navigation", "choices": ["Ajouter une équipe", "Afficher les équipes", "Quitter"]},
    ]
    navigationAnswer = prompt(navigationMenu)
    if navigationAnswer["navigation"] == "Ajouter une équipe":
        addTeamMenu()
    elif navigationAnswer["navigation"] == "Afficher les équipes":
        displayTeammsMenu()
    elif navigationAnswer["navigation"] == "Quitter":
        exit()


# This function will simply display the menu of the application on launch.

def displayWelcomeMenu():
    # Defining the table
    table = Table()
    console = Console()
    print('''
            ___      _                                                               _    
    o O O  | _ )    (_)     ___    _ _     __ __    ___    _ _     _  _     ___     | |   
   o       | _ \    | |    / -_)  | ' \    \ V /   / -_)  | ' \   | +| |   / -_)    |_|   
  TS__[O]  |___/   _|_|_   \___|  |_||_|   _\_/_   \___|  |_||_|   \_,_|   \___|   _(_)_  
 {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_| """ | 
./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'
    ''')
    console.print(table)  

    # then we display the nagivation menu
    nagivationMenu()

# This function is meant to display the list of all teams in the database.
def displayTeammsMenu():
    table = Table()
    console = Console()
    columns = ["Rank", "Team Name", "Last Match", "Next Match"]
    rows = []
    for column in columns:
        table.add_column(column)
    print("Bienvenue :") # TODO: Add the logo in ASCII art
    console.print(table)  
    # Display the menu options

def addTeamMenu():
    table = Table()
    console = Console()
    columns = ["Rank", "Team Name", "Last Match", "Next Match"]
    rows = []
    for column in columns:
        table.add_column(column)
    print("Bienvenue :") # TODO: Add the logo in ASCII art
    console.print(table)  
    # Display the menu options
