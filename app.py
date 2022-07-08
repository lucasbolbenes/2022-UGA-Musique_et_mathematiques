import time
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import pyaudio
import numpy as np
from math import pi

from clavier import demarrerClavier
from construireGamme import construireFrequencesDeLaGammeTemperee, construireFrequencesDeLaGammePythagoricienne
from entendreGamme import entendreGamme
from entendreNombre import entendreNombre
from jouerSequence import jouerSequence
from entendreAccord import entendreAccordComplet
from gammeShepard import illusionAscendante
from Signal import Signal

# - Variables globales
couleur_principale = '#E1A61D'
couleur_secondaire = '#424949'
couleur_texte_boutton = 'White'
couleur_texte_label = 'White'
largeur=45
taille_texte_grand_titre_label = ("Claibri",15)
taille_texte_titre_label = ("Calibri", 13)

frequencesDeLaGamme = []
pourcentage = 0.1
frequence_1 = 360
frequence_2 = 360
fao = ""
fad = ""

# Variables PyAudio
volume = 0.4                 # intervalle : [0.0, 1.0]
echantillonage = 44100       # échantillonage, en Hz, valeur entière
duree = 1                    # durée en seconde, peut être un nombre décimal

frequencesDeLaGamme = []
signauxDeLaGamme = []
diffuseur = 0


def majFrequence_1(event):
    global frequence_1
    frequence_1 = float(event)

def majFrequence_2(event):
    global frequence_2
    frequence_2 = float(event)

def majDuree(event):
    global duree
    duree = float(event)

def majVolume(event):
    global volume
    volume = float(event)

def nouvelleFrequence(event):
    global frequence_1
    global frequence_2

    frequence = int(frequence_entry.get())

    bas = int(frequence - pourcentage * frequence)
    haut = int(frequence + pourcentage * frequence)
    frequence1_scale.configure(from_=bas)
    frequence1_scale.configure(to=haut)
    frequence2_scale.configure(from_=bas)
    frequence2_scale.configure(to=haut)

    frequence1_scale.set(bas)
    frequence2_scale.set(haut)

    frequence_1 = bas
    frequence_2 = haut

    frequence_entry.delete(0,END)

def jouerAccord():
    entendreAccordComplet([frequence_1, frequence_2], diffuseur, duree, [0.5, 0.5], volume, echantillonage)

def reset():
        for widget in app.winfo_children():
            if(widget.winfo_class() != 'Menu'):
                widget.destroy()

def gammeManuelle():

    global frequencesDeLaGamme
    frequencesDeLaGamme = gamme_text.get(1.0, "end").split(" ")
    frequencesDeLaGamme = list(map(float, frequencesDeLaGamme))

def gammeTemperee():
    global frequencesDeLaGamme
    frequencesDeLaGamme = construireFrequencesDeLaGammeTemperee(float(fondamentale_entry.get()), float(intervalles_entry.get()), float(octaves_entry.get()))
    gamme_text.delete(1.0,"end")
    gamme_text.insert(1.0,frequencesDeLaGamme)

def gammePythagoricienne():
    global frequencesDeLaGamme
    frequencesDeLaGamme = construireFrequencesDeLaGammePythagoricienne(float(fondamentale_entry.get()), float(intervalles_entry.get()))
    gamme_text.delete(1.0,"end")
    gamme_text.insert(1.0,frequencesDeLaGamme)

def entendreGammeCourante():
    entendreGamme(frequencesDeLaGamme, diffuseur, volume, echantillonage, duree)

def clavier():
    demarrerClavier(frequencesDeLaGamme, diffuseur, volume, echantillonage, duree)

def jouerUneSequence():
    jouerSequence(sequence_entry.get(), frequencesDeLaGamme, diffuseur, volume, echantillonage, duree)

def jouerUnNombre():
    param = nombre_entry.get()
    try:
        param = param.replace(",",".")
        float(param)
        entendreNombre(param, frequencesDeLaGamme, diffuseur, volume, echantillonage, duree)
    except ValueError:
        messagebox.showinfo("Erreur", "La saisie doit être composée de chiffres d'une virgule ou d'un point.")

