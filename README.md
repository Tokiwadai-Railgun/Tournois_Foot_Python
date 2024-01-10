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
* [ ] Afficher les matches des autres jours dans un autre tableau

### 4 - Menu équipes
* [ ] Affiche les différentes équipes -> Nom, score
* [ ] Affiche les différentes équipes 
* [ ] Saisir une nouvelle équipe
* [ ] Modifier une équipe

### 5 - Menu pronostiques : Permet d'afficher les pronostiques du tournois
*Permet aux utilisateurs de voter pour une équipe dans le top 3*\
* [ ] Affiche le podium avec le nombre de vote pour tel équipe
* [ ] Voter pour une équipe 

/!\ Chaque Menu affiche en dessous un menu de navgation pour se balader entre les différents menus. Il doit donc s'adapter à chaque menu pour n'afficher que les menus disponnible ou signaler sur quel menu on se trouve. (à voir si on peut pas mettre d'une certains couleur un élément du menu où simplement le différencier avec un caractère en plus)
