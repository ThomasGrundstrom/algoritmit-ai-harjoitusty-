import time
from kartta.kartta import kartta
from komponentit.jpssolmut import Jpssolmu


class DiagonalFirstPrio:
    def __init__(self, lista):
        self.lista = lista

    def lisaa_listaan(self, solmu):
        pos_x = solmu.koordinaatit[0]
        pos_y = solmu.koordinaatit[1]
        if pos_x != solmu.edellinen.koordinaatit[0] and pos_y != solmu.edellinen.koordinaatit[1]:
            self.lista.insert(0, solmu)
        else:
            self.lista.append(solmu)

    def poista_listasta(self):
        return (self.lista.pop(0))

    def pituus(self):
        return (len(self.lista))


class Jps:

    # Luokka JPS-algoritmin toteutusta varten.

    def __init__(self):
        self.solmut = []
        self.alkusolmu = None
        self.loppusolmu = None
        self.polku = []
        self.hyppypisteet = []

    def luo_solmut(self):

        # Luodaan kaksiulotteinen lista solmuista, jossa jokainen solmu vastaa pistettä kartalla.
        # Määritellään samalla lähtö- ja maalipisteiden koordinaatit.
        # Asetetaan lähtöpisteen etäisyydeksi 0 ja määritellään lähtöpisteen naapurisolmut.

        for j in range(len(kartta.taulukko)):
            rivi = []
            for i in range(len(kartta.taulukko[0])):
                rivi.append(Jpssolmu((i, j), kartta.taulukko[j][i]))
            self.solmut.append(rivi)
        for j in range(len(self.solmut)):
            for i in range(len(self.solmut[0])):
                if self.solmut[j][i].tyyppi == 1:
                    self.alkusolmu = self.solmut[j][i]
                    self.alkusolmu.etaisyys = 0
                    if j > 0 and j < len(self.solmut)-1:
                        if i > 0 and i < len(self.solmut[0])-1:
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j-1][i])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j+1][i])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j][i-1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j][i+1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j+1][i+1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j+1][i-1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j-1][i+1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j-1][i-1])
                        if i == 0:
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j+1][i])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j-1][i])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j][i+1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j-1][i+1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j+1][i+1])
                        if i == len(self.solmut[0])-1:
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j+1][i])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j-1][i])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j][i-1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j-1][i-1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j+1][i-1])
                    if j == 0:
                        if i == 0:
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j][i+1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j+1][i])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j+1][i+1])
                        if i == len(self.solmut[0])-1:
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j][i-1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j+1][i])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j+1][i-1])
                        if i > 0 and i < len(self.solmut[0])-1:
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j][i+1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j][i-1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j+1][i])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j+1][i-1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j+1][i+1])
                    if j == len(self.solmut)-1:
                        if i == 0:
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j][i+1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j-1][i])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j-1][i+1])
                        if i == len(self.solmut[0])-1:
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j][i-1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j-1][i])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j-1][i-1])
                        if i > 0 and i < len(self.solmut[0])-1:
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j][i+1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j][i-1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j-1][i])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j-1][i+1])
                            self.solmut[j][i].naapurit.append(
                                self.solmut[j-1][i-1])
                if self.solmut[j][i].tyyppi == 2:
                    self.loppusolmu = self.solmut[j][i]

    def karsi_naapurit(self, solmu):

        # Määrittelee, mitkä tutkittavan solmun naapureista ovat tarpeellisia käydä läpi.
        # Tutkittavat naapurisolmut riippuvat suunnasta, josta solmuun on saavuttu sekä siitä, onko naapurisolmujen joukossa esteitä.

        pos_x = solmu.koordinaatit[0]
        pos_y = solmu.koordinaatit[1]
        if solmu.edellinen.koordinaatit[0] < pos_x and solmu.edellinen.koordinaatit[1] == pos_y:
            if pos_x != len(kartta.taulukko[0])-1:
                if kartta.taulukko[pos_y][pos_x+1] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y][pos_x+1])
