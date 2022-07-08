import time
import pyaudio
import numpy as np


def creerSignauxDepuisFrequences(echantillonage, duree):

    global signauxDeLaGamme

    signauxDeLaGamme = []
    i = 0
    while i < len(frequencesDeLaGamme):
        frequence = frequencesDeLaGamme[i]
        signauxDeLaGamme.append((np.sin(2*np.pi*np.arange(echantillonage*duree)*frequence/echantillonage)).astype(np.float32))
        i+=1

def entendreGamme(paramFrequencesDeLaGamme, diffuseur, volume, echantillonage, duree):

    global frequencesDeLaGamme
    frequencesDeLaGamme = paramFrequencesDeLaGamme

    creerSignauxDepuisFrequences(echantillonage, duree)
    # - Traitement
    i = 0
    while i < len(signauxDeLaGamme):
        diffuseur.write(volume*signauxDeLaGamme[i], len(signauxDeLaGamme[i]))
        i+=1
