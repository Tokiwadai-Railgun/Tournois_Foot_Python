# Database import
import mysql.connector
connexion_params = {
  'host': "localhost",
  'user': "root",
  'password': "Walendithas",
  'database': "tournoi"
}

with mysql.connector.connect(**connexion_params) as db:
  with db.cursor() as c:
    c.execute("SELECT * FROM equipe;")
    resultat = c.fetchall()
    for table in resultat:
      for field in table:
        print(field)
      print(table)
      #TODO: Do something
