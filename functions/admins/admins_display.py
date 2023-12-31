# Importing modules
from InquirerPy import prompt
from rich.console import Console
from rich.table import Table



# This module is used to display table containing the necessary informations.
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

# This function is meant to display the list of all teams in the database.
def displayTeams():
    table = Table()
    console = Console()
    columns = ["Rank", "Nom d'équipe", "Dernier match", "Prochain match"]
    rows = []
    for column in columns:
        table.add_column(column)

    # Afficage du titre en ASCII art

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
    columns = ["Date", "Premère équipe", "Seconde équipe", "Arbitre", "Résultat" ]
    rows = []
    for column in columns:
        table.add_column(column)

    # Afficage du titre en ASCII art
    #
    # Affichage du tableau
    console.print(table)
