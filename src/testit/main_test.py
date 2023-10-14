import unittest
import pygame
from main.main import Suorita
from kartta.kartta import Kartta


class TestSuorita(unittest.TestCase):
    def setUp(self):
        self.suorita = Suorita()
        self.kartta = Kartta()

    def test_naytto_alkuarvot(self):
        self.assertEqual(self.suorita.leveys, len(self.kartta.taulukko[0])*10)
        self.assertEqual(self.suorita.korkeus, len(self.kartta.taulukko)*10)
        self.assertEqual(self.suorita.musta, (0, 0, 0))
        self.assertEqual(self.suorita.harmaa, (50, 50, 50))
        self.assertEqual(self.suorita.vihrea, (0, 255, 0))
        self.assertEqual(self.suorita.punainen, (255, 0, 0))
        self.assertEqual(self.suorita.sininen, (0, 100, 255))
        self.assertEqual(self.suorita.valkoinen, (255, 255, 255))
