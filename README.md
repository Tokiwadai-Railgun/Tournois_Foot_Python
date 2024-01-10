# Planification saison foot

**Application Shell (CLI)**

## Plugins utilisés
1 - InquirerPy(https://pypi.org/project/inquirerpy/) : pour les menus et les questions
2 - rich (https://pypi.org/project/rich/) : pour l'affichage des tableaux

## Fonctionnalités
Le programme permet de créer un planpour les matchs de foots à venir.
Il contient donc les menus suivants :
### 1 - Menu principal : Affiche le logo de l'application en ASCII,
* [ ] Affiche Classement
* [ ] Affiche le menu matchs 
* [ ] Affiche le menu équipes
* [ ] Affiche les pronostiques 

### 2 - Menu Classement : Voir les points des équipes actuelles 
*3points en cas de victoire , 1 points en cas de match nul et 0 en cas de défaite*\
* [ ] Affiche le classement

### 3 - Menu Matchs : Affiche les matchs (daily, all)
#### daily 
* [ ] Afficher les matchs de la journée -> id du match , Les deux équipes , date , heure , vainceurs et arbitres attitrés .
* [ ] saisir les résultats ->  choisir le match par son id, équipes , 
* [ ]
### 4 - Menu Staff : Permet de créer des membres du staff, de les modifier, de les supprimer et d'afficher les membres du staff par équipe
1 : Ajout d'un membre du staff : On renseigne le nom, le prénom, la date de naissance, le poste et l'équipe
2 : Modification d'un membre du staff : On peut modifier le nom, le prénom, la date de naissance, le poste et l'équipe

### 5 - Menu matchs : Permet de créer des matchs, de les modifier, de les supprimer et d'afficher les matchs par équipe
1 : Ajout d'un match : On renseigne les équipes, la date, le stade et les arbitres
2 : Modification d'un match, on peut modifier les équipes, la date, le stade et les arbitres
3 : Ajout du résultat d'un match : On renseigne le score et le gagnant, cette page affiche automatiquement les matchs passés sans résultats.

/!\ Chaque Menu affiche en dessous un menu de navgation pour se balader entre les différents menus. Il doit donc s'adapter à chaque menu pour n'afficher que les menus disponnible ou signaler sur quel menu on se trouve. (à voir si on peut pas mettre d'une certains couleur un élément du menu où simplement le différencier avec un caractère en plus)
