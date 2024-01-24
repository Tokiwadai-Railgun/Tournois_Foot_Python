# Planification saison foot


## Installation : 
Simplement clone et ajouter les différentes bibliothèqes
concernant la basse de donnée elle est hébergée sur un VPS il n'y a donc pas besoin de la cloner

**Application Shell (CLI)**

## Plugins utilisés
1 - InquirerPy(https://pypi.org/project/inquirerpy/) : pour les menus et les questions
2 - rich (https://pypi.org/project/rich/) : pour l'affichage des tableaux \
2 - mysql-connector-python : pour la connection avec la base de donnée 

## Fonctionnalités
Le programme permet de créer un planpour les matchs de foots à venir.
Il contient donc les menus suivants :
### 1 - Menu principal : Affiche le logo de l'application en ASCII,
* [X] Affiche le menu Classement
* [X] Affiche le menu matchs 
* [X] Affiche le menu équipes
* [X] Affiche le menu pronostiques 

### 2 - Menu Classement : Voir les points des équipes actuelles 
*3points en cas de victoire , 1 points en cas de match nul et 0 en cas de défaite*\
* [X] Affiche le classement

### 3 - Menu Matchs : Affiche les matchs (daily, all)
#### daily 
* [X] Afficher les matchs de la journée -> id du match , Les deux équipes , date , heure , vainceurs et arbitres attitrés .
* [X] saisir les résultats ->  choisir le match par son id, équipes , 

### 4 - Menu équipes
* [X] Affiche les différentes équipes 
* [X] Saisir une nouvelle équipe

### 5 - Menu pronostiques : Permet d'afficher les pronostiques du tournois
*Permet aux utilisateurs de voter pour une équipe dans le top 3*\
* [X] Affiche le podium avec le nombre de vote pour tel équipe
* [X] Voter pour une équipe 

/!\ Chaque Menu affiche en dessous un menu de navgation pour se balader entre les différents menus. Il doit donc s'adapter à chaque menu pour n'afficher que les menus disponnible ou signaler sur quel menu on se trouve. (à voir si on peut pas mettre d'une certains couleur un élément du menu où simplement le différencier avec un caractère en plus)
