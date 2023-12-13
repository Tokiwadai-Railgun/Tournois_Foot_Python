# Planification saison foot

**Application Shell (CLI)**

**Plugins utilisés**
1 - InquirerPy(https://pypi.org/project/inquirerpy/) : pour les menus et les questions
2 - rich (https://pypi.org/project/rich/) : pour l'affichage des tableaux

**Fonctionnalités**
Le programme permet de créer un planning pour les matches de foots à venir.
Il doit donc untégrer différents affichages :
1 - Affichage équipes
2 - Affichage des prochains matches
3 - Affichage des membres du staff
4 - Affichage des derniers mathes

Pour regrouper tout ça on va donc créer X Affichages :
1 - Menu principal : Affiche le logo de l'application en ASCII,
2 - Menu équipes : le classement des équipes avec leur rank, leur nom, la date de leur dernier match et la date de leur prochain ( affiche "éliminée" si l'équipe est éliminée)
3 - Menu planning : Affiche les prochains matches, avec les deux équipes et la date du match.
4 - Menu résultats : Affiche le résultat des derniers matches avec la date, le score, le gagnant, les équipes et les arbitres.

/!\ Chaque Menu affiche en dessous un menu de navgation pour se balader entre les différents menus. Il doit donc s'adapter à chaque menu pour n'afficher que les menus disponnible ou signaler sur quel menu on se trouve. (à voir si on peut pas mettre d'une certains couleur un élément du menu où simplement le différencier avec un caractère en plus)
