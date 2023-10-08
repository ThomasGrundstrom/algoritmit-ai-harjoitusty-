import time
from kartta.kartta import kartta
from komponentit.jpssolmut import Jpssolmu


class Jps:

    # Luokka JPS-algoritmin toteutusta varten. Vaatii korjausta.

    def __init__(self):
        self.solmut = []
        self.alkusolmu = None
        self.loppusolmu = None
        self.polku = []
        self.hyppypisteet = []

    def luo_solmut(self):

        # Luodaan solmuista koostuva verkko, jota algoritmi voi käyttää.

        for j in range(len(kartta.taulukko)):
            rivi = []
            for i in range(len(kartta.taulukko[0])):
                rivi.append(Jpssolmu((i, j), kartta.taulukko[j][i]))
            self.solmut.append(rivi)
        for j in range(len(self.solmut)):
            for i in range(len(self.solmut[0])):
                if self.solmut[j][i].tyyppi == 1:
                    self.alkusolmu = self.solmut[j][i]
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
                if kartta.taulukko[pos_y-1][pos_x] == 3 and kartta.taulukko[pos_y-1][pos_x+1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y-1][pos_x+1])
                if pos_y != len(kartta.taulukko)-1:
                    if kartta.taulukko[pos_y+1][pos_x]+1 != 3:
                        solmu.luonnolliset.append(
                            self.solmut[pos_y+1][pos_x+1])
            if pos_y != len(kartta.taulukko)-1:
                if kartta.taulukko[pos_y+1][pos_x] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y+1][pos_x])
                if kartta.taulukko[pos_y][pos_x-1] == 3 and kartta.taulukko[pos_y+1][pos_x-1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y+1][pos_x-1])
        if solmu.edellinen.koordinaatit[0] < pos_x and solmu.edellinen.koordinaatit[1] > pos_y:
            if pos_x != len(kartta.taulukko[0])-1:
                if kartta.taulukko[pos_y][pos_x+1] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y][pos_x+1])
                if kartta.taulukko[pos_y+1][pos_x] == 3 and kartta.taulukko[pos_y+1][pos_x+1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y+1][pos_x+1])
                if pos_y != 0:
                    if kartta.taulukko[pos_y-1][pos_x+1] != 3:
                        solmu.luonnolliset.append(
                            self.solmut[pos_y-1][pos_x+1])
            if pos_y != 0:
                if kartta.taulukko[pos_y-1][pos_x] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y-1][pos_x])
                if kartta.taulukko[pos_y][pos_x-1] == 3 and kartta.taulukko[pos_y-1][pos_x-1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y-1][pos_x-1])
        if solmu.edellinen.koordinaatit[0] > pos_x and solmu.edellinen.koordinaatit[1] > pos_y:
            if pos_x != 0:
                if kartta.taulukko[pos_y][pos_x-1] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y][pos_x-1])
                if kartta.taulukko[pos_y+1][pos_x] == 3 and kartta.taulukko[pos_y+1][pos_x-1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y+1][pos_x-1])
                if pos_y != 0:
                    if kartta.taulukko[pos_y-1][pos_x-1] != 3:
                        solmu.luonnolliset.append(
                            self.solmut[pos_y-1][pos_x-1])
            if pos_y != 0:
                if kartta.taulukko[pos_y-1][pos_x] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y-1][pos_x])
                if kartta.taulukko[pos_y][pos_x+1] == 3 and kartta.taulukko[pos_y-1][pos_x+1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y-1][pos_x+1])
        if solmu.edellinen.koordinaatit[0] > pos_x and solmu.edellinen.koordinaatit[1] < pos_y:
            if pos_x != 0:
                if kartta.taulukko[pos_y][pos_x-1] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y][pos_x-1])
                if kartta.taulukko[pos_y-1][pos_x] == 3 and kartta.taulukko[pos_y-1][pos_x-1] != 3:
                    solmu.pakolliset.append(self.solmut[pos_y-1][pos_x-1])
                if pos_y != len(kartta.taulukko)-1:
                    if kartta.taulukko[pos_y+1][pos_x-1] != 3:
                        solmu.luonnolliset.append(
                            self.solmut[pos_y+1][pos_x-1])
            if pos_y != len(kartta.taulukko)-1:
                if kartta.taulukko[pos_y+1][pos_x] != 3:
                    solmu.luonnolliset.append(self.solmut[pos_y+1][pos_x])
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

        # JPS:n tarvitsema hyppyfunktio. Vastaa luentomateriaalista löytyvässä JPS-dokumentaatiossa olevaa algoritmia 2.

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
        if seuraava.jumppoint:
            return None
        seuraava.tutkittu = True
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

        # JPS:n tarvitsema funktio seuraavien hyppypisteiden tunnistamista varten. Vastaa JPS-dokumentaation algoritmia 1.

        if solmu.koordinaatit != self.alkusolmu.koordinaatit:
            for i in solmu.pakolliset:
                solmu.naapurit.append(i)
            for i in solmu.luonnolliset:
                solmu.naapurit.append(i)

        for naapuri in solmu.naapurit:
            seuraava = self.hyppy(solmu, self.suunta(solmu, naapuri))
            if seuraava != None:
                solmu.seuraajat.append(seuraava)
                seuraava.jumppoint = True
                self.hyppypisteet.append(seuraava)
        return solmu.seuraajat

    def reitinhaku(self):

        # JPS-algoritmi.

        self.luo_solmut()

        alku = time.time()

        stack = self.tunnista_seuraavat(self.alkusolmu)
        while True:
            if len(stack) == 0:
                break
            solmu = stack.pop(0)
            for i in self.tunnista_seuraavat(solmu):
                stack.append(i)

        loppu = time.time()

        solmu = self.loppusolmu
        while True:
            solmu = solmu.edellinen
            if solmu.koordinaatit == self.alkusolmu.koordinaatit:
                break
            pos_x = solmu.koordinaatit[0]
            pos_y = solmu.koordinaatit[1]
            kartta.taulukko[pos_y][pos_x] = 4
#        for solmu in self.hyppypisteet:
#            pos_x = solmu.koordinaatit[0]
#            pos_y = solmu.koordinaatit[1]
#            kartta.taulukko[pos_y][pos_x] = 5
        print(f"Aikaa kului: {loppu-alku} s")
