from math import exp, log, fabs, sqrt

def construireGamme(nbIntervalle):
    alpha = exp(log(2)/nbIntervalle)
    tab = []
    i = 0
    while i < nbIntervalle:
        tab.append(pow(alpha,i))
        i+=1
    tab.append(2)

    return tab

def lePlusProche(reference, tab):

    lePlusProche = tab[0]
    difference = fabs(tab[0] - reference)

    i = 1
    while i < len(tab):
        differenceCourante = fabs(tab[i] - reference)
        if differenceCourante < difference:
            lePlusProche = tab[i]
            difference = differenceCourante
        i+=1

    return lePlusProche

def calculErreur(tab):
    quinte = 3/2
    tierceMajeure = 5/4
    tierceMineure = 6/5
    quarte = 4/3

    erreurQuinte = fabs(lePlusProche(quinte, tab) - quinte)
    erreurTierceMajeure = fabs(lePlusProche(tierceMajeure, tab) - tierceMajeure)
    erreurTierceMineure = fabs(lePlusProche(tierceMineure, tab) - tierceMineure)
    erreurQuarte = fabs(lePlusProche(quarte, tab) - quarte)
    return(erreurQuinte, erreurTierceMajeure, erreurTierceMineure, erreurQuarte, erreurQuinte + erreurTierceMajeure + erreurTierceMineure + erreurQuarte)

def tabResultat(minimum, maximum):
    tab = []

    i = minimum
    while i < maximum:
        resultat = calculErreur(construireGamme(i))

        sousTableau = [i]
        sousTableau.append(resultat[0])
        sousTableau.append(resultat[1])
        sousTableau.append(resultat[2])
        sousTableau.append(resultat[3])
        sousTableau.append(resultat[4])

        tab.append(sousTableau)
        i+=1
    return tab

def afficherTabResultat(tab):
    print("n\tQuinte\t\tTierce Majeure\t\tTierce Mineure\t\tQuarte\t\tSomme des erreurs")
    i = 0
    while i < len(tab):
        print(str(tab[i][0])+"\t"+str(round(tab[i][1]*10000))+"\t\t"+str(round(tab[i][2]*10000))+"\t\t\t"+str(round(tab[i][3]*10000))+"\t\t\t"+str(round(tab[i][4]*10000))+"\t\t"+str(round(tab[i][5]*10000))+"\n")
        i+=1


def afficherResultats(minimum, maximum):
    afficherTabResultat(tabResultat(minimum,maximum))


