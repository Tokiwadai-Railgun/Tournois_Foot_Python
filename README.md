# Planification saison foot

**Application Shell (CLI)**

**Plugins utilisés**
1 - InquirerPy(https://pypi.org/project/inquirerpy/) : pour les menus et les questions
2 - rich (https://pypi.org/project/rich/) : pour l'affichage des tableaux

**Fonctionnalités**
Le programme permet de créer un planpour les matches de foots à venir.
Il contient donc les menus suivants :
#### 1 - Menu principal : Affiche le logo de l'application en ASCII,

#### 2 - Menu équipes : Permet de créer des équipes, de les modifier, de les supprimer et d'afficher les équipes par rank
#### 2 - 
1 : Ajout d'une équipe : On renseigne les joueurs, le nom et l'entraineur
2 : Modification d'une équipe : On peut modifier le nom, l'entraineur et les joueurs

#### 3 - Menu joueurs : Permet de créer des joueurs, de les modifier, de les supprimer et d'afficher les joueurs par équipe
1 : Ajout d'un joueur : On renseigne le nom, le prénom, la date de naissance, le poste et l'équipe
2 : Modification d'un joueur : On peut modifier le nom, le prénom, la date de naissance, le poste et l'équipe

#### 4 - Menu Staff : Permet de créer des membres du staff, de les modifier, de les supprimer et d'afficher les membres du staff par équipe
1 : Ajout d'un membre du staff : On renseigne le nom, le prénom, la date de naissance, le poste et l'équipe
2 : Modification d'un membre du staff : On peut modifier le nom, le prénom, la date de naissance, le poste et l'équipe

#### 5 - Menu matches : Permet de créer des matches, de les modifier, de les supprimer et d'afficher les matches par équipe
1 : Ajout d'un match : On renseigne les équipes, la date, le stade et les arbitres
2 : Modification d'un match, on peut modifier les équipes, la date, le stade et les arbitres
3 : Ajout du résultat d'un match : On renseigne le score et le gagnant, cette page affiche automatiquement les matches passés sans résultats.

/!\ Chaque Menu affiche en dessous un menu de navgation pour se balader entre les différents menus. Il doit donc s'adapter à chaque menu pour n'afficher que les menus disponnible ou signaler sur quel menu on se trouve. (à voir si on peut pas mettre d'une certains couleur un élément du menu où simplement le différencier avec un caractère en plus)
