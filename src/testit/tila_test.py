import unittest
from main.tila import Tila

class testTila(unittest.TestCase):
    def setUp(self):
        self.tila = Tila()
    

    def test_alkutila(self):
        self.assertEqual(self.tila.tila, 0)