#                    if kartta.taulukko[pos_y][pos_x+1] != 2:
#                        solmu.luonnolliset.append(self.solmut[pos_y][pos_x+1])
#                    else:
#                        solmu.pakolliset.append(self.solmut[pos_y][pos_x+1])
                if pos_y > 0:
                    if kartta.taulukko[pos_y-1][pos_x] == 3 and kartta.taulukko[pos_y-1][pos_x+1] != 3:
                        solmu.pakolliset.append(self.solmut[pos_y-1][pos_x+1])
                if pos_y < len(kartta.taulukko)-1:
                    if kartta.taulukko[pos_y+1][pos_x] == 3 and kartta.taulukko[pos_y+1][pos_x+1] != 3:
                        solmu.pakolliset.append(self.solmut[pos_y+1][pos_x+1])
        if solmu.edellinen.koordinaatit[0] == pos_x and solmu.edellinen.koordinaatit[1] < pos_y:
            if pos_y != len(kartta.taulukko)-1:
                if kartta.taulukko[pos_y+1][pos_x] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y+1][pos_x])
#                    if kartta.taulukko[pos_y+1][pos_x] != 2:
#                        solmu.luonnolliset.append(self.solmut[pos_y+1][pos_x])
#                    else:
#                        solmu.pakolliset.append(self.solmut[pos_y+1][pos_x])
                if pos_x > 0:
                    if kartta.taulukko[pos_y][pos_x-1] == 3 and kartta.taulukko[pos_y+1][pos_x-1] != 3:
                        solmu.pakolliset.append(self.solmut[pos_y+1][pos_x-1])
                if pos_x < len(kartta.taulukko[0])-1:
                    if kartta.taulukko[pos_y][pos_x+1] == 3 and kartta.taulukko[pos_y+1][pos_x+1] != 3:
                        solmu.pakolliset.append(self.solmut[pos_y+1][pos_x+1])
        if solmu.edellinen.koordinaatit[0] > pos_x and solmu.edellinen.koordinaatit[1] == pos_y:
            if pos_x != 0:
                if kartta.taulukko[pos_y][pos_x-1] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y][pos_x-1])
#                    if kartta.taulukko[pos_y][pos_x-1] != 2:
#                        solmu.luonnolliset.append(self.solmut[pos_y][pos_x-1])
#                    else:
#                        solmu.pakolliset.append(self.solmut[pos_y][pos_x-1])
                if pos_y > 0:
                    if kartta.taulukko[pos_y-1][pos_x] == 3 and kartta.taulukko[pos_y-1][pos_x-1] != 3:
                        solmu.pakolliset.append(self.solmut[pos_y-1][pos_x-1])
                if pos_y < len(kartta.taulukko)-1:
                    if kartta.taulukko[pos_y+1][pos_x] == 3 and kartta.taulukko[pos_y+1][pos_x-1] != 3:
                        solmu.pakolliset.append(self.solmut[pos_y+1][pos_x-1])
        if solmu.edellinen.koordinaatit[0] == pos_x and solmu.edellinen.koordinaatit[1] > pos_y:
            if pos_y != 0:
                if kartta.taulukko[pos_y-1][pos_x] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y-1][pos_x])
#                    if kartta.taulukko[pos_y-1][pos_x] != 2:
#                        solmu.luonnolliset.append(self.solmut[pos_y-1][pos_x])
#                    else:
#                        solmu.pakolliset.append(self.solmut[pos_y-1][pos_x])
                if pos_x > 0:
                    if kartta.taulukko[pos_y][pos_x-1] == 3 and kartta.taulukko[pos_y-1][pos_x-1] != 3:
                        solmu.pakolliset.append(self.solmut[pos_y-1][pos_x-1])
                if pos_x < len(kartta.taulukko[0])-1:
                    if kartta.taulukko[pos_y][pos_x+1] == 3 and kartta.taulukko[pos_y-1][pos_x+1] != 3:
                        solmu.pakolliset.append(self.solmut[pos_y-1][pos_x+1])
        if solmu.edellinen.koordinaatit[0] < pos_x and solmu.edellinen.koordinaatit[1] < pos_y:
            if pos_x != len(kartta.taulukko[0])-1:
                if kartta.taulukko[pos_y][pos_x+1] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y][pos_x+1])
