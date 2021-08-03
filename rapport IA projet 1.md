CIFTCI Semih         L3MN

Rapport de projet n°1 : « Trouver le trésor »

Objectif :

Le but de ce programme en python est de trouver le trésor.  
<span id="anchor"></span>Le chercheur est symbolisé par un
agent<span id="anchor-1"></span>(rectangle rouge) et le trésor est
symbolisé par un rectangle jaune.  
<span id="anchor-2"></span>Il y a également sur son parcours 2 pièges
symbolisés par un rectangle noir qu’il faudra éviter.

![](Pictures/1000000000000192000001AF996333B62FF57625.png)

Principe de fonctionnement :

<span id="anchor-3"></span>Le programme apprend grâce au principe de
d'apprentissage par renforcement qui consiste, pour un agent autonome, à
prendre les actions à partir d'expériences, de façon à optimiser une
récompense. L'agent est plongé au sein d'un environnement, et prend ses
décisions. 

L'environnement procure à l'agent une récompense, qui peut être positive
ou négative, dans notre cas l'environnement donne une récompense lorsque
l'agent trouve le trésor et donne une pénalité lorsque l'agent tombe sur
un piège.

L'agent va donc essayer d'avoir le maximum de récompenses positives en
moins de temps possible.

Réalisation :

<span id="anchor-4"></span>Ce programme est donc comme dit précédemment
réalisé en python.

  
<span id="anchor-5"></span>Le programme commence par les librairies, il
y a par exemple l'utilisation de<span id="anchor-6"></span> Tkinter pour
l'interface, de numpy pour les opérations et de pandas pour stocker les
valeurs (data frame).

![](Pictures/100000000000011B0000009DBDFF60DB86301083.png)

Puis, viens la déclaration de variables globales qui permettent de
configurer l'environnement visuel comme la taille de la fenêtre, le
nombre de cases, etc.

![](Pictures/10000000000001440000008ECF9FB4DB6BAAE713.png)

Après la déclaration des variables globales, on crée la classe "Maze" et
son constructeur, il permet de définir les paramètres de notre programme
conformément aux variables globales écrites plus haut.

![](Pictures/1000000000000293000000C46CBD474248B77D04.png)

Voici la 1ère fonction de la classe Maze, elle permet comme son nom
l'indique de construire le labyrinthe, ce code permet de créer les
carreaux des cases en fonction des variables globales, place l'agent,
les pièges et le trésor à trouver, la méthode renvoie la position des
éléments qui ont été placés.

![](Pictures/10000000000002D500000264F318DD8733215E01.png)

La fonction step qui fait parti de la classe Maze, quant à elle, permet
de faire bouger l'agent dans une direction en vérifiant qui puisse le
faire pour ne pas sortir des casses.

![](Pictures/10000000000002240000011B68B7B7FCBD7E572A.png)

La méthode<span id="anchor-7"></span> check\_state\_exist de la classe
Maze permet de vérifier que la position actuelle de l'agent ne figure
pas dans l'indice du tableau q\_table, si elle n'y est pas, elle est
ajoutée.

![](Pictures/10000000000001A3000000B370BF9E6DC66BB6FC.png)

La méthode<span id="anchor-8"></span> choose\_action permet comme son
nom l'indique de choisir une action, mais elle le fait selon les scores
de chaque case qui est stocké dans la<span id="anchor-9"></span>
q\_table et va choisir la direction ou la valeur est la plus grande,
mais elle à également une probabilité de 0.1 de faire une action
totalement aléatoire pour découvrir son environnement.

![](Pictures/10000000000002E4000000941C8778606226316F.png)

Voici la méthode<span id="anchor-10"></span> learn de la classe Maze,
cette méthode contient l'essence même du<span id="anchor-11"></span>
QLearning, cette méthode va donner une récompense si la position de
l'agent correspond à la position du trésor et à l'inverse, il va donner
un malus si l'agent se trouve sur une case piège.

![](Pictures/100000000000038A000000C8114CAAF17D134107.png)

La méthode<span id="anchor-12"></span> reset, va lui remettre à zéro
l'environnement tout en gardant la<span id="anchor-13"></span> q\_table
intacte pour que l'agent puisse réessayer en cas d'échec ou de réussite,
on va effacer dans cette méthode l'agent précédent et recrée un agent à
la case départ avec les données du précédent.

![](Pictures/100000000000026200000090C7AA902005ECCBDF.png)

Les méthodes<span id="anchor-14"></span> writeText
et<span id="anchor-15"></span> resetText de la classe Maze, vont comme
leur nom indique écrire du texte à une position donner et remettre à
zéro les textes à l'écran.

![](Pictures/10000000000003920000007A43CEA8429A2297FB.png)

<span id="anchor-16"></span>Et c'est ainsi que la classe Maze se
termine. Passons maintenant aux méthodes globales du programme.

La méthode global<span id="anchor-17"></span> displayScore permet de
prendre les données de la<span id="anchor-18"></span> q\_table et
d'afficher les scores pour chaque case sur la case elle-même, elle
reprend pour cela la méthode de la classe Maze décrit plus
haut,<span id="anchor-19"></span> writeText.

![](Pictures/100000000000037B000000806F3EDCCE3CEB1335.png)

<span id="anchor-20"></span>Cette méthode globale permet de faire
"tourner" le programme, elle va faire appelle à toutes les méthodes une
par une dans l'ordre pour le bon fonctionnement du
programme.<span id="anchor-21"></span> la boucle va se répéter jusqu'à
ce que l'agent ait trouvé le trésor 100 fois.

![](Pictures/100000000000031E00000199C40BE8B3D4DDCFBA.png)

Et 

voici le résultat final à l'exécution du code.

![](Pictures/10000000000003E7000001D58836D423D1CBD61A.png)

On peut également tester le programme en changeant quelques paramètres,
j'ai donc essayer de changer le taux de "découverte" dans la
fonction<span id="anchor-22"></span> choose\_action, pour passer de 0.1
à 0.2, mes remarques sont que comme prévu le programme fait plus de
détours pour essayer autre chose, mais il arrive tout de même à trouver
le bon chemin assez vite sans encombres.

Grâce à ce projet, j'ai compris le principe de fonctionnement de
l'apprentissage par renforcement qui consiste à apprendre du passé et à
évalué les meilleurs choix possibles en faisant de l'exploration.
