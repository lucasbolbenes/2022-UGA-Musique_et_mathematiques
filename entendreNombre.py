from math import pi, log, exp
import time
from tkinter import messagebox
import pyaudio
import numpy as np


# Variables PyAudio
volume = 0.5                 # intervalle : [0.0, 1.0]
echantillonage = 44100       # échantillonage, en Hz, valeur entière
duree = 1.0                  # durée en seconde, peut être un nombre décimal

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

def baseTenToX(nombreBase10, x):
    
    nombreBaseX = ""
    dividende = nombreBase10
    diviseur = x
    quotient = -1
    reste = -1

    while quotient != 0:
        quotient = dividende // diviseur
        reste = dividende % diviseur
        if(reste > 9):
            reste = chr(reste+55)

        dividende = quotient
        nombreBaseX += str(reste)
        

    nombreBaseX = nombreBaseX[::-1] # [::-1] sert à inverser la chaine de caractère nombreBaseX
    return nombreBaseX

def charToInt(c):
    if c > 47 and c < 58: 
        return c - 48
    else:
        return(c - 55)         

def entendreNombre(nombre, paramFrequencesDeLaGamme, paramDiffuseur, paramVolume, paramEchantillonage, paramDuree):

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

    if(frequencesDeLaGamme != []):

        nombre = eval(nombre)
        nombre = format(nombre, '.100g')
        print(type(nombre))
        nombre = str(nombre)
        nombre= nombre.replace(",","")
        nombre = nombre.replace(".","")
        nombre = int(nombre)
        
        print(nombre)
        creerSignauxDepuisFrequences()

        nombre = baseTenToX(nombre, len(frequencesDeLaGamme) - 1)

        aLire = str(nombre)
        print(aLire)
        # - Traitement
        i = 0
        while i < len(aLire):
            diffuseur.write(volume*signauxDeLaGamme[charToInt(ord(aLire[i]))])
            #time.sleep(0.1)
            i+=1
    else:
        messagebox.showinfo("Erreur", "Veuillez créer une gamme.")


    
        