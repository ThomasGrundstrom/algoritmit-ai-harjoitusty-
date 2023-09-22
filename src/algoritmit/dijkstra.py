from kartta.kartta import kartta
from komponentit.solmut import Solmu
from komponentit.kaaret import Kaari


class Dijkstra:

    # Luokka, jolla toteutetaan Dijkstran algoritmi.

    def __init__(self):
        self.solmut = []
        self.keko = []
        self.alkusolmu = None
        self.loppusolmu = None
        self.polku = []
    

    def luo_verkko(self):

        # Luodaan solmuista ja kaarista koostuva verkko, jota algoritmi voi käyttää.

        for j in range(len(kartta.taulukko)):
            rivi = []
            for i in range(len(kartta.taulukko[j])):
                rivi.append(Solmu((i, j), kartta.taulukko[j][i]))
            self.solmut.append(rivi)
        for j in range(len(self.solmut)):
            for i in range(len(self.solmut[j])):
                if self.solmut[j][i].tyyppi == 1:
                    self.alkusolmu = self.solmut[j][i]
                    self.alkusolmu.etaisyys = 0
                if self.solmut[j][i].tyyppi == 2:
                    self.loppusolmu = self.solmut[j][i]
                if j > 0 and j < len(self.solmut) - 1:
                    if i > 0 and i < len(self.solmut[j]) - 1:
                        if kartta.taulukko[j-1][i] != 3:
                            self.solmut[j][i].naapurit.append(Kaari(self.solmut[j-1][i], 5))
                        if kartta.taulukko[j+1][i] != 3:
                            self.solmut[j][i].naapurit.append(Kaari(self.solmut[j+1][i], 5))
                        if kartta.taulukko[j][i-1] != 3:
                            self.solmut[j][i].naapurit.append(Kaari(self.solmut[j][i-1], 5))
                        if kartta.taulukko[j][i+1] != 3:
                            self.solmut[j][i].naapurit.append(Kaari(self.solmut[j][i+1], 5))
                        if kartta.taulukko[j+1][i+1] != 3:
                            self.solmut[j][i].naapurit.append(Kaari(self.solmut[j+1][i+1], 7))
                        if kartta.taulukko[j+1][i-1] != 3:
                            self.solmut[j][i].naapurit.append(Kaari(self.solmut[j+1][i-1], 7))
                        if kartta.taulukko[j-1][i+1] != 3:
                            self.solmut[j][i].naapurit.append(Kaari(self.solmut[j-1][i+1], 7))
                        if kartta.taulukko[j-1][i-1] != 3:
                            self.solmut[j][i].naapurit.append(Kaari(self.solmut[j-1][i-1], 7))
                if j == 0 and i > 0 and i < len(self.solmut[j]) - 1:
                    if kartta.taulukko[j+1][i] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j+1][i], 5))
                    if kartta.taulukko[j+1][i+1] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j+1][i+1], 7))
                    if kartta.taulukko[j+1][i-1] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j+1][i-1], 7))
                if j == len(self.solmut) - 1 and i > 0 and i < len(self.solmut[j]) - 1:
                    if kartta.taulukko[j-1][i] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j-1][i], 5))
                    if kartta.taulukko[j-1][i+1] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j-1][i+1], 7))
                    if kartta.taulukko[j-1][i-1] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j-1][i-1], 7))
                if i == 0 and j > 0 and j < len(self.solmut) - 1:
                    if kartta.taulukko[j][i+1] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j][i+1], 5))
                    if kartta.taulukko[j+1][i+1] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j+1][i+1], 7))
                    if kartta.taulukko[j-1][i+1] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j-1][i+1], 7))
                if i == len(self.solmut[j]) - 1 and j > 0 and j < len(self.solmut) - 1:
                    if kartta.taulukko[j][i-1] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j][i-1], 5))
                    if kartta.taulukko[j-1][i-1] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j-1][i-1], 7))
                    if kartta.taulukko[j+1][i-1] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j+1][i-1], 7))
                if j == 0 and i == 0:
                    if kartta.taulukko[j+1][i+1] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j+1][i+1], 7))
                if j == 0 and i == len(self.solmut[j]) - 1:
                    if kartta.taulukko[j+1][i-1] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j+1][i-1], 7))
                if j == len(self.solmut) - 1 and i == 0:
                    if kartta.taulukko[j-1][i+1] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j-1][i+1], 7))
                if j == len(self.solmut) - 1 and i == len(self.solmut[j]) - 1:
                    if kartta.taulukko[j-1][i-1] != 3:
                        self.solmut[j][i].naapurit.append(Kaari(self.solmut[j-1][i-1], 7))
    

    def reitinhaku(self):

        # Varsinainen Dijkstran algoritmi.

        self.luo_verkko()
        self.keko.append(self.alkusolmu)
        while len(self.keko) != 0:
            solmu = self.keko.pop(0)
            if solmu.koordinaatit == self.loppusolmu.koordinaatit:
                break
            if solmu.kasitelty:
                continue
            solmu.kasitelty = True
            for kaari in solmu.naapurit:
                nyky = kaari.loppu.etaisyys
                uusi = solmu.etaisyys + kaari.pituus
                if uusi < nyky:
                    kaari.loppu.etaisyys = uusi
                self.keko.append(kaari.loppu)
                kaari.loppu.edellinen = solmu
        while solmu.edellinen.koordinaatit != self.alkusolmu.koordinaatit:
            self.polku.append(solmu)
            solmu = solmu.edellinen
        print(self.solmut[39][39].etaisyys)
        print(self.polku)


dijkstra = Dijkstra()