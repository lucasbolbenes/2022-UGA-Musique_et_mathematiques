# Stage d'excellence UGA - Juin 2022
Lors d'un stage d'excellence effectué en Juin 2022 dont l'objectif était d'étudier le lien entre les mathématiques et la musique, nous avons pu élaborer des programmes permettant de comprendre et d'observer certains phénomènes liés à cette thématique ainsi que de faire du traitement de fichier wav.

## Compte rendu : "rapport.pdf"
Ce fichier est le compte rendu de notre stage. Nous vous invitons à le consulter pour saisir l'intérêt des programmes suivants.

## Programme principal : "app.py"
Pour utiliser le programme il faut récupérer les fichiers python dans un répertoire, ouvrir une console dans ce même répertoire, et lancer la commande "py app.py".

Vous pourrez alors :
- gérer le volume et la durée des sons joués
- créer une gamme tempérée en fonction d'une fréquence fondamentale, d'un nombre d'intervalles et d'un nombre d'octaves
- créer une gamme pythagoricienne en fonction d'une fréquence fondamentale et d'un nombre d'intervalles
- écouter la gamme courante
- modifier manuellement la gamme courante
- jouer les notes de la gamme courante à l'aide de votre clavier
- jouer une séquence de notes
- entendre un nombre (cette possibilité correspond plus à un exercice de programmation, pour plus de renseignements, consultez le rapport)
- écouter la gamme de Shepard qui correspond à une illusion auditive (nous l'avons reprogrammé mais la fonction utilisé pour la gestion de volume n'est pas idéale, nous vous invitons à réecouter cette illusion sur internet)
- définir une fichier d'origine et un fichier de destination (il faut sélectionner un fichier wav)
- entendre le fichier d'origine courant
- observer le graphe correspondant au fichier d'origine courant ainsi que de sa fft (fast fourier transform)
- traiter le fichier d'origine courant avec un filtre passe-bas, passe-haut une augmentation ou une diminution de tonalité, la valeur saisie dans le champ d'entrée correspond à la fréquence en hertz, par exemple pour le filtre passe-bas, saisir 400 correspondra à couper toutes les fréquences supérieures à 440 Hz
- traiter le fichier d'origine courante avec de l'autotune faite-maison qui est peu convaincante, l'intêret étant dans la conception plutôt que dans l'utilisation, pour plus de renseignements, consultez le rapport
- observer à nouveau le graphe mais avec les modifications apportées par le traitement
- exporter le résultat dans le fichier de destination courant
- régler deux fréquences pour pouvoir entendre le phénomène de battements

## Script "etudeErreurGammes.py"
Le script "etudeErreurGammes.py" est celui utilisé pour justifier le choix de 12 notes pour le nombre de notes de la gamme tempérée dans notre rapport.
Pour l'éxecuter, veuillez ouvrir la console dans le repértoire où celui-ci est contenu et saisissez la commande : "py etudeErreurGames.py".

## Script "harmonique.py"
Le script "harmonique.py" est celui utilisé pour expliquer ce qu'est le timbre.
Pour l'éxecuter, veuillez ouvrir la console dans le repértoire où celui-ci est contenu et saisissez la commande : "py harmonique.py".

## Installation de PyAudio :
PyAudio est un module qui s'installe pas de manière conventionnelle.
Pour l'installer veuillez suivre les instructions du tutoriel suivant : https://www.youtube.com/watch?v=gVZZzb_FIXo

