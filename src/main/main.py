import pygame
from tapahtumat.tapahtumat import tapahtumat
from kartta.kartta import kartta
from algoritmit.dijkstra import Dijkstra
from algoritmit.jps import Jps
from main.tila import tila


class Suorita:

    # Luokka, joka suorittaa ohjelman.

    def __init__(self):

        # Määritellään näytön koko, kello ja käytettävät värit.

        pygame.init()
        self.naytto = pygame.display.set_mode((800, 800))
        self.kello = pygame.time.Clock()
        self.musta = (0, 0, 0)
        self.harmaa = (50, 50, 50)
        self.vihrea = (0, 255, 0)
        self.punainen = (255, 0, 0)
        self.sininen = (0, 100, 255)

    def piirra_naytto(self):

        # Piirretään visualisointi kartasta.

        ruutu_x_pos = (800//len(kartta.taulukko[0]))
        ruutu_y_pos = (800//len(kartta.taulukko))
        ruutu_leveys = (800//len(kartta.taulukko[0])) - 2
        ruutu_korkeus = (800//len(kartta.taulukko)) - 2

        self.naytto.fill(self.musta)
        for j in range(len(kartta.taulukko)):
            for i in range(len(kartta.taulukko[0])):
                if kartta.taulukko[j][i] == 0:
                    pygame.draw.rect(self.naytto, self.harmaa,
                                     (i * ruutu_x_pos + 1, j * ruutu_y_pos + 1, ruutu_leveys, ruutu_korkeus))
                elif kartta.taulukko[j][i] == 1:
                    pygame.draw.rect(self.naytto, self.vihrea,
                                     (i * ruutu_x_pos + 1, j * ruutu_y_pos + 1, ruutu_leveys, ruutu_korkeus))
                elif kartta.taulukko[j][i] == 2:
                    pygame.draw.rect(self.naytto, self.punainen,
                                     (i * ruutu_x_pos + 1, j * ruutu_y_pos + 1, ruutu_leveys, ruutu_korkeus))
                elif kartta.taulukko[j][i] == 3:
                    pygame.draw.rect(self.naytto, self.musta,
                                     (i * ruutu_x_pos + 1, j * ruutu_y_pos + 1, ruutu_leveys, ruutu_korkeus))
                elif kartta.taulukko[j][i] == 4:
                    pygame.draw.rect(self.naytto, self.sininen,
                                     (i * ruutu_x_pos + 1, j * ruutu_y_pos + 1, ruutu_leveys, ruutu_korkeus))
        pygame.display.flip()
        self.kello.tick(60)

    def silmukka(self):

        # Suoritetaan toistuvat tapahtumat silmukassa.

        while True:
            self.piirra_naytto()
            tapahtumat.tutki_tapahtumat()
            if tila.tila == 1:
                Dijkstra().reitinhaku()
                tila.tila = 0
            if tila.tila == 2:
                Jps().reitinhaku()
                tila.tila = 0


suorita = Suorita()