def gammeShepard():
    illusionAscendante(diffuseur, volume, echantillonage, duree)

def fao():
    global fao
    global o
    global diffuseur
    global echantillonage

    file = askopenfilename(title="Choose the file to open", filetypes=[("WAV sound", ".wav")])
    print(file)
    fao_entry.configure(state="normal")
    fao_entry.delete(0,END)
    fao_entry.insert(0, file)
    fao_entry.configure(state="readonly")
    fao = file
    
    if frequencesDeLaGamme != []:
        o = Signal(frequencesDeLaGamme)
    else:
        o = Signal([440, 466, 494, 523, 554, 587, 622, 659, 698, 740, 784, 831, 880])

    o.init_from_wav(file)
    if o.echantillonage != echantillonage:
        echantillonage = o.echantillonage
        diffuseur = p.open(format=pyaudio.paFloat32,channels=1,rate=echantillonage,output=True)
        o.setDiffuseur(diffuseur)
    o.setDiffuseur(diffuseur)
    

def fad():
    global fad
    file = askopenfilename(title="Choose the file to open", filetypes=[("WAV sound", ".wav")])
    fad_entry.configure(state="normal")
    fad_entry.delete(0,END)
    fad_entry.insert(0, file)
    fad_entry.configure(state="readonly")
    fad = file


def ecouter():
    o.ecouter(0.9, o.signal)

def entendreEao():
    o.ecouter(1,o.signal)

def entendrePasseBas():
    o.filtre_passe_bas(int(passeBas_entry.get()))
    time.sleep(0.1)
    o.ecouter(1,o.filtered_signal)

def entendrePasseHaut():
    o.filtre_passe_haut(int(passeHaut_entry.get()))
    time.sleep(0.1)
    o.ecouter(1,o.filtered_signal)

def entendrePitchHigh():
    o.shift_right(int(pitchHigh_entry.get()))
    time.sleep(0.1)
    o.ecouter(1,o.filtered_signal)

def entendrePitchLow():
    o.shift_left(int(pitchLow_entry.get()))
    time.sleep(0.1)
    o.ecouter(1,o.filtered_signal)

def grapheEao():
    o.affichage()

def exporter():
    o.exporter(fad, o.filtered_signal)

def saturation():
    param = float(saturation_entry.get()) 
    if param < -1 or param > 1:
        messagebox.showinfo("Erreur", "Le paramètre doit être compris entre -1 et 1.")
    else:
        o.saturation(param)
        time.sleep(0.1)
        o.ecouter(1,o.filtered_signal)

def autotune():
    if frequencesDeLaGamme != []:
        o.set_gamme(frequencesDeLaGamme)
    else:
        o.set_gamme([440, 466, 494, 523, 554, 587, 622, 659, 698, 740, 784, 831, 880])
    o.autotune(int(autotune_entry.get()))
    time.sleep(0.1)
    o.ecouter(0.8,o.filtered_signal)


### - PROGRAMME PRINCIPAL


# - Lancement PyAudio
p = pyaudio.PyAudio()
diffuseur = p.open(format=pyaudio.paFloat32,channels=1,rate=echantillonage,output=True)

# - Lancement Tkinter
app = Tk()
app.configure(bg=couleur_secondaire)

freqFondamentale = DoubleVar()
nbIntervalle = DoubleVar()
app.geometry("600x400")

### - CREATION WIDGETS

