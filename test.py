import mysql.connector
connevtion_params = {
  'host' : "localhost",
  'user': "root",
  "password" : "Walendithas",
  "database" : "tournoi"
}

with mysql.connector.connect(**connevtion_params) as db:
  with db.cursor() as c:
    c.execute("INSERT INTO equipe (nom, ville, nb_points) VALUES ("B", "B", 0)")
    db.commit()
