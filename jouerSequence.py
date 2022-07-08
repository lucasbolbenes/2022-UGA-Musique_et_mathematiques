from math import pi, log, exp
import time
from tkinter import messagebox
import pyaudio
import numpy as np
from tkinter import *

# Variables PyAudio
volume = 0.2                 # intervalle : [0.0, 1.0]
echantillonage = 44100       # échantillonage, en Hz, valeur entière
duree = 1                  # durée en seconde, peut être un nombre décimal

frequencesDeLaGamme = []
signauxDeLaGamme = []
diffuseur = 0

def creerSignauxDepuisFrequences():

    global signauxDeLaGamme

    signauxDeLaGamme = []
    i = 0
    while i < len(frequencesDeLaGamme):
        frequence = frequencesDeLaGamme[i]
        signauxDeLaGamme.append((np.sin(2*np.pi*np.arange(echantillonage*duree)*frequence/echantillonage)).astype(np.float32))
        i+=1

def maVersionDeInt(nombre):
    if nombre > 47 and nombre < 58: 
        return nombre - 48
    else:
        return(nombre - 55) 

def jouerSequence(sequence, paramFrequencesDeLaGamme, paramDiffuseur, paramVolume, paramEchantillonage, paramDuree):

    global frequencesDeLaGamme
    global diffuseur
    global volume
    global echantillonage 
    global duree

    diffuseur = paramDiffuseur
    duree = paramDuree
    echantillonage = paramEchantillonage
    volume = paramVolume
    frequencesDeLaGamme = paramFrequencesDeLaGamme

    creerSignauxDepuisFrequences()

    # - Traitement
    i = 0
    sommeSignaux = 0
    while i < len(sequence):
        if sequence[i] == " ":
            time.sleep(duree/8)
        elif sequence[i] == "(":
            i+=1
            while sequence[i] != ")":
                try:
                    sommeSignaux += signauxDeLaGamme[maVersionDeInt(ord(sequence[i]))]
                except IndexError:
                    print("Vous avez saisi une note exclue de la gamme.")
                    messagebox.showinfo("Erreur", "Vous avez saisi une note exclue de la gamme.")
                    i = ")"
                i+=1
            diffuseur.write(volume*sommeSignaux, len(sommeSignaux))
        else:
            try:
                print(maVersionDeInt(ord(sequence[i])))
                diffuseur.write(volume*signauxDeLaGamme[maVersionDeInt(ord(sequence[i]))], len(signauxDeLaGamme[maVersionDeInt(ord(sequence[i]))]))
                #time.sleep(0.1)
            except IndexError:
                print("Vous avez saisi une note exclue de la gamme.")
                messagebox.showinfo("Erreur", "Vous avez saisi une note exclue de la gamme.")
                i = len(sequence)

        i+=1