# - Espaces
espace1 = Label(text=" ", highlightbackground=couleur_secondaire, bg=couleur_secondaire)
espace2 = Label(text=" ", highlightbackground=couleur_secondaire, bg=couleur_secondaire)
espace3 = Label(text=" ", highlightbackground=couleur_secondaire, bg=couleur_secondaire)
espace4 = Label(text=" ", highlightbackground=couleur_secondaire, bg=couleur_secondaire)
espace5 = Label(text="   ", highlightbackground=couleur_secondaire, bg=couleur_secondaire)
espace6 = Label(text=" ", highlightbackground=couleur_secondaire, bg=couleur_secondaire)
espace7 = Label(text=" ", highlightbackground=couleur_secondaire, bg=couleur_secondaire)
espace8 = Label(text=" ", highlightbackground=couleur_secondaire, bg=couleur_secondaire)
espace9 = Label(text=" ", highlightbackground=couleur_secondaire, bg=couleur_secondaire)
espace10 = Label(text="   ", highlightbackground=couleur_secondaire, bg=couleur_secondaire)
espace11 = Label(text=" ", highlightbackground=couleur_secondaire, bg=couleur_secondaire)
espace12 = Label(text=" ", highlightbackground=couleur_secondaire, bg=couleur_secondaire)

# - Titres
saisirDonnees_label = Label(app, fg=couleur_texte_label, text="Saisir les données",highlightbackground=couleur_secondaire, bg=couleur_secondaire, font=taille_texte_grand_titre_label) 
outilsTitre_label= Label(app, fg=couleur_texte_label, text="Outils",highlightbackground=couleur_secondaire, bg=couleur_secondaire, font=taille_texte_grand_titre_label) 
fltreBattement_label= Label(app, fg=couleur_texte_label, text="Filtres / Battement",highlightbackground=couleur_secondaire, bg=couleur_secondaire, font=taille_texte_grand_titre_label) 
# - Construire gamme
titre_label = Label(app, fg=couleur_texte_label, text="Construction d'une gamme",highlightbackground=couleur_secondaire, bg=couleur_secondaire, font=taille_texte_titre_label) 
fondamentale_label = Label(app, fg=couleur_texte_label, text="Fréquence fondamentale",highlightbackground=couleur_secondaire, bg=couleur_secondaire) 
intervalles_label = Label(app, fg=couleur_texte_label, text="Nombre d'intervalles",highlightbackground=couleur_secondaire, bg=couleur_secondaire)
octaves_label = Label(app, fg=couleur_texte_label, text="Nombre d'octaves",highlightbackground=couleur_secondaire, bg=couleur_secondaire)
fondamentale_entry = Entry(app, width=str(largeur)) 
intervalles_entry = Entry(app, width=str(largeur)) 
octaves_entry = Entry(app, width=str(largeur))
temperee_button = Button(app, text="Gamme tempérée", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/2)), command=gammeTemperee,highlightbackground=couleur_secondaire) 
pythagoricienne_button = Button(app, text="Gamme pythagoricienne", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/2)), command=gammePythagoricienne,highlightbackground=couleur_secondaire) 

# - Fichier audio origine
fao_label = Label(app, fg=couleur_texte_label, text="Fichier d'origine",highlightbackground=couleur_secondaire, bg=couleur_secondaire, font=taille_texte_titre_label) 
fao_label2 = Label(app, fg=couleur_texte_label, text="Fichier d'origine courant",highlightbackground=couleur_secondaire, bg=couleur_secondaire)
fao_button = Button(app, text="Ouvrir l'explorateur de fichier", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/2)), command=fao,highlightbackground=couleur_secondaire)
fao_entry = Entry(app, width=str(largeur), state="readonly")
# - Fichier audio origine
fad_label = Label(app, fg=couleur_texte_label, text="Fichier de desination",highlightbackground=couleur_secondaire, bg=couleur_secondaire, font=taille_texte_titre_label)
fad_label2 = Label(app, fg=couleur_texte_label, text="Fichier de destination courant",highlightbackground=couleur_secondaire, bg=couleur_secondaire) 
fad_button = Button(app, text="Ouvrir l'explorateur de fichier", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/2)), command=fad,highlightbackground=couleur_secondaire)
fad_entry = Entry(app, width=str(largeur), state="readonly")

