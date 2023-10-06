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
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j+1][i+1])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j+1][i-1])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j-1][i+1])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j-1][i-1])
                    if i == 0:
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i])
                        self.solmut[j][i].naapurit.append(self.solmut[j][i+1])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j-1][i+1])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j+1][i+1])
                    if i == len(self.solmut[0])-1:
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i])
                        self.solmut[j][i].naapurit.append(self.solmut[j][i-1])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j-1][i-1])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j+1][i-1])
                if j == 0:
                    if i == 0:
                        self.solmut[j][i].naapurit.append(self.solmut[j][i+1])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j+1][i+1])
                    if i == len(self.solmut[0])-1:
                        self.solmut[j][i].naapurit.append(self.solmut[j][i-1])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j+1][i-1])
                    if i > 0 and i < len(self.solmut[0])-1:
                        self.solmut[j][i].naapurit.append(self.solmut[j][i+1])
                        self.solmut[j][i].naapurit.append(self.solmut[j][i-1])
                        self.solmut[j][i].naapurit.append(self.solmut[j+1][i])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j+1][i-1])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j+1][i+1])
                if j == len(self.solmut)-1:
                    if i == 0:
                        self.solmut[j][i].naapurit.append(self.solmut[j][i+1])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j-1][i+1])
                    if i == len(self.solmut[0])-1:
                        self.solmut[j][i].naapurit.append(self.solmut[j][i-1])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j-1][i-1])
                    if i > 0 and i < len(self.solmut[0])-1:
                        self.solmut[j][i].naapurit.append(self.solmut[j][i+1])
                        self.solmut[j][i].naapurit.append(self.solmut[j][i-1])
                        self.solmut[j][i].naapurit.append(self.solmut[j-1][i])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j-1][i+1])
                        self.solmut[j][i].naapurit.append(
                            self.solmut[j-1][i-1])
                        
    def karsi_naapurit(self, solmu):
        pos_x = solmu.koordinaatit[0]
        pos_y = solmu.koordinaatit[1]
        if solmu.edellinen.koordinaatit[0] < pos_x and solmu.edellinen.koordinaatit[1] == pos_y:
            if pos_x != len(kartta.taulukko[0])-1:
                if kartta.taulukko[pos_y][pos_x+1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y][pos_x+1])
                if pos_y > 0:
                    if kartta.taulukko[pos_y-1][pos_x] == 3 and kartta.taulukko[pos_y-1][pos_x+1] != 3:
                        solmu.pakolliset.append(self.solmut[pos_y-1][pos_x+1])
                if pos_y < len(kartta.taulukko)-1:
                    if kartta.taulukko[pos_y+1][pos_x] == 3 and kartta.taulukko[pos_y+1][pos_x+1] != 3:
                        solmu.pakolliset.append(self.solmut[pos_y+1][pos_x+1])
        if solmu.edellinen.koordinaatit[0] == pos_x and solmu.edellinen.koordinaatit[1] < pos_y:
            if pos_y != len(kartta.taulukko)-1:
                if kartta.taulukko[pos_y+1][pos_x] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y+1][pos_x])
                if pos_x > 0:
                    if kartta.taulukko[pos_y][pos_x-1] == 3 and kartta.taulukko[pos_y+1][pos_x-1] != 3:
                        solmu.pakolliset.append(self.solmut[pos_y+1][pos_x-1])
                if pos_x < len(kartta.taulukko[0])-1:
                    if kartta.taulukko[pos_y][pos_x+1] == 3 and kartta.taulukko[pos_y+1][pos_x+1] != 3:
                        solmu.pakolliset.append(self.solmut[pos_y+1][pos_x+1])

    
    def tunnista_seuraavat(self, solmu):


    def reitinhaku(self):

        # JPS-algoritmi
