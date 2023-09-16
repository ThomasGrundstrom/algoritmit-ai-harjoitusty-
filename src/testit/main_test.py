import unittest
import pygame
from main.main import Suorita


class TestSuorita(unittest.TestCase):
    def setUp(self):
        self.suorita = Suorita()
    

    def test_naytto_alkuarvot(self):
        self.assertEqual(self.suorita.naytto.get_width(), 800)
        self.assertEqual(self.suorita.naytto.get_height(), 800)
        self.assertEqual(self.suorita.musta, (0, 0, 0))
        self.assertEqual(self.suorita.harmaa, (50, 50, 50))
        self.assertEqual(self.suorita.vihrea, (0, 255, 0))
        self.assertEqual(self.suorita.punainen, (255, 0, 0))
        self.assertEqual(self.suorita.sininen, (0, 100, 255))
    
    
    def test_naytto_kaynnistys(self):
        self.suorita.piirra_naytto()
        self.assertEqual(self.suorita.naytto.get_at((0, 0)), self.suorita.musta)
        self.assertEqual(self.suorita.naytto.get_at((5, 5)), self.suorita.vihrea)
        self.assertEqual(self.suorita.naytto.get_at((25, 25)), self.suorita.harmaa)
        self.assertEqual(self.suorita.naytto.get_at((795, 795)), self.suorita.punainen)