#                    if kartta.taulukko[pos_y][pos_x+1] != 2:
#                        solmu.luonnolliset.append(self.solmut[pos_y][pos_x+1])
#                    else:
#                        solmu.pakolliset.append(self.solmut[pos_y][pos_x+1])
                if kartta.taulukko[pos_y-1][pos_x] == 3 and kartta.taulukko[pos_y-1][pos_x+1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y-1][pos_x+1])
                if pos_y != len(kartta.taulukko)-1:
                    if kartta.taulukko[pos_y+1][pos_x+1] != 3:
                        solmu.luonnolliset.append(
                            self.solmut[pos_y+1][pos_x+1])
#                        if kartta.taulukko[pos_y+1][pos_x+1] != 2:
#                            solmu.luonnolliset.append(
#                                self.solmut[pos_y+1][pos_x+1])
#                        else:
#                            solmu.pakolliset.append(self.solmut[pos_y+1][pos_x+1])
            if pos_y != len(kartta.taulukko)-1:
                if kartta.taulukko[pos_y+1][pos_x] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y+1][pos_x])
#                    if kartta.taulukko[pos_y+1][pos_x] != 2:
#                        solmu.luonnolliset.append(self.solmut[pos_y+1][pos_x])
#                    else:
#                        solmu.pakolliset.append(self.solmut[pos_y+1][pos_x])
                if kartta.taulukko[pos_y][pos_x-1] == 3 and kartta.taulukko[pos_y+1][pos_x-1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y+1][pos_x-1])
        if solmu.edellinen.koordinaatit[0] < pos_x and solmu.edellinen.koordinaatit[1] > pos_y:
            if pos_x != len(kartta.taulukko[0])-1:
                if kartta.taulukko[pos_y][pos_x+1] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y][pos_x+1])
#                    if kartta.taulukko[pos_y][pos_x+1] != 2:
#                        solmu.luonnolliset.append(self.solmut[pos_y][pos_x+1])
#                    else:
#                        solmu.pakolliset.append(self.solmut[pos_y][pos_x+1])
                if kartta.taulukko[pos_y+1][pos_x] == 3 and kartta.taulukko[pos_y+1][pos_x+1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y+1][pos_x+1])
                if pos_y != 0:
                    if kartta.taulukko[pos_y-1][pos_x+1] != 3:
                        solmu.luonnolliset.append(
                            self.solmut[pos_y-1][pos_x+1])
#                        if kartta.taulukko[pos_y-1][pos_x+1] != 2:
#                            solmu.luonnolliset.append(
#                                self.solmut[pos_y-1][pos_x+1])
#                        else:
#                            solmu.pakolliset.append(self.solmut[pos_y-1][pos_x+1])
            if pos_y != 0:
                if kartta.taulukko[pos_y-1][pos_x] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y-1][pos_x])
#                    if kartta.taulukko[pos_y-1][pos_x] != 2:
#                        solmu.luonnolliset.append(self.solmut[pos_y-1][pos_x])
#                    else:
#                        solmu.pakolliset.append(self.solmut[pos_y-1][pos_x])
                if kartta.taulukko[pos_y][pos_x-1] == 3 and kartta.taulukko[pos_y-1][pos_x-1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y-1][pos_x-1])
        if solmu.edellinen.koordinaatit[0] > pos_x and solmu.edellinen.koordinaatit[1] > pos_y:
            if pos_x != 0:
                if kartta.taulukko[pos_y][pos_x-1] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y][pos_x-1])
#                    if kartta.taulukko[pos_y][pos_x-1] != 2:
#                        solmu.luonnolliset.append(self.solmut[pos_y][pos_x-1])
#                    else:
#                        solmu.pakolliset.append(self.solmut[pos_y][pos_x-1])
                if kartta.taulukko[pos_y+1][pos_x] == 3 and kartta.taulukko[pos_y+1][pos_x-1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y+1][pos_x-1])
                if pos_y != 0:
                    if kartta.taulukko[pos_y-1][pos_x-1] != 3:
                        solmu.luonnolliset.append(
                            self.solmut[pos_y-1][pos_x-1])
#                        if kartta.taulukko[pos_y-1][pos_x-1] != 2:
#                            solmu.luonnolliset.append(
#                                self.solmut[pos_y-1][pos_x-1])
#                        else:
#                            solmu.pakolliset.append(self.solmut[pos_y-1][pos_x-1])
            if pos_y != 0:
                if kartta.taulukko[pos_y-1][pos_x] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y-1][pos_x])
