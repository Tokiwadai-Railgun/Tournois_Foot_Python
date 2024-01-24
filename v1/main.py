from InquirerPy import prompt
from rich.console import Console
from rich.jupyter import display
from rich.table import Table
# Import the display module
from functions.display import *
from functions.menus import navigationMenu

loggedIn = False
user = ""

navigationMenu()
