
# Blender Game Base
# bgb


### License and Copyright

Ce jeu est sous Creative Commons Attribution-ShareAlike 3.0 Unported License.

Les scripts sont sous GNU GENERAL PUBLIC LICENSE Version 2.

Pour plus détails, voir le fichier License.

## A quoi ça sert ?

Ce jeu contient tout ce qu'il faut pour commencer un jeu avec le Blender Game Engine, cela évite de réinventer la poudre tous les 4 matins.

## Des scripts python plutôt que des briques logiques
#### Les briques logiques deviennent vite des plats de spaghetti.

C'est plus facile de s'y retrouver dans des scripts.

#### Des briques logiques plutôt que du python

Pour les entrées clavier, le son, la souris ...

Il suffit de modifier une Game Property, et d'appeler cette propriété en python.

#### Les scripts non modifiables

* labomedia_once.py
* labomedia_always.py

sont les seuls scripts importés directement dans Blender.
Il ne faut jamais les modifier.

#### Les scripts modifiables

* main_once.py est excécuté à la première frame
* main_always.py est excuté toutes les frames suivantes

Tous les scripts sont importés en temps que modules, et ne sont compilés qu'une seule fois.

Ces scripts importés n'ont plus besoin d'être rechargé dans Blender et il est alors possible de les modifier dans un éditeur externe. Il faut relancer le jeu pour que les modifications soient effectives.

## Un serveur et du réseau avec twisted

### Des threads dans le Game Engine
C'est possible avec le blenderplayer.

Dans Blender avec ["P"], les threads continueront à tourner en arrêtant le jeu avec ["Echap"]
Cela exige de relancer le jeu avec un lanceur d'application.

## Comment utiliser les scripts de labtools ?
Le dossier labtools contient des scripts pour un tas de choses courrantes:

* réseau
* son
* fichier de configuration
* tempo
* texture

### TODO Rajouter un exemple dans mon jeu de tout ça !!

Ben dis donc ça m'en fait du boulot

## Testé sur
* Debian Jessie 8.3 avec Blender 2.72

### Installation
#### Blender

~~~text
sudo apt-get install blender
~~~

### Installation de twisted pour python 3
#### Dépendances

~~~text
sudo apt-get install python3-dev python3-setuptools
~~~

#### Installation

~~~text
sudo pip3 twisted
~~~

## Exécution du jeu du jeu
Avec les lanceurs TODO expliquer tout ça

#### Installer xterm

~~~text
sudo apt-get install xterm
~~~

### Merci à:

* [Labomedia]( https://labomedia.org/)


