# bgb
## Blender Game Base

### License and Copyright

Ce jeu est sous Creative Commons Attribution-ShareAlike 3.0 Unported License.

Les scripts sont sous GNU GENERAL PUBLIC LICENSE Version 2.

Pour plus détails, voir le fichier License.

## A quoi ça sert ?
Ce jeu contient tout ce qu'il faut pour commencer un jeu, cela évite de réinventer la poudre tous les 4 matins.

### Des scripts python plutôt que des briques logiques
#### Les briques logiques devient vite des plats de spaghetti.
C'est plus facile de s'y retrouver dans des scripts.


#### Quels scripts
Les scripts:

* labomedia_once.py
* labomedia_always.py

sont les seuls scripts importés directement dans Blender.
Il ne faut jamais les modifier.

* main_once.py est excécuté à la première frame
* main_always.py est excuté toutes les frames suivantes

Tous les scripts sont importés en temps que modules, et ne sont compilés
qu'une seule fois.

Ces scripts importés n'ont plus besoin d'être rechargé dans Blender et il est alors possible de les modifier dans un éditeur externe. En relançant le jeu

### Testé sur
* Debian Jessie 8.3 avec Blender 2.72

### Installation
#### Blender

~~~text
sudo apt-get install blender
~~~

#### Installation de twisted pour python 3
##### Dépendances

~~~text
sudo apt-get install python3-dev python3-setuptools
~~~

##### Installation

~~~text
sudo pip3 twisted
~~~

### Lancement du jeu
Pour pouvoir utiliser les lanceurs

##### Installer xterm

~~~text
sudo apt-get install xterm
~~~


### Des threads dans le Game Engine
C'est possible avec le blenderplayer.

Dans Blender avec ["P"], les threads continueront à tourner en arrêtant le jeu avec Echap

### Merci à:

* Labomedia
