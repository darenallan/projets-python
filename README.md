# Projets Python

Deux mini-projets réalisés en Bachelor 1 Informatique à Ynov. Ce sont des programmes console, sans dépendance externe (Python 3.8+).

## Jeu des pions (`jeu-des-pions/`)

Jeu de stratégie à deux joueurs, au tour par tour, dans le terminal.

- Plateau de `n` cases, chacune remplie au hasard avec 0 à `p` pions
- À son tour, un joueur déplace un pion d'une case vers une case située plus à gauche
- Quand tous les pions sont sur la première case, plus personne ne peut jouer : le joueur qui a fait le dernier coup gagne
- Saisies contrôlées : case de départ non vide, destination valide

Notions utilisées : programmation procédurale, découpage en fonctions, listes, boucles de jeu, validation des entrées.

```bash
python jeu-des-pions/jeu.py
```

## Caisse automatique (`caisse-automatique/`)

Simulation d'une caisse en libre-service, en programmation orientée objet.

- Classe `Article` : désignation, code-barre, prix, heure de scan (attributs privés, getters, setters)
- Classe `Panier` : ajout d'articles, total, ticket de caisse, durée des courses entre le premier et le dernier scan
- Menu interactif : ajouter un article, afficher le ticket, quitter

Notions utilisées : classes, encapsulation, `datetime`.

```bash
python caisse-automatique/caisse.py
```

Le même projet existe en Java : [caisse-automatique-java](https://github.com/darenallan/caisse-automatique-java).
