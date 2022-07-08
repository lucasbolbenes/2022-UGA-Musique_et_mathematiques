# Ce script permet de construire des gammes tempérées ou pythagoriciennes

from math import exp, log

def construireFrequencesDeLaGammeTemperee(noteFondamentale, nbIntervalle, nbOctave):

    frequencesDeLaGamme = []

    alpha = exp(log(2)/nbIntervalle)

    i = 0
    while i <= nbIntervalle*nbOctave:
        frequencesDeLaGamme.append(pow(alpha,i))
        i+=1

    i = 0
    while i < len(frequencesDeLaGamme):
        frequencesDeLaGamme[i] *= noteFondamentale
        i+=1

    return frequencesDeLaGamme

def construireFrequencesDeLaGammePythagoricienne(noteFondamentale, nbNote):

    # - On commence par créer la gamme de Pythagore
    float(noteFondamentale)
    notecourante = noteFondamentale
    frequencesDeLaGamme = []
    i = 0
    while i < nbNote:
        frequencesDeLaGamme.append(notecourante)
        if (notecourante * 3/2) < (2*noteFondamentale) :
            notecourante = notecourante * 3/2
        else :
            notecourante = notecourante * 3/4
        i+=1
    frequencesDeLaGamme.append(2*noteFondamentale)

    # - trie dans l'ordre la gamme
    list.sort(frequencesDeLaGamme)

    return frequencesDeLaGamme

    
