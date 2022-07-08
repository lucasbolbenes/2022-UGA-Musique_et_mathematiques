# Ce script permet d'utiliser le clavier de l'ordinateur pour jouer les notes d'une gamme

from math import exp, log
import tkinter as tk
import pyaudio
import numpy as np

# Variables globales
volume = 0.5                 
echantillonage = 44100       
duree = 1.0                  
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

def jouerSignal(evt):
    
    c1 = ['1','2','3','4','5','6','7','8','9','0','°', '+','a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','%','µ','<','w','x','c','v','b','n',',',';',':','!']
    c2 = ['&','é','"','\'','(','-','è','_','ç','à',')','=','A','Z','E','R','T','Y','U','I','O','P','Q','S','D','F','G','H','J','K','L','M','ù','*','<','W','X','C','V','B','N','?','.','/','§']
    i = 0
    while i < (len(frequencesDeLaGamme)) and i < len(c1):
        if(evt.char == c1[i] or evt.char == c2[i] and len(frequencesDeLaGamme) >= i):
            diffuseur.write(volume*signauxDeLaGamme[i])
        i+=1

def fermerFenetre(event):
    global app
    app.quit()
    app.destroy()


def demarrerClavier(paramfrequencesDeLaGamme, paramDiffuseur, paramVolume, paramEchantillonage, paramDuree):
    global volume
    global echantillonage
    global diffuseur
    global app
    global frequencesDeLaGamme
    global duree

    duree = paramDuree
    echantillonage = paramEchantillonage
    volume = paramVolume
    diffuseur = paramDiffuseur
    frequencesDeLaGamme = paramfrequencesDeLaGamme

    print("La gamme utilisée est : "+str(frequencesDeLaGamme))

    creerSignauxDepuisFrequences()
    
    keyPress_1 = ["<KeyPress-1>","<KeyPress-2>","<KeyPress-3>","<KeyPress-4>","<KeyPress-5>","<KeyPress-6>","<KeyPress-7>","<KeyPress-8>","<KeyPress-9>","<KeyPress-0>","<KeyPress-degree>","<+>","<a>","<z>","<e>","<r>","<t>","<y>","<u>","<i>","<o>","<p>","<q>","<s>","<d>","<f>","<g>","<h>","<j>","<k>","<l>","<m>","<KeyPress-percent>","<KeyPress-mu>","<KeyPress-less>","<w>","<x>","<c>","<v>","<b>","<n>","<KeyPress-comma>","<KeyPress-semicolon>","<KeyPress-colon>","<KeyPress-exclam>"]
    keyPress_2 = ["<KeyPress-ampersand>","<KeyPress-eacute>","<KeyPress-quotedbl>","<KeyPress-apostrophe>","<(>","<KeyPress-minus>","<KeyPress-egrave>","<_>","<KeyPress-ccedilla>","<KeyPress-agrave>","<)>","<=>","<A>","<Z>","<E>","<R>","<T>","<Y>","<U>","<I>","<O>","<P>","<Q>","<S>","<D>","<F>","<G>","<H>","<J>","<K>","<L>","<M>","<KeyPress-ugrave>","<*>","<KeyPress-greater>","<W>","<X>","<C>","<V>","<B>","<N>","<?>","<.>","</>","<KeyPress-section>"]

    app = tk.Tk()
    i = 0
    while i < len(frequencesDeLaGamme) and i < len(keyPress_1):
        app.bind(keyPress_1[i], jouerSignal)
        app.bind(keyPress_2[i], jouerSignal)
        app.bind('<Escape>', fermerFenetre)
        i+=1
    app.mainloop()



