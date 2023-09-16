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
        self.vihrea = (0, 255, 0)
        self.punainen = (255, 0, 0)
        self.sininen = (0, 100, 255)


    def piirra_naytto(self):

        # Piirretään näyttö.

        self.naytto.fill(self.musta)
        for j in range(len(kartta.taulukko)):
            for i in range(len(kartta.taulukko[0])):
                if kartta.taulukko[j][i] == 0:
                    pygame.draw.rect(self.naytto, self.harmaa, (i * 20 + 1, j * 20 + 1, 18, 18))
                elif kartta.taulukko[j][i] == 1:
                    pygame.draw.rect(self.naytto, self.vihrea, (i * 20 + 1, j * 20 + 1, 18, 18))
                elif kartta.taulukko[j][i] == 2:
                    pygame.draw.rect(self.naytto, self.punainen, (i * 20 + 1, j * 20 + 1, 18, 18))
        pygame.display.flip()
        self.kello.tick(1)
    

    def silmukka(self):

        # Suoritetaan toistuvat tapahtumat silmukassa.

        while True:
            self.piirra_naytto()
            tapahtumat.tutki_tapahtumat()


suorita = Suorita()