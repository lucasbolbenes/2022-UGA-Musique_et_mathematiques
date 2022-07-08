from tkinter import * 
from entendreAccord import entendreAccordComplet


pourcentage = 0.1
duree = 2
frequence_1 = 360
frequence_2 = 360

def majFrequence_1(event):
    global frequence_1
    frequence_1 = float(event)

def majFrequence_2(event):
    global frequence_2
    frequence_2 = float(event)

def majDuree(event):
    global duree
    duree = float(event)

def nouvelleFrequence(event):
    global frequence_1
    global frequence_2

    frequence = int(entryFrequence.get())

    bas = int(frequence - pourcentage * frequence)
    haut = int(frequence + pourcentage * frequence)
    scaleFrequence_1.configure(from_=bas)
    scaleFrequence_1.configure(to=haut)
    scaleFrequence_2.configure(from_=bas)
    scaleFrequence_2.configure(to=haut)

    scaleFrequence_1.set(bas)
    scaleFrequence_2.set(haut)

    frequence_1 = bas
    frequence_2 = haut

    entryFrequence.delete(0,END)

def jouerAccord():
    entendreAccordComplet([frequence_1, frequence_2],duree,[0.5, 0.5])

root = Tk()

entryFrequence = Entry()
entryFrequence.bind("<Return>", nouvelleFrequence)

scaleFrequence_1=Scale(root, tickinterval=20, resolution = 1, from_=360, to=400, orient='horizontal', label='Frequence de la première note', command=majFrequence_1, length=500)
scaleFrequence_2=Scale(root, tickinterval=20, resolution = 1, from_=360, to=400, orient='horizontal', label='Frequence de la seconde note', command=majFrequence_2, length=500)
scaleDuree=Scale(root, tickinterval=1, resolution = 1, from_=1, to=10, orient='horizontal', label='Durée', command=majDuree, length=500/4)


soumettre = Button(root, text ="Entendre", command = jouerAccord)

scaleFrequence_1.grid(row=1, column=4)
scaleFrequence_2.pack(row=2, column=4)
scaleDuree.pack(row=3, column=4)
entryFrequence.pack(row=4, column=4)
soumettre.pack(row=5, column=4)



root.mainloop()