# - Volume / Duree
parametres_label = Label(app, fg=couleur_texte_label, text="Paramètres généraux", width=str(int(largeur/2)),highlightbackground=couleur_secondaire, bg=couleur_secondaire, font=taille_texte_titre_label)
duree_label = Label(app, fg=couleur_texte_label, text="Durée", width="10",highlightbackground=couleur_secondaire, bg=couleur_secondaire)
duree_scale=Scale(app, highlightbackground=couleur_secondaire, bg=couleur_secondaire, tickinterval=1, resolution = 0.1, from_=0, to=5, orient='horizontal', command=majDuree, length=300, fg=couleur_texte_boutton)
duree_scale.set(1)
volume_label = Label(app, fg=couleur_texte_label, text="Volume", width="10",highlightbackground=couleur_secondaire, bg=couleur_secondaire)
volume_scale=Scale(app, tickinterval=0.2, resolution = 0.1, from_=0, to=1, orient='horizontal', command=majVolume, length=300,highlightbackground=couleur_secondaire, bg=couleur_secondaire, fg=couleur_texte_boutton)
volume_scale.set(0.5)


# - Gamme courante
gamme_label = Label(app, fg=couleur_texte_label, text="Gamme courante", width=str(int(largeur/2)),highlightbackground=couleur_secondaire, bg=couleur_secondaire, font=taille_texte_titre_label) 
gamme_text = Text(app, width="50", height="4", wrap="word")
gamme_button = Button(app, text="Mettre à jour la gamme", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/2)), command=gammeManuelle,highlightbackground=couleur_secondaire)
entendreGamme_button = Button(app, text="Entendre la gamme", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/2)), command=entendreGammeCourante,highlightbackground=couleur_secondaire)

# - Clavier
clavier_label = Label(app, fg=couleur_texte_label, text="Clavier", width=str(int(largeur/2)),highlightbackground=couleur_secondaire, bg=couleur_secondaire, font=taille_texte_titre_label)
clavier_button = Button(app, text="Jouer la gamme au clavier", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/2)), command=clavier,highlightbackground=couleur_secondaire)

# - Outils
outils_label = Label(app, fg=couleur_texte_label, text="Outils", width=str(int(largeur/2)),highlightbackground=couleur_secondaire, bg=couleur_secondaire, font=taille_texte_titre_label)
sequence_label = Label(app, fg=couleur_texte_label, text="Jouer une séquence",highlightbackground=couleur_secondaire, bg=couleur_secondaire)
sequence_entry = Entry(app, width=str(int(largeur/1.5))) 
sequence_entry.insert(0,"M  HIK  IHF  FIM  KIH  HIK  M  I  F  F")
sequence_button = Button(app, text="Jouer", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/4)), command=jouerUneSequence,highlightbackground=couleur_secondaire)
nombre_label = Label(app, fg=couleur_texte_label, text="Entendre un nombre",highlightbackground=couleur_secondaire, bg=couleur_secondaire)
nombre_entry = Entry(app, width=str(int(largeur/1.5))) 
nombre_button = Button(app, text="Jouer", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/4)), command=jouerUnNombre,highlightbackground=couleur_secondaire)

# - Illusion
illusion_label = Label(app, fg=couleur_texte_label, text="Illusions auditives", width=str(int(largeur/2)),highlightbackground=couleur_secondaire, bg=couleur_secondaire, font=taille_texte_titre_label)
shepard_button = Button(app, text="Gamme de Shepard", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/2)), command=gammeShepard,highlightbackground=couleur_secondaire)


# - Battements
battement_label = Label(app, fg=couleur_texte_label, text="Battement", width=str(int(largeur/2)),highlightbackground=couleur_secondaire, bg=couleur_secondaire, font=taille_texte_titre_label)
frequence_entry = Entry(app, width=str(largeur))
frequence_entry.bind("<Return>", nouvelleFrequence)
frequence1_scale=Scale(app, from_=360, to=400, orient='horizontal', command=majFrequence_1, length=300,highlightbackground=couleur_secondaire, bg=couleur_secondaire, fg=couleur_texte_boutton)
frequence2_scale=Scale(app, tickinterval=20, resolution = 1, from_=360, to=400, orient='horizontal', command=majFrequence_2, length=300,highlightbackground=couleur_secondaire, bg=couleur_secondaire, fg=couleur_texte_boutton)
soumettre_button = Button(app, text ="Entendre", command = jouerAccord,fg=couleur_texte_boutton, bg=couleur_principale,highlightbackground=couleur_secondaire , width=str(int(largeur/2)))

