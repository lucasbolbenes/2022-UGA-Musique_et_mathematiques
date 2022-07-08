from entendreAccord import entendreAccordComplet
from math import exp, log
import time
import pyaudio
import numpy as np

NB_ITERATION = 30
noteFondamentale = 440
frequences =    [noteFondamentale/32, noteFondamentale/16, noteFondamentale/8, noteFondamentale/4, noteFondamentale/2, noteFondamentale, noteFondamentale*2, noteFondamentale*4, noteFondamentale*8, noteFondamentale*16, noteFondamentale*32]
volumes =       [0.1,   0.2,  0.3,0.5, 0.7, 0.9, 0.7,  0.5,  0.3,  0.2,   0.1]

# Variables PyAudio
volume = 0.2                 # intervalle : [0.0, 1.0]
echantillonage = 44100       # échantillonage, en Hz, valeur entière
duree = 2.0                  # durée en seconde, peut être un nombre décimal

def gestionVolume(volume, frequence):
    #print(str(frequence)+" & "+str(volume)+" : ",end="")

    if noteFondamentale/32 <= frequence and frequence < noteFondamentale/16:
        volume += (0.15 - 0.1) / 12
    elif noteFondamentale/16 <= frequence and frequence < noteFondamentale/8:
        volume += (0.25 - 0.15) / 12
    elif noteFondamentale/8 <= frequence and frequence < noteFondamentale/4:
        volume += (0.55 - 0.25) / 12
    elif noteFondamentale/4 <= frequence and frequence < noteFondamentale/2:
        volume += (0.85 - 0.55) / 12
    elif noteFondamentale/2 <= frequence and frequence < noteFondamentale:
        volume += (0.9 - 0.85) / 12
    elif noteFondamentale*2 > frequence and frequence >= noteFondamentale:
        volume -= (0.9 - 0.85) / 12
    elif noteFondamentale*4 > frequence and frequence >= noteFondamentale*2:
        volume -= (0.85 - 0.55) / 12
    elif noteFondamentale*8 > frequence and frequence >= noteFondamentale*4:
        volume -= (0.55 - 0.25) / 12
    elif noteFondamentale*16 > frequence and frequence >= noteFondamentale*8:
        volume -= (0.25 - 0.15) / 12
    elif noteFondamentale*32 > frequence and frequence >= noteFondamentale*16:
        volume -= (0.15 - 0.1) / 12
    #print(volume)
    return volume

def illusionAscendante(paramDiffuseur, paramVolume, paramEchantillonage, paramDuree):

    global volume
    global echantillonage 
    global duree

    diffuseur = paramDiffuseur
    duree = paramDuree
    echantillonage = paramEchantillonage
    volume = paramVolume

    print("Écoutons ! ")

    i = 0
    while i < NB_ITERATION:
        print(frequences)
        print(volumes)
        print("\n")

        sommeSignaux = 0
        j = 0
        while j < len(frequences):
            sommeSignaux += volumes[j]*np.sin(2*np.pi*np.arange(echantillonage*duree)*frequences[j]/echantillonage)
            j+=1
        
        j = 0
        while j < len(frequences):
            volumes[j] = gestionVolume(volumes[j], frequences[j])
            frequences[j] *= exp(log(2)/12)
            if frequences[j] > noteFondamentale*64:
                print("\n\nOn est revenu au début !")
                frequences[j] = noteFondamentale/32
            j+=1
        
        sommeSignaux = sommeSignaux.astype(np.float32)
        diffuseur.write(0.2*sommeSignaux)

        time.sleep(0.2)
        
        i+=1