#                    if kartta.taulukko[pos_y-1][pos_x] != 2:
#                        solmu.luonnolliset.append(self.solmut[pos_y-1][pos_x])
#                    else:
#                        solmu.pakolliset.append(self.solmut[pos_y-1][pos_x])
                if kartta.taulukko[pos_y][pos_x+1] == 3 and kartta.taulukko[pos_y-1][pos_x+1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y-1][pos_x+1])
        if solmu.edellinen.koordinaatit[0] > pos_x and solmu.edellinen.koordinaatit[1] < pos_y:
            if pos_x != 0:
                if kartta.taulukko[pos_y][pos_x-1] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y][pos_x-1])
#                    if kartta.taulukko[pos_y][pos_x-1] != 2:
#                        solmu.luonnolliset.append(self.solmut[pos_y][pos_x-1])
#                    else:
#                        solmu.pakolliset.append(self.solmut[pos_y][pos_x-1])
                if kartta.taulukko[pos_y-1][pos_x] == 3 and kartta.taulukko[pos_y-1][pos_x-1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y-1][pos_x-1])
                if pos_y != len(kartta.taulukko)-1:
                    if kartta.taulukko[pos_y+1][pos_x-1] != 3:
                        solmu.luonnolliset.append(
                            self.solmut[pos_y+1][pos_x-1])
#                        if kartta.taulukko[pos_y+1][pos_x-1] != 2:
#                            solmu.luonnolliset.append(
#                                self.solmut[pos_y+1][pos_x-1])
#                        else:
#                            solmu.pakolliset.append(self.solmut[pos_y+1][pos_x-1])
            if pos_y != len(kartta.taulukko)-1:
                if kartta.taulukko[pos_y+1][pos_x] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y+1][pos_x])