# - Filtres
filtres_label = Label(app, fg=couleur_texte_label, text="Filtres", width=str(int(largeur/2)),highlightbackground=couleur_secondaire, bg=couleur_secondaire, font=taille_texte_titre_label)
eao_label = Label(app, fg=couleur_texte_label, text="Audio d'origine",highlightbackground=couleur_secondaire, bg=couleur_secondaire) 
entendreEao_button = Button(app, text="Ecouter", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/4)), command=entendreEao, highlightbackground=couleur_secondaire)
grapheEao_button = Button(app, text="Graphe", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/4)), command=grapheEao, highlightbackground=couleur_secondaire)

passeBas_label = Label(app, fg=couleur_texte_label, text="Passe-bas",highlightbackground=couleur_secondaire, bg=couleur_secondaire) 
passeBas_entry = Entry(app)
passeBas_button = Button(app, text="Ecouter", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/4)), command=entendrePasseBas, highlightbackground=couleur_secondaire)

passeHaut_label = Label(app, fg=couleur_texte_label, text="Passe-haut",highlightbackground=couleur_secondaire, bg=couleur_secondaire) 
passeHaut_entry = Entry(app)
passeHaut_button = Button(app, text="Ecouter", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/4)), command=entendrePasseHaut, highlightbackground=couleur_secondaire)

pitchHigh_label = Label(app, fg=couleur_texte_label, text="Augmenter la hauteur",highlightbackground=couleur_secondaire, bg=couleur_secondaire) 
pitchHigh_entry = Entry(app)
pitchHigh_button = Button(app, text="Ecouter", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/4)), command=entendrePitchHigh, highlightbackground=couleur_secondaire)

pitchLow_label = Label(app, fg=couleur_texte_label, text="Baisser la hauteur",highlightbackground=couleur_secondaire, bg=couleur_secondaire) 
pitchLow_entry = Entry(app)
pitchLow_button = Button(app, text="Ecouter", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/4)), command=entendrePitchLow, highlightbackground=couleur_secondaire)

saturation_label = Label(app, fg=couleur_texte_label, text="Saturation",highlightbackground=couleur_secondaire, bg=couleur_secondaire) 
saturation_entry = Entry(app)
saturation_button = Button(app, text="Ecouter", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/4)), command=saturation, highlightbackground=couleur_secondaire)

autotune_label = Label(app, fg=couleur_texte_label, text="Auto-tune",highlightbackground=couleur_secondaire, bg=couleur_secondaire) 
autotune_entry = Entry(app)
autotune_button = Button(app, text="Ecouter", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/4)), command=autotune, highlightbackground=couleur_secondaire)

export_button = Button(app, text="Exporter", fg=couleur_texte_boutton, bg=couleur_principale, width=str(int(largeur/4)), command=exporter, highlightbackground=couleur_secondaire)

# - A propos

nom_label = Label(app, fg=couleur_texte_label, text="Par Brice Vittet & Lucas Bolbènes - 2022",highlightbackground=couleur_secondaire, bg=couleur_secondaire) 

### - AFFICHAGE

## - COLONNE N°1

# - Titres
saisirDonnees_label.grid(row=0, column=1)

# - Construire gamme
titre_label.grid(row=1, column=1) 
fondamentale_label.grid(row=2, column=0) 
intervalles_label.grid(row=3, column=0)
octaves_label.grid(row=4, column=0)
fondamentale_entry.grid(row=2, column=1) 
intervalles_entry.grid(row=3, column=1)
octaves_entry.grid(row=4, column=1)
temperee_button.grid(row=5, column=1)
pythagoricienne_button.grid(row=6, column=1)

# - Espace
espace1.grid(row=7, column=0, columnspan = 5)

# - Fichier audio origine
fao_label.grid(row=8, column=1)
fao_button.grid(row=9, column=1)
fao_label2.grid(row=10, column=0)
fao_entry.grid(row=10, column=1)

