import pygame
from main.tila import tila


class Tapahtumat:

    # Luokka, joka tutkii ohjelman saamat syötteet.

    def __init__(self):

        # Määritellään pygame.

        pygame.init()

    def tutki_tapahtumat(self):

        # Tutkitaan tapahtumat.

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                return "click"
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_d:
                    tila.tila = 1


tapahtumat = Tapahtumat()
