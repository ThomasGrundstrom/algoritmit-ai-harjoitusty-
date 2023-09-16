from kartta.kartta import kartta
from komponentit.solmut import Solmu
from komponentit.kaaret import Kaari
import heapq


class Dijkstra:

    # Luokka, jolla toteutetaan Dijkstran algoritmi.

    def __init__(self):
        self.solmut = [[] for i in range(len(kartta.taulukko))]
        self.kaaret = [[[] for i in range(len(kartta.taulukko[0]))] for j in range(len(kartta.taulukko))]
        self.kasitelty = [[False for i in range(len(kartta.taulukko[0]))] for j in range(len(kartta.taulukko))]
        self.keko = []
    

    def luo_verkko(self):

        # Luodaan solmuista ja kaarista koostuva verkko, jota algoritmi voi käyttää.

        for j in range(len(kartta.taulukko)):
            for i in range(len(kartta.taulukko[0])):
                if kartta.taulukko[j][i] == 1:
                    self.solmut[j].append(Solmu((j, i), 0))
                else:
                    self.solmut[j].append(Solmu((j, i), float("inf")))
        for j in range(len(self.kaaret)):
            for i in range(len(self.kaaret[0])):
                if j > 0 and j < len(kartta.taulukko) - 1:
                    self.kaaret[j][i].append(Kaari(self.solmut[j+1][i], 5))
                    self.kaaret[j][i].append(Kaari(self.solmut[j-1][i], 5))
                if i > 0 and i < len(kartta.taulukko[0]) - 1:
                    self.kaaret[j][i].append(Kaari(self.solmut[j][i+1], 5))
                    self.kaaret[j][i].append(Kaari(self.solmut[j][i-1], 5))
                if j == 0:
                    self.kaaret[j][i].append(Kaari(self.solmut[j+1][i], 5))
                if j == len(kartta.taulukko) - 1:
                    self.kaaret[j][i].append(Kaari(self.solmut[j-1][i], 5))
                if i == 0:
                    self.kaaret[j][i].append(Kaari(self.solmut[j][i+1], 5))
                if i == len(kartta.taulukko[0]) - 1:
                    self.kaaret[j][i].append(Kaari(self.solmut[j][i-1], 5))
                if j > 0 and j < len(kartta.taulukko) - 1 and i > 0 and i < len(kartta.taulukko[0]) - 1:
                    self.kaaret[j][i].append(Kaari(self.solmut[j+1][i+1], 7))
                    self.kaaret[j][i].append(Kaari(self.solmut[j-1][i-1], 7))
                    self.kaaret[j][i].append(Kaari(self.solmut[j+1][i-1], 7))
                    self.kaaret[j][i].append(Kaari(self.solmut[j-1][i+1], 7))
                self.kaaret[0][0].append(Kaari(self.solmut[1][1], 7))
                self.kaaret[0][len(kartta.taulukko[0])-1].append(Kaari(self.solmut[1][len(kartta.taulukko[0])-2], 7))
                self.kaaret[len(kartta.taulukko)-1][0].append(Kaari(self.solmut[len(kartta.taulukko)-2][1], 7))
                self.kaaret[len(kartta.taulukko)-1][len(kartta.taulukko[0])-1].append(Kaari(self.solmut[len(kartta.taulukko)-2][len(kartta.taulukko[0])-2], 7))
    

    def reitinhaku(self):

        # Varsinainen Dijkstran algoritmi.

        self.luo_verkko()
        heapq.heappush(self.keko, (0, (0, 0)))
        while len(self.keko) != 0:
            solmu = heapq.heappop(self.keko)[1]
            if self.kasitelty[solmu[0]][solmu[1]]:
                continue
            self.kasitelty[solmu[0]][solmu[1]] = True
            for kaari in self.kaaret[solmu[0]][solmu[1]]:
                nyky = kaari.loppu.etaisyys
                uusi = self.solmut[solmu[0]][solmu[1]].etaisyys + kaari.pituus
                if uusi < nyky:
                    kaari.loppu.etaisyys = uusi
                    heapq.heappush(keko, (uusi, kaari.loppu.koordinaatit))