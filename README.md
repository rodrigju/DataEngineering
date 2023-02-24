# Projet de DataEngineering 

Dans le cadre de l'unité de DataEngineering 1, nous devons réaliser comme projet final mettant en avant les différents notions abordées durant les TP. Nous avons d'abord abordé le scraping des sites web pour récupérer les données qu'ils contenaient, puis les databases comme MongoDb et d'autres ayant chacunes leurs avantages et inconvénients. 

J'ai choisi comme sujet d'étude la NFL (National Football League) car c'est un sujet qui me plait beaucoup. J'ai du scraper le site officiel de la NFL pour récupérer les données des joueurs, une fois les données récupérées j'ai alimenté ma base MongoDB et j'ai utilisé ces données dans un dashboard.

Je souhaitais au départ réaliser une interface web plus pousée avec Flask, celle-ci devait avoir plusieurs pages correspondant à plusieurs sections (une section team, players, etc...). J'ai dû abandonner cette idée, elle était trop compliquée et chronophage. Je suis donc parti finalement sur un dashboard pour présenter ces données.
De plus je souhaitais réaliser une prédicteur des résultats des matchs basés sur les joueurs présents sur le terrain, sous la forme de matrice avec comme valeurs les joueurs de l'équipe. Au départ il s'agirait d'une simple classification binaire retournant victoire ou défaite pour une équipe. Les bases d'apprentissage et de test seraient construites à partir des données récupérées. 
Comme pour le Flask j'ai du abandonner cette idée.

## Que contient le git
Vous trouverez dans mon git les fichiers python contenant la partie scraping et alimentation de ma database MongoDB dans un jupyter notebook, le fichier python du dashboard, et un tuto expliquant comment récupérer le headers nécessaire à la partie scraping. 

Le fichier requirements.txt vous permettra d'installer les librairies nécessaires pour le projet.
