from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
# Import the display module
from functions.user_selector import login
from functions.admins.admins_menus import *

login()

table = Table(title = "People")
console = Console()

columns = ["Name", "Language"]
teamMembers = []
questions = [
    {"type": "input", "message": "What's your name:", "name": "name"},
    {
        "type": "list",
        "message": "What's your favourite programming language:",
        "choices": ["Go", "Python", "Rust", "JavaScript"],
    },
    {"type": "confirm", "message": "Confirm?"},
]


navigationMenu()

# Setup de la table avec données déjà présentes
for column in columns:
    table.add_column(column)
for teamMember in teamMembers:
    table.add_row(teamMember["name"], teamMember["fav_lang"])
