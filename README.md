# labyrinthe

Projet 3:  Aidez  MacGyver  à  s'échapper

Introduction :

Le but de ce projet est de développer  un jeu vidéo  en 2 D  codé  en python  dans  lequel  MacGyver  est  enfermé  dans  un labyrinthe.  Pour s'en  évader,  il  doit se  déplacer  de case  en  case  à  l'aide  des  touches  directionnelles  du clavier  et  ramasser  trois  objets , placés  aléatioirement  dans  le labyrinthe , afin  de confectionner  une seringue  qui  lui  permettra  d'endormir  le garde  qui  en protège  la sortie . S'il arrive  devant  le  garde  sans  avoir  ramassé   les  trois  objets,  il ne pourra  pas  s'échapper  et le jeu  est  perdu.
Ce  jeu  est  réalisé  en  mode  console  puis  se  base  sur  le  module  Pygame  pour dessiner  l'interface  graphique.

Code  du  jeu :
Mon  code  est divisé  en quatre  fichiers: 
1- Fichier  Ressources :
Cedossier comporte 2 fichiers la  structure  du  labyr inthe  ainsi  que  les  différentes  images  utilisées  dans  le  jeu .  Le  symbole  «  # » correspond  aux  murs  et  le symbole «  » correspond  aux  chemins  libres. 
2- Fichier  config .py:
Ce  fichier comporte  les  variables  liées  aux  éléments  graphiques  du  jeu.  On  y trouve  la taille  en pixel  de  la fenêtre  du jeu  et  de la bande  d'affichage  des messages,  ainsi  que  les  chemins  d'accès  aux  images  utilisées  dans  le  jeu .
3- Fichier  Classes :
-La  classe  Character : 
Permet  le chargement  des images  des personnages  sur le labyrinthe  ainsi  que la création  des  coordonnées  des  positions  de  ces  personnages.
- La  classe  MacGyver :
Elle hérite  de la classe  Character  et comporte deux  méthodes,  une  permettant  le positionnement   de  MacGyver  sur  le  labyrinthe  et  l'autre  permettant  ses déplacements  de  case  en case  lorsque  le joueur appuit  sur les touches directionnelles  du clavier.
- La  classe  Map :
Elle  définit  la  création  de la  carte  du labyrinthe  et contient  plusieurs  méthodes  qui permettent : la  génération  des  chemins  de passage,  des  deux  personnages  et  des  trois  objects  positionnés  sur  les  chemins  de passage , en  coordonnées   x  et  y.   Elle  permet  d'ouvrir le  fichier  mapping.text  qui  contient  la structure  du labyrinthe , de l'enregistrer  sous  forme  de  liste  et  de  lire  cette  liste  ligne  par  ligne  et  sprite  par  sprite  en  allant  à la  ligne  chaque  15  sprites. 
- La  classe  Item :
Possède  une  méthode  qui  permet  d'afficher  les  trois  objets  sur les  chemins  de passage  de manière  aléatoire  grâce  à la fonction  randint  du module  random.
- La  classe  Display :
Permet  l'affichage   des  murs , des  chemin s de passage , des  messages ,  des  personnages  et  des  objets .  Elle  posséde  une  méthode  conditionnelle  qui  ne permet  les  déplacements  de  MacGyver  que  dans  les  chemins  de passage  et, dans ce  cas, lui permet  le ramassage  des  objets.  Elle  permet également  de remplacer MacGyver  et  l'objet  une fois ramassé  par le chemin de passage , d'afficher  l'objet rammassé  dans  le bandeau  en bas de l'écran  et d'incrémenter  l'inventaire  des  objets.  Cette  méthode  définit  aussi  l'affichage  du message : « invalid destination » en bas à gauche de l'écran  si le joueur  dirige  MacGyver  ver s un mur.
4- Fichier  main.py : 
Ce  fichier  comporte  une méthode  avec  une  boucle  principale  conditionnelle  qui  permet   le lancement  du jeu  et  les  déplacements  de MacGyver  grâce  aux  touches  directionnelles  du clavier.  Si le joueur appuit sur le x, le jeu s'arrête,  sinon  s'il appuit sur les touches  directionnelles  du clavier, MacGyver  se déplacera  dans  la direction choisie.  Il définit  également  l'affichage  de l'écran  d'accueil  comportant  le titre,  du labyrinthe  et  des  personnages  du jeu  ainsi  qu'une  méthode  permetant  l'affichage  des  objets  récoltés  et  une  autre  qui affichera  le message  de fin du jeu   lors  de  l'arrivée  de  MacGyver  à la  position  du gardien.
Difficultés  : Avec  un premier  mentor,  j'ai commencé  à coder  directement  sous  interphace  graphique,  ce  qui  ne  m'a  pas  permis  d'appréhender  la logique  du jeu.  Avec un deuxième  mentor,  j'ai  commencé  cette  fois  à coder  en  mode  console  mais  en procédural,  j'ai  alors  eu  beaucoup  de difficultés  à développer  mon code  en  mode  orienté  objet.  Le problème  se  situait  au  niveau  de  ma  maitrise  du  concept  de  classes.  J'ai  dû revoir les  cours  et  faire  des  recherches  sur internet.  J'ai  eu alors  un troisième  mentor qui  m'a  beaucoup  aidée  pour développer  le code  en  mode  orienté  objet.
