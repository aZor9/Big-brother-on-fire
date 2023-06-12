# Big-brother-on-fire
Jeux crée pour la Nuit du code 2023


## Description :
Vous jouez un astronaute qui essaye d'empêcher son vaisseau d'exploser alors qu'il traverse un champ d'astéroïdes.  <br>
Eteignez les flammes qui ravagent votre vaisseau pour vous en sortir !


## Documentation : 
Touche | Action
--- | ---
```Z``` / ```↑``` | monter <br>
```S``` / ```↓``` | descendre <br>
```Q``` / ```⟵``` | aller à gauche <br>
```D``` / ```⟶``` | aller à droite <br>
```P``` | quitter le jeu <br>

Vous devez atteindre un score de 20 pour gagner la partie.  <br>
Si vous arrivez à 10 au nombres de flammes vous avez perdu.

D'autres musiques et bruitages sont disponible dans les fichiers du jeu mais n'ont pas été utilisé par manque de temps.  <br>
Univers sélectionné : 1  <br>
Module pyxel uniquement  <br>


## Mise A Jour : 
MAJ du 04/06/2023 : 
- ajout des fleches du clavier 
- ajout d'une page d'accueil
- ajout d'un score
- ajout du temps 
- ajout du texte "p : quitter"
- ajout des mouvement du perso
- modif des couleurs en fonction de la perte ou de la victoire
- modif de la victoire : il faut que score = 20

## Installer Pyxel 
copié/collé venant du github source : [Lien](https://github.com/kitao/pyxel/) <br><br><br>

### Windows
Après avoir installé [Python3](https://www.python.org/) (version 3.7 ou plus), lancez la commande suivante :
```sh
pip install -U pyxel 
```
Si vous installez Python à l'aide de l'installateur officiel, veuillez cocher la case `Add Python 3.x to PATH` pour activer la commande `pyxel`.
### Mac
Après avoir installé [Python3](https://www.python.org/) (version 3.7 ou plus), lancez la commande suivante :
```sh
python3 -m pip install -U pyxel
```
Si vous utilisez Python3, qui est installé par défaut sur Mac, veuillez ajouter `sudo` au début de la commande ci-dessus pour activer la commande `pyxel`.
### Linux
Après avoir installé le paquet SDL2 (`libsdl2-dev` pour Ubuntu), [Python3](https://www.python.org/) (version 3.7 ou plus), et `python3-pip`, lancez la commande suivante :
```sh
sudo pip3 install -U pyxel
```
Si ce qui précède ne fonctionne pas, essayez l'autoconstruction en suivant les instructions de [Makefile](../Makefile).