#                    if kartta.taulukko[pos_y+1][pos_x] != 2:
#                        solmu.luonnolliset.append(self.solmut[pos_y+1][pos_x])
#                    else:
#                        solmu.pakolliset.append(self.solmut[pos_y+1][pos_x])
                if kartta.taulukko[pos_y][pos_x+1] == 3 and kartta.taulukko[pos_y+1][pos_x+1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y+1][pos_x+1])

    def suunta(self, nykyinen, seuraava):

        # Määrittelee suunnan, johon haku liikkuu.

        nykyx = nykyinen.koordinaatit[0]
        nykyy = nykyinen.koordinaatit[1]
        seurx = seuraava.koordinaatit[0]
        seury = seuraava.koordinaatit[1]
        if nykyx < seurx and nykyy == seury:
            return 0
        elif nykyx < seurx and nykyy > seury:
            return 1
        elif nykyx == seurx and nykyy > seury:
            return 2
        elif nykyx > seurx and nykyy > seury:
            return 3
        elif nykyx > seurx and nykyy == seury:
            return 4
        elif nykyx > seurx and nykyy < seury:
            return 5
        elif nykyx == seurx and nykyy < seury:
            return 6
        elif nykyx < seurx and nykyy < seury:
            return 7

    def hyppy(self, solmu, suunta):

        # JPS:n tarvitsema hyppyfunktio.

        pos_x = solmu.koordinaatit[0]
        pos_y = solmu.koordinaatit[1]
        seuraava = None
        if suunta == 0 and pos_x != len(kartta.taulukko[0])-1:
            seuraava = self.solmut[pos_y][pos_x+1]
        if suunta == 1 and pos_x != len(kartta.taulukko[0])-1 and pos_y != 0:
            seuraava = self.solmut[pos_y-1][pos_x+1]
        if suunta == 2 and pos_y != 0:
            seuraava = self.solmut[pos_y-1][pos_x]
        if suunta == 3 and pos_x != 0 and pos_y != 0:
            seuraava = self.solmut[pos_y-1][pos_x-1]
        if suunta == 4 and pos_x != 0:
            seuraava = self.solmut[pos_y][pos_x-1]
        if suunta == 5 and pos_x != 0 and pos_y != len(kartta.taulukko)-1:
            seuraava = self.solmut[pos_y+1][pos_x-1]
        if suunta == 6 and pos_y != len(kartta.taulukko)-1:
            seuraava = self.solmut[pos_y+1][pos_x]
        if suunta == 7 and pos_x != len(kartta.taulukko[0])-1 and pos_y != len(kartta.taulukko)-1:
            seuraava = self.solmut[pos_y+1][pos_x+1]
        if seuraava == None:
            return None
        if seuraava.tyyppi == 3:
            return None
        if seuraava.hyppypiste:
            return None
        seuraava.tutkittu = True
        if seuraava.etaisyys == None:
            seuraava.edellinen = solmu
            if suunta in [1, 3, 5, 7]:
                seuraava.etaisyys = solmu.etaisyys + 7
            else:
                seuraava.etaisyys = solmu.etaisyys + 5
        elif seuraava.etaisyys != None:
            if suunta in [1, 3, 5, 7]:
                uusi = solmu.etaisyys + 7
            else:
                uusi = solmu.etaisyys + 5
            if uusi < seuraava.etaisyys:
                seuraava.etaisyys = uusi
                seuraava.edellinen = solmu
        self.karsi_naapurit(seuraava)
        if seuraava.koordinaatit == self.loppusolmu.koordinaatit:
            return seuraava
        if len(seuraava.pakolliset) > 0:
            return seuraava
        if suunta == 1:
            if self.hyppy(seuraava, 0) != None:
                return seuraava
            if self.hyppy(seuraava, 2) != None:
                return seuraava
        if suunta == 3:
            if self.hyppy(seuraava, 2) != None:
                return seuraava
            if self.hyppy(seuraava, 4) != None:
                return seuraava
        if suunta == 5:
            if self.hyppy(seuraava, 4) != None:
                return seuraava
            if self.hyppy(seuraava, 6) != None:
                return seuraava
        if suunta == 7:
            if self.hyppy(seuraava, 6) != None:
                return seuraava
            if self.hyppy(seuraava, 0) != None:
                return seuraava
        return self.hyppy(seuraava, suunta)

    def tunnista_seuraavat(self, solmu):

        # JPS:n tarvitsema funktio seuraavien hyppypisteiden tunnistamista varten.

        if solmu.koordinaatit != self.alkusolmu.koordinaatit:
            for i in solmu.pakolliset:
                solmu.naapurit.append(i)
            for i in solmu.luonnolliset:
                solmu.naapurit.append(i)

        for naapuri in solmu.naapurit:
            seuraava = self.hyppy(solmu, self.suunta(solmu, naapuri))
            if seuraava != None:
                solmu.seuraajat.append(seuraava)
                seuraava.hyppypiste = True
                self.hyppypisteet.append(seuraava)
        return solmu.seuraajat

    def reitinhaku(self):

        # JPS-algoritmi. Tämä käyttää apunaan tunnista_seuraavat-funktiota.
        # Funktio tunnista_seuraavat vuorostaan käyttää funktioita hyppy ja suunta.
        # Funktio hyppy käyttää funktiota karsi_naapurit.

        alku = time.time()

        self.luo_solmut()

        stack = DiagonalFirstPrio(self.tunnista_seuraavat(self.alkusolmu))
        while True:
            if stack.pituus() == 0:
                break
            solmu = stack.poista_listasta()
#            if solmu.koordinaatit == self.loppusolmu.koordinaatit:
#                break
            for i in self.tunnista_seuraavat(solmu):
                stack.lisaa_listaan(i)

        loppu = time.time()

        # Piirretään löydetty polku kartalle:
        solmu = self.loppusolmu
        while True:
            solmu = solmu.edellinen
            if solmu.koordinaatit == self.alkusolmu.koordinaatit:
                break
            pos_x = solmu.koordinaatit[0]
            pos_y = solmu.koordinaatit[1]
            kartta.taulukko[pos_y][pos_x] = 4

        # Alla olevalla koodilla saa piirrettyä löydetyt hyppypisteet kartalle.
#        for solmu in self.hyppypisteet:
#            if solmu.koordinaatit != self.loppusolmu.koordinaatit:
#                pos_x = solmu.koordinaatit[0]
#                pos_y = solmu.koordinaatit[1]
#                kartta.taulukko[pos_y][pos_x] = 5

        print()
        print("Jump Point Search: ")
        print(f"Polun pituus: {self.loppusolmu.etaisyys}")
        print(f"Aikaa kului: {loppu-alku} s.")
        print()
