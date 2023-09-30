from kartta.kartta import kartta
from komponentit.jpssolmut import Jpssolmu


class Jps:

    # Luokka JPS-algoritmin toteutusta varten.

    def __init__(self):
        self.solmut = []
        self.alkusolmu = None
        self.loppusolmu = None
    
    def luo_solmut(self):

        # Luodaan solmuista koostuva verkko, jota algoritmi voi käyttää.

        for j in range(len(self.kartta)):
            rivi = []
            for i in range(len(self.kartta[0])):
                rivi.append(Jpssolmu((i, j), kartta.taulukko[j][i]))
            self.solmut.append(rivi)
        for j in range(len(self.solmut)):
            for i in range(len(self.solmut[0])):
                if self.solmut[j][i].tyyppi == 1:
                    self.alkusolmu = self.solmut[j][i]
                if self.solmut[j][i].tyyppi == 2:
                    self.loppusolmu = self.solmut[j][i]
                if j > 0 and j < len(self.solmut)-1:
                    if i > 0 and i < len(self.solmut[0])-1:
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i])
                        self.solmut[j][i].naapurit.append(self.solmut[j][i-1])
                        self.solmut[j][i].naapurit.append(self.solmut[j][i+1])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i+1])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i-1])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i+1])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i-1])
                    if i == 0:
                        self.solmut[j][i].naapurit.append(self.solmut[j][i+1])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i+1])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i+1])
                    if i == len(self.solmut[0])-1:
                        self.solmut[j][i].naapurit.append(self.solmut[j][i-1])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i-1])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i-1])
                if j == 0:
                    if i == 0:
                        self.solmut[j][i].naapurit.append(self.solmut[j][i+1])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i+1])
                    if i == len(self.solmut[0])-1:
                        self.solmut[j][i].naapurit.append(self.solmut[j][i-1])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i-1])
                    if i > 0 and i < len(self.solmut[0])-1:
                        self.solmut[j][i].naapurit.append(self.solmut[j][i+1])
                        self.solmut[j][i].naapurit.append(self.solmut[j][i-1])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i-1])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i+1])
                if j == len(self.solmut)-1:
                    if i == 0:
                        self.solmut[j][i].naapurit.append(self.solmut[j][i+1])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i+1])
                    if i == len(self.solmut[0])-1:
                        self.solmut[j][i].naapurit.append(self.solmut[j][i-1])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i-1])
                    if i > 0 and i < len(self.solmut[0])-1:
                        self.solmut[j][i].naapurit.append(self.solmut[j][i+1])
                        self.solmut[j][i].naapurit.append(self.solmut[j][i-1])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i+1])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i-1])

    def reitinhaku(self):

        # JPS-algoritmi

