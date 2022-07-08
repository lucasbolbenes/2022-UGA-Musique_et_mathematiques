from math import fabs
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from librosa import load
import pyaudio
plt.rcParams['figure.figsize'] = [10, 5]
#plt.rcParams.update({'font.size' : 10})

class Signal:
    def __init__(self, gamme):
        self.gamme = gamme
        self.diffuseur = []
        self.echantillonage = 0
        self.volume = 0
        self.duree = 0
        self.signal = np.array([])
        self.t = np.array([])
        self.signal_hat = np.array([])
        self.filtered_signal = np.array([])
        self.filtered_signal_hat = np.array([])
        self.filtered_signal_hat_ifft = np.array([])     
        #np.set_printoptions(threshold=sys.maxsize)

    # - Initialisations
    def init_from_wav(self, file):
        lu = load(file, sr=None)
        self.signal = lu[0]
        self.signal_hat = np.fft.fft(self.signal)
        self.echantillonage = lu[1]
        self.duree = len(self.signal)/self.echantillonage
        self.t = np.linspace(0., 1.*self.duree, int(self.echantillonage*self.duree))

    def init_from_param(self, tab_freq, duree, echantillonage):
        self.echantillonage = echantillonage
        self.duree = duree
        self.t = np.linspace(0., 1.*self.duree, int(self.echantillonage*self.duree))
        self.signal = self.creerSon(tab_freq)
        self.signal_hat = np.fft.fft(self.signal)

    # - Méthodes
    def setDiffuseur(self, diffuseur):
        self.diffuseur = diffuseur
        
    def creerSon(self, tabFreq):
        i = 0
        signal = 0
        while i < len(tabFreq):
            signal += 0.2*np.sin(2.*np.pi*tabFreq[i]*self.t)
            i+=1
        return signal

    def exporter(self, file, signal):
        print("Export en cours ...")
        amplitude = np.iinfo(np.int16).max/2
        data = amplitude * signal.real
        write(file, self.echantillonage, data.astype(np.int16))
        print("Export terminé !")
    


    def affichage(self):
        print("Affichage en cours ...")
        print(self.filtered_signal)
        if self.filtered_signal != []:
            nb_graph = 4
            label = "Signaux"
        else:
            nb_graph = 3
            label = "Signal"

        fig,axs = plt.subplots(nb_graph,1)
        plt.subplots_adjust(hspace=1)

        plt.sca(axs[0])
        plt.plot(self.t,self.signal,color='silver',linewidth=1.5, label="Signal d'origine")
        if nb_graph == 4:
            plt.plot(self.t,self.filtered_signal,color='gold',linewidth=1.5, label="Signal filtré")
        plt.legend()
        axs[0].set_title(label)

        plt.sca(axs[1])
        plt.plot(self.t,self.signal,color='silver',linewidth=1.5, label="Signal d'origine")
        if nb_graph == 4:
            plt.plot(self.t,self.filtered_signal,color='gold',linewidth=1.5, label="Signal filtré")
        plt.legend()
        plt.xlim(0, 0.1)
        axs[1].set_title(label)

        n = self.signal.size
        fftFreq = np.fft.fftfreq(n, d=self.t[1]-self.t[0])

        plt.sca(axs[2])
        plt.plot(abs(fftFreq), abs(self.signal_hat), color='silver', linewidth=1.5)
        axs[2].set_title("FFT du signal")
        if nb_graph == 4:
            plt.sca(axs[3])
            plt.plot(abs(fftFreq), abs(self.filtered_signal_hat), color='gold', linewidth=1.5)
            axs[3].set_title("FFT du signal fitlré")
        plt.show()
        print("Affichage terminé !")

    def ecouter(self,volume,signal):
        print("Ecoute en cours ...")
        print(signal)
        self.diffuseur.write(volume*((signal).astype(np.float32)), len(signal))
        print("Ecoute terminée !")

    # - Filtres
    def filtre_passe_bas(self, N):
        print("Filtrage des harmoniques supérieures à "+str(N)+" Hz en cours ...")

        N = int(N*self.duree)

        signal_hat = self.signal_hat.copy()
        i = N
        while i <= len(signal_hat) - N:
            signal_hat[i] = 0
            i+=1
        self.filtered_signal = np.fft.ifft(signal_hat)
        self.filtered_signal_hat = signal_hat
        self.filtered_signal_hat_ifft = np.fft.fft(self.filtered_signal)
        print("Filtrage terminé !")

    def filtre_passe_haut(self, N):
        print("Filtrage des harmoniques inférieures à "+str(N)+" Hz en cours ...")
        N = int(N*self.duree)
        signal_hat = self.signal_hat.copy()
        
        
        i = 0
        while i <= N:
            signal_hat[i] = 0
            i+=1

        i = len(signal_hat) - N
        while i < (len(signal_hat)):
            signal_hat[i] = 0
            i+=1
        

        self.filtered_signal = np.fft.ifft(signal_hat)
        self.filtered_signal_hat = signal_hat
        self.filtered_signal_hat_ifft = np.fft.fft(self.filtered_signal)
        print("Filtrage terminé !")

    def shift_left(self, N):
        N = int(N*self.duree)
        print("Décalage des harmoniques vers la gauche de "+str(N)+"Hz en cours ...")
        signal_hat = self.signal_hat.copy()

        mh = int(len(signal_hat)/2)
        mb = mh - 1
        j = 0
        for j in range(N):
            i = mb
            file = [0]
            while i >= 0:
                file.append(signal_hat[i])
                signal_hat[i] = file[0]
                file.pop(0)
                i -= 1
        
        
        j = 0
        for j in range(N):
            i = mh
            file = [0]
            while i < len(signal_hat):
                file.append(signal_hat[i])
                signal_hat[i] = file[0]
                file.pop(0)
                i += 1
        
        self.filtered_signal = np.fft.ifft(signal_hat)
        self.filtered_signal_hat = signal_hat
        self.filtered_signal_hat_ifft = np.fft.fft(self.filtered_signal)
        print("Décalage terminé !")


    def shift_right(self, N):
        N = int(N*self.duree)
        print("Décalage des harmoniques vers la droite de "+str(N)+"Hz en cours ...")
        signal_hat = self.signal_hat.copy()

        mh = int(len(signal_hat)/2)
        mb = mh - 1

        j = 0
        for j in range(N):
            i = 0
            file = [0]
            while i <= mb :
                file.append(signal_hat[i])
                signal_hat[i] = file[0]
                file.pop(0)
                i += 1
        
        j = 0
        for j in range(N):
            i = len(signal_hat) - 1
            file = [0]
            while i >= mh:
                file.append(signal_hat[i])
                signal_hat[i] = file[0]
                file.pop(0)
                i -= 1
        
        self.filtered_signal = np.fft.ifft(signal_hat)
        self.filtered_signal_hat = signal_hat
        self.filtered_signal_hat_ifft = np.fft.fft(self.filtered_signal)
        print("Décalage terminé !")

    def saturation(self, s):

        tab = self.signal.copy()

        n=len(tab)
        i=0
        while i<n:
                if(tab[i]>=s):
                        tab[i]=s
                i=i+1

        self.filtered_signal = tab
        self.filtered_signal_hat = np.fft.fft(tab)

    # -  Autotune
    
    def indice_le_plus_proche(self, reference, tab):
        indice = 0
        difference = fabs(tab[0] - reference)

        i = 1
        while i < len(tab):
            difference_courante = fabs(tab[i] - reference)
            if difference_courante < difference:
                indice = i
                difference = difference_courante
            i+=1

        return tab[indice]
    
    def shift_left_2(self, signal_hat, duree, N):
        N = int(N*duree)
        print("Décalage des harmoniques vers la gauche de "+str(N)+"Hz en cours ...")

        mh = int(len(signal_hat)/2)
        mb = mh - 1
        j = 0
        for j in range(N):
            i = mb
            file = [0]
            while i >= 0:
                file.append(signal_hat[i])
                signal_hat[i] = file[0]
                file.pop(0)
                i -= 1
        
        
        j = 0
        for j in range(N):
            i = mh
            file = [0]
            while i < len(signal_hat):
                file.append(signal_hat[i])
                signal_hat[i] = file[0]
                file.pop(0)
                i += 1
        
        print("Décalage terminé !")
        return signal_hat


    def shift_right_2(self, signal_hat, duree, N):
        N = int(N*duree)
        print("Décalage des harmoniques vers la droite de "+str(N)+"Hz en cours ...")

        mh = int(len(signal_hat)/2)
        mb = mh - 1

        j = 0
        for j in range(N):
            i = 0
            file = [0]
            while i <= mb :
                file.append(signal_hat[i])
                signal_hat[i] = file[0]
                file.pop(0)
                i += 1
        
        j = 0
        for j in range(N):
            i = len(signal_hat) - 1
            file = [0]
            while i >= mh:
                file.append(signal_hat[i])
                signal_hat[i] = file[0]
                file.pop(0)
                i -= 1
    
        print("Décalage terminé !")
        return signal_hat
    
    def autotune(self, nombre_sous_tableau):

        resultat = []
        taille = int(self.echantillonage / nombre_sous_tableau)
        tabs = self.subdiviser(self.signal, taille)
        rapport = self.echantillonage/taille
        duree = taille / self.echantillonage
        i = 0
        gamme = self.multiplier_gamme(0,1)
        print(gamme)
        while i < len(tabs):
            signal_hat = np.fft.fft(tabs[i])
            indice_harmonique_fondamentale = self.indice_harmonique_fondamentale(signal_hat, rapport)
            print("Fondamentale : "+str(indice_harmonique_fondamentale))
            difference = indice_harmonique_fondamentale - self.indice_le_plus_proche(indice_harmonique_fondamentale, gamme)
            print("Différence : "+str(difference))
            if difference < 0:
                resultat = np.concatenate([resultat, np.fft.ifft(self.shift_right_2(signal_hat, duree, abs(difference)))])
            else:
                resultat = np.concatenate([resultat, np.fft.ifft(self.shift_left_2(signal_hat, duree, difference))])
            i+=1
            
        self.filtered_signal = resultat
        self.filtered_signal_hat = np.fft.fft(resultat)  

    def set_gamme(self,gamme):
        self.gamme = gamme

    def multiplier_gamme(self, max_factor, max_divisor):
        i = 0
        resultat_1 = []
        resultat_2 = []

        factor = 2
        divisor = 2

        while i < max_factor - 1:
            j = 0
            while j < len(self.gamme):
                resultat_1.append(factor*self.gamme[j])
                j+=1
            factor += 1
            i += 1
        
        i = 0
        while i < max_divisor - 1:
            j = 0
            while j < len(self.gamme):
                resultat_1.append(self.gamme[j]/divisor)
                j+=1
            divisor += 1
            i += 1

        self.gamme += resultat_1
        self.gamme += resultat_2
        return self.gamme
    
    def subdiviser(self, signal_hat, taille_sous_tableaux):
        i = 0
        result = []

        while i < len(signal_hat):
            sous_tableau = []
            j = i
            n = j + taille_sous_tableaux
            while j < n and j < len(signal_hat):
                sous_tableau.append(signal_hat[j])
                j += 1
            i += taille_sous_tableaux
            result.append(sous_tableau)
        return result

    def indice_harmonique_fondamentale(self,signal_hat, rapport):
        return min(self.harmoniques_maximales(signal_hat, rapport))

    def harmoniques_maximales(self, signal_hat, rapport):
    
        indices = signal_hat * np.conj(signal_hat) >  0.10*self.harmonique_maximale(signal_hat)
        print(0.25*self.harmonique_maximale(signal_hat))
        harmoniques_maximales = []
        i = 0
        while i < len(indices):
            if indices[i] == True:
                harmoniques_maximales.append(i)
            i+=1
        return np.multiply(harmoniques_maximales, rapport)

    def harmonique_maximale(self, signal_hat):
        mh = int(len(signal_hat)/2)
        i = mh
        max = signal_hat[mh].real

        while i < len(signal_hat):
            if signal_hat[i].real > max:
                max = signal_hat[i].real
            i+=1

        return max
        

    

    

