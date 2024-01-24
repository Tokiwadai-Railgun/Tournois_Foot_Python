donnees = {"254": ["PSG", "Paris", "1"], "468": ["OM", "Marseilles", "10"], "410": ["OL", "Lyon", "0"]}

# Tri du dictionnaire par points (troisième élément de chaque liste)
donnees_tries = dict(sorted(donnees.items(), key=lambda item: int(item[1][2]), reverse = True))

print(donnees_tries)
