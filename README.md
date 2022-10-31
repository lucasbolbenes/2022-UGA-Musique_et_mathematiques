# ENGLISH VERSION

# UGA Excellence Course - June 2022
During a training course of excellence carried out in June 2022 whose objective was to study the link between mathematics and music, we were able to develop programs allowing to understand and to observe certain phenomena related to this topic as well as to make treatment of wav file.

## Prerequisite : *prerequis.txt*
Some prerequisites are necessary for the program to run correctly. You will find them in the file *prerequis.txt*.

## Report : *rapport.pdf*
This file is the report of our course. We invite you to consult it to understand the interest of the following programs.

## Main program : *app.py*
To use the program you have to get the python files in a directory, open a console in this same directory, and run the command *py app.py*.

You can then :
- manage the volume and duration of the sounds played
- create a tempered scale according to a fundamental frequency, a number of intervals and a number of octaves
- create a Pythagorean scale according to a fundamental frequency and a number of intervals
- listen to the current scale
- manually modify the current scale
- play the notes of the current scale using your keyboard
- play a sequence of notes
- hear a number (this is more of a programming exercise, for more information see the report)
- listen to the Shepard scale which corresponds to an auditory illusion (we have reprogrammed it but the function used for volume management is not ideal, we invite you to listen to this illusion on the internet)
- define a source file and a destination file (a wav file must be selected)
- listen to the current source file
- observe the graph corresponding to the current source file and its fft (fast fourier transform)
- process the current source file with a low-pass filter, high-pass filter, tone boost or cut, the value entered in the input field corresponds to the frequency in hertz, e.g. for the low-pass filter, entering 400 will cut all frequencies above 440 Hz
- process the current original file with home-made autotune which is not very convincing, the interest is in the design rather than in the use, for more information see the report
- look at the graph again but with the changes made by the processing
- export the result to the current destination file
- set two frequencies so that you can hear the flapping phenomenon

## Script *etudeErreurGammes.py*
The *etudeErreurGammes.py* script is the one used to justify the choice of 12 notes for the number of notes in the tempered scale in our report.
To run it, please open the console in the directory where it is contained and enter the command : *py etudeErreurGammes.py*.

## Script *harmonique.py*
The *harmonique.py* script is the one used to explain what the timbre is.
To execute it, please open the console in the directory where it is contained and enter the command : *py harmonique.py*.

## Installing PyAudio
PyAudio is a module that cannot be installed in a conventional way.
To install it, please follow the instructions in the following tutorial: https://www.youtube.com/watch?v=gVZZzb_FIXo

# VERSION FRANÇAISE

# Stage d'excellence UGA - Juin 2022
Lors d'un stage d'excellence effectué en Juin 2022 dont l'objectif était d'étudier le lien entre les mathématiques et la musique, nous avons pu élaborer des programmes permettant de comprendre et d'observer certains phénomènes liés à cette thématique ainsi que de faire du traitement de fichier wav.

## Prérequis : *prerequis.txt*
Des prérequis sont nécessaires pour que le programme puisse s'éxecuter correctement. Vous les trouverez dans le fichier *prerequis.txt*.

## Compte rendu : *rapport.pdf*
Ce fichier est le compte rendu de notre stage. Nous vous invitons à le consulter pour saisir l'intérêt des programmes suivants.

## Programme principal : *app.py*
Pour utiliser le programme il faut récupérer les fichiers python dans un répertoire, ouvrir une console dans ce même répertoire, et lancer la commande *py app.py*.

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

## Script *etudeErreurGammes.py*
Le script *etudeErreurGammes.py* est celui utilisé pour justifier le choix de 12 notes pour le nombre de notes de la gamme tempérée dans notre rapport.
Pour l'éxecuter, veuillez ouvrir la console dans le repértoire où celui-ci est contenu et saisissez la commande : *py etudeErreurGames.py*.

## Script *harmonique.py*
Le script *harmonique.py* est celui utilisé pour expliquer ce qu'est le timbre.
Pour l'éxecuter, veuillez ouvrir la console dans le repértoire où celui-ci est contenu et saisissez la commande : *py harmonique.py*.

## Installation de PyAudio
PyAudio est un module qui ne s'installe pas de manière conventionnelle.
Pour l'installer veuillez suivre les instructions du tutoriel suivant : https://www.youtube.com/watch?v=gVZZzb_FIXo

