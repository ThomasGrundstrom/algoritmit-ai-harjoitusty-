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
        self.leveys = len(kartta.taulukko[0])*10
        self.korkeus = len(kartta.taulukko)*10
        self.naytto = pygame.display.set_mode((self.leveys, self.korkeus))
        self.kello = pygame.time.Clock()
        self.musta = (0, 0, 0)
        self.harmaa = (50, 50, 50)
        self.vihrea = (0, 255, 0)
        self.punainen = (255, 0, 0)
        self.sininen = (0, 100, 255)
        self.valkoinen = (255, 255, 255)

    def piirra_naytto(self):

        # Piirretään visualisointi kartasta.

        ruutu_x_pos = (self.leveys//len(kartta.taulukko[0]))
        ruutu_y_pos = (self.korkeus//len(kartta.taulukko))
        ruutu_leveys = (self.leveys//len(kartta.taulukko[0]))-2
        ruutu_korkeus = (self.korkeus//len(kartta.taulukko))-2

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
                elif kartta.taulukko[j][i] == 5:
                    pygame.draw.rect(self.naytto, self.valkoinen, (i * ruutu_x_pos + 1,
                                     j * ruutu_y_pos + 1, ruutu_leveys, ruutu_korkeus))
        pygame.display.flip()
        self.kello.tick(60)

    def nollaa_piirretyt_polut(self):

        # Poistetaan löydetty polku kartalta.

        for j in range(len(kartta.taulukko)):
            for i in range(len(kartta.taulukko[j])):
                if kartta.taulukko[j][i] == 4:
                    kartta.taulukko[j][i] = 0
                elif kartta.taulukko[j][i] == 5:
                    kartta.taulukko[j][i] = 0

    def silmukka(self):

        # Suoritetaan toistuvat tapahtumat silmukassa.

        while True:
            self.piirra_naytto()
            tapahtumat.tutki_tapahtumat()
            if tila.tila == 1:
                Dijkstra(kartta.taulukko).reitinhaku()
                tila.tila = 0
            if tila.tila == 2:
                Jps(kartta.taulukko).reitinhaku()
                tila.tila = 0
            if tila.tila == 3:
                self.nollaa_piirretyt_polut()
                tila.tila = 0


suorita = Suorita()
