import pygame
from tapahtumat.tapahtumat import tapahtumat
from kartta.kartta import kartta


class Suorita:

    # Luokka, joka suorittaa ohjelman.

    def __init__(self):

        # Määritellään näytön koko, kello ja käytettävät värit.

        pygame.init()
        self.naytto = pygame.display.set_mode((800, 800))
        self.kello = pygame.time.Clock()
        self.musta = (0, 0, 0)
        self.harmaa = (50, 50, 50)


    def piirra_naytto(self):

        # Piirretään näyttö.

        self.naytto.fill(self.musta)
        for i in range(len(kartta.taulukko)):
            for j in range(len(kartta.taulukko)):
                if kartta.taulukko[i][j] == 0:
                    pygame.draw.rect(self.naytto, self.harmaa, (i * 20 + 1, j * 20 + 1, 18, 18))
        pygame.display.flip()
        self.kello.tick(1)
    

    def silmukka(self):

        # Suoritetaan toistuvat tapahtumat silmukassa.

        while True:
            self.piirra_naytto()
            tapahtumat.tutki_tapahtumat()


suorita = Suorita()