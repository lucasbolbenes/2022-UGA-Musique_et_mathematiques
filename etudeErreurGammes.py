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

    erreurQuinte = lePlusProche(quinte, tab) / quinte
    erreurTierceMajeure = lePlusProche(tierceMajeure, tab) / tierceMajeure
    erreurTierceMineure = lePlusProche(tierceMineure, tab) / tierceMineure
    erreurQuarte = lePlusProche(quarte, tab) / quarte
    return(erreurQuinte, erreurTierceMajeure, erreurTierceMineure, erreurQuarte)

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

        tab.append(sousTableau)
        i+=1
    return tab

def afficherTabResultat(tab):
    print("n\tQuinte\t\tTierce Maj\tTierce Min\tQuarte")
    i = 0
    while i < len(tab):
        print(str(tab[i][0])+"\t"+str(format(fabs(1 - tab[i][1]), ".1E"))+"\t\t"+str(format(fabs(1 - tab[i][2]), ".1E"))+"\t\t"+str(format(fabs(1 - tab[i][3]), ".1E"))+"\t\t"+str(format(fabs(1 - tab[i][4]), ".1E"))+"\t\t\n")
        i+=1


def afficherResultats(minimum, maximum):
    afficherTabResultat(tabResultat(minimum,maximum))


minimum = '\0'
maximum = '\0'
while minimum != 0 and maximum != 0:
    print("Ce programme permet de comparer les gammes tempérées de différentes tailles en fonction du critère suivant :\nOn trouve la note la plus proche de la quinte dans la gamme courante, on calcule son rapport avec la quinte réelle,\non soustrait cette valeur à 1 (car plus cette valeur est proche de 1, plus l'erreur est faible, donc plus la différence\nentre 1 et cette valeur est faible, plus l'erreur est faible), puis on l'affiche en écriture scientifique.\nOn répète ce procédé avec la tierce majeure, la tierce mineur et la quarte pour toutes les gammes comprises\ndans l'intervalle que vous allez définir. Pour quitter veuillez saisir 0\n")
    minimum = int(input("Veuillez saisir le minimum de l'intervalle : (On conseille 2)"))
    maximum = int(input("Veuillez saisir le maximum de l'intervalle : "))
    if minimum != 0 and maximum != 0:
        afficherResultats(minimum, maximum)


