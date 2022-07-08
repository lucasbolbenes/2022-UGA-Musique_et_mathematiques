from tkinter import * 
from entendreAccord import entendreAccordComplet

# On considère que la n-ième harmonique est l'harmonique de rang n
# Variables globales
frequenceFondamentale = float(input("Veuillez saisir la fréquence de la note fondamentale : "))
longueur = 500

volumes = [0]* 10


dureeNote = 2

def jouerAccord():
    
    frequences = [frequenceFondamentale, frequenceFondamentale*2, frequenceFondamentale*3, frequenceFondamentale*4, frequenceFondamentale*5, frequenceFondamentale*6, frequenceFondamentale*7, frequenceFondamentale*8, frequenceFondamentale*9, frequenceFondamentale*10]
    print(frequences)
    print("On joue l'accord : ")
    entendreAccordComplet(frequences, dureeNote, volumes)
    print("Son joué : ")

def majVolumeFondamentale(event):
    global volumes
    volumes[0] = float(event)

def majVolumeSecondeHarmonique(event):
    global volumes
    volumes[1] = float(event)

def majVolumeTroisiemeHarmonique(event):
    global volumes
    volumes[2] = float(event)

def majVolumeQuatriemeHarmonique(event):
    global volumes
    volumes[3] = float(event)

def majVolumeCinquiemeHarmonique(event):
    global volumes
    volumes[4] = float(event)

def majVolumeSixiemeHarmonique(event):
    global volumes
    volumes[5] = float(event)

def majVolumeSeptiemeHarmonique(event):
    global volumes
    volumes[6] = float(event)

def majVolumeHuitiemeHarmonique(event):
    global volumes
    volumes[7] = float(event)

def majVolumeNeuviemeHarmonique(event):
    global volumes
    volumes[8] = float(event)

def majVolumeDixiemeHarmonique(event):
    global volumes
    volumes[9] = float(event)


root = Tk()

widgetVolumeDixiemeHarmonique=Scale(root, resolution = 0.1, from_=0, to=1, orient='horizontal', label='Volume de l\'harmonique de rang 10', command=majVolumeDixiemeHarmonique, length=longueur)
widgetVolumeNeuviemeHarmonique=Scale(root, resolution = 0.1, from_=0, to=1, orient='horizontal', label='Volume de l\'harmonique de rang 9', command=majVolumeNeuviemeHarmonique, length=longueur)
widgetVolumeHuitiemeHarmonique=Scale(root, resolution = 0.1, from_=0, to=1, orient='horizontal', label='Volume de l\'harmonique de rang 8', command=majVolumeHuitiemeHarmonique, length=longueur)
widgetVolumeSeptiemeHarmonique=Scale(root, resolution = 0.1, from_=0, to=1, orient='horizontal', label='Volume de l\'harmonique de rang 7', command=majVolumeSeptiemeHarmonique, length=longueur)
widgetVolumeSixiemeHarmonique=Scale(root, resolution = 0.1, from_=0, to=1, orient='horizontal', label='Volume de l\'harmonique de rang 6', command=majVolumeSixiemeHarmonique, length=longueur)
widgetVolumeCinquiemeHarmonique=Scale(root, resolution = 0.1, from_=0, to=1, orient='horizontal', label='Volume de l\'harmonique de rang 5', command=majVolumeCinquiemeHarmonique, length=longueur)
widgetVolumeQuatriemeHarmonique=Scale(root, resolution = 0.1, from_=0, to=1, orient='horizontal', label='Volume de l\'harmonique de rang 4', command=majVolumeQuatriemeHarmonique, length=longueur)
widgetVolumeTroisiemeHarmonique=Scale(root, resolution = 0.1,from_=0, to=1, orient='horizontal', label= 'Volume de l\'harmonique de rang 3', command=majVolumeTroisiemeHarmonique, length=longueur)
widgetVolumeSecondeHarmonique=Scale(root, resolution = 0.1,from_=0, to=1, orient='horizontal', label='Volume de l\'harmonique de rang 2', command=majVolumeSecondeHarmonique, length=longueur)
widgetVolumeFondamentale=Scale(root, resolution = 0.1, from_=0, to=1, orient='horizontal', label='Volume de la fondamentale', command=majVolumeFondamentale, length=longueur)

widgetVolumeFondamentale.pack()
widgetVolumeSecondeHarmonique.pack()
widgetVolumeTroisiemeHarmonique.pack()
widgetVolumeQuatriemeHarmonique.pack()
widgetVolumeCinquiemeHarmonique.pack()
widgetVolumeSixiemeHarmonique.pack()
widgetVolumeSeptiemeHarmonique.pack()
widgetVolumeHuitiemeHarmonique.pack()
widgetVolumeNeuviemeHarmonique.pack()
widgetVolumeDixiemeHarmonique.pack()

soumettre = Button(root, text ="Soumettre", command = jouerAccord)
soumettre.pack()

root.mainloop()