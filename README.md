#Projet Poly#
Pandiculation

##Objectifs

Ce projet a pour but de générer l'ensemble des positions optimales pour des routeurs dans une pièce donnée
Les pièces sont décrites par leurs colonnes, lignes, coût d'un routeur,côut d'une cellule de fibre,cellule initial reliant la fibre
ainsi que une description de la carte avec des caractères ASCII

##L'équipe :

Nicolas Cuadros , Sebastien Berlioux, Simon Bessenay, Alexandre Nonnon

##Installation et utilisation du programme
Téléchargez la dernière version, et à partir du dossier racine lancez dans un terminal :

 * python3 main.py nom_de_la_carte

La solution sera sauvée dans le fichier solution.out dans le dossier racine du programme.

##Stratégie de résolution :

1) Calcul du potentiel de chaque cellule pouvant accueillir un routeur en fonction du nombre de cellules que le routeur couvrirait
2) Insertion des cellules dans une liste chainée dans l'ordre du potentiel le plus important au plus faible
3) Parcours de la liste chainée pour placer les routeurs sur la carte. Une fois un routeur placé, le potentiel de la cellule suivante dans la liste est recalculé et la cellule est retiré puis réinsérer dans la liste dans la liste si différent.
4) Un algorithme de calcul d'arbre optimisé pour relier les routeurs est lancé afin de placer la fibre au coup le plus faible possible
5) Parcours de la liste des routeurs placés et de la liste des cellules fibrées pour écrire la solution dans un fichier

##Organisation du code



##Bugs et limitations

- Algorithme de calcul du chemin de la fibre non optimal dans certains cas
- Algorithme très rapide au détriment de certains calculs plus pointu qui auraient permis un gain de points que l'on a trouvé négligeable

##Informations utiles

- Algorithmes de calcul et de placement routeurs très rapident pour de très bons résultats :
  - ~5sec pour charleston_road
  - ~3min pour opera