# - Espace
espace2.grid(row=11, column=0, columnspan = 5)

# - Fichier audio destination
fad_label.grid(row=12, column=1)
fad_button.grid(row=13, column=1)
fad_label2.grid(row=14, column=0)
fad_entry.grid(row=14, column=1)

# - Espace
espace3.grid(row=15, column=0, columnspan = 5)

# - Volume / Duree
parametres_label.grid(row=16, column=1)
duree_label.grid(row=17, column=0)
duree_scale.grid(row=17, column=1)
volume_label.grid(row=18, column=0)
volume_scale.grid(row=18, column=1)

## - COLONNE N°2

# - Titres
outilsTitre_label.grid(row=0, column=4, columnspan=3)

# - Séparation verticale
espace5.grid(row = 0, column=3, rowspan=20)

# - Gamme courante
gamme_label.grid(row=1, column=4, columnspan=3)
gamme_text.grid(row=2, column=4, rowspan=3, columnspan=3)
gamme_button.grid(row=5, column=4, columnspan=3)
entendreGamme_button.grid(row=6, column=4, columnspan=3)

# - Espace
espace6.grid(row=7, column=4)

# - Clavier
clavier_label.grid(row=8, column=4, columnspan=3)
clavier_button.grid(row=9, column=4, columnspan=3)

# - Espace
espace7.grid(row=10, column=4)
espace8.grid(row=11, column=4)

# - Outils
outils_label.grid(row=12, column=4, columnspan=3)
sequence_label.grid(row=13, column=4)
sequence_entry.grid(row=13, column=5) 
sequence_button.grid(row=13, column=6)
nombre_label.grid(row=14, column=4)
nombre_entry.grid(row=14, column=5) 
nombre_button.grid(row=14, column=6)

#espace
espace9.grid(row=15, column=4)

# - Titres
illusion_label.grid(row=16, column=4, columnspan=3)
shepard_button.grid(row=17, column=4, columnspan=3)

## - COLONNE N°3

# - Espace
espace10.grid(row = 0, column=7, rowspan=20)

# - Titre
fltreBattement_label.grid(row=0, column=8, columnspan=4)

# - Filtres
filtres_label.grid(row=1, column=8, columnspan=3)
eao_label.grid(row=2,column=8)
entendreEao_button.grid(row=2, column=9)
grapheEao_button.grid(row=2, column=10)

passeBas_label.grid(row=3,column=8)
passeBas_entry.grid(row=3, column=9)
passeBas_button.grid(row=3, column=10)

passeHaut_label.grid(row=4,column=8)
passeHaut_entry.grid(row=4, column=9)
passeHaut_button.grid(row=4, column=10)

pitchHigh_label.grid(row=5,column=8)
pitchHigh_entry.grid(row=5, column=9)
pitchHigh_button.grid(row=5, column=10)

pitchLow_label.grid(row=6,column=8)
pitchLow_entry.grid(row=6, column=9)
pitchLow_button.grid(row=6, column=10)

saturation_label.grid(row=7,column=8)
saturation_entry.grid(row=7, column=9)
saturation_button.grid(row=7, column=10)

autotune_label.grid(row=8,column=8)
autotune_entry.grid(row=8, column=9)
autotune_button.grid(row=8, column=10)

export_button.grid(row=9, column=8, columnspan=3)

# - Espace
espace11.grid(row=10, column=8)

# - Battements
battement_label.grid(row=11, column=8, columnspan=3)
frequence1_scale.grid(row=12, column=8, rowspan=3, columnspan=3)
frequence2_scale.grid(row=15, column=8, columnspan=3)
frequence_entry.grid(row=16, column=8, columnspan=3)
soumettre_button.grid(row=17, column=8, columnspan=3)

# - A propos
espace12.grid(row=18, column=8)
nom_label.grid(row=19, column=9, columnspan=2)

app.mainloop()


# - Fermeture PyAudio
diffuseur.stop_stream()
diffuseur.close()
p.terminate()
