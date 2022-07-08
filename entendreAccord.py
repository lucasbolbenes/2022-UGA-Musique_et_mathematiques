import pyaudio
import numpy as np

def charToInt(c):
    if c > 47 and c < 58: 
        return c - 48
    else:
        return(c - 55)

def entendreAccordComplet(frequencesDeLaGamme, diffuseur, duree, volumes, volume, echantillonage ):
    
    sommeSignaux = 0
    i = 0
    while i < len(frequencesDeLaGamme):
        frequence =  frequencesDeLaGamme[i]
        signal = (np.sin(2*np.pi*np.arange(echantillonage*duree)*frequence/echantillonage))
        sommeSignaux += volumes[i]*signal
        i+=1
    sommeSignaux = sommeSignaux.astype(np.float32)

    # - Traitement
    diffuseur.write(volume*sommeSignaux, len(sommeSignaux))
