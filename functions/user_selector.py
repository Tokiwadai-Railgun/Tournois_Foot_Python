
# This module is ued to display the login menu wich looks like a basic linux login whitout user interface.
# Only username and password. The password is hidden.

from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
import json

adminMenu = functions.admins.admin_menu

userFolder = "./datas/users.json"
userJson = json.load(open(userFolder))

adminName = userJson["admin"]["username"]
print(adminName)

def loginMenu():
    loginMenu = [
        {
            "type": "input",
            "message": "Username:",
            "name": "username"
        },
        {
            "type": "password",
            "message": "Password:",
            "name": "password"
        },
    ]
    return loginMenu

def login():
    loginAnswer = prompt(loginMenu())
    return loginAnswer

