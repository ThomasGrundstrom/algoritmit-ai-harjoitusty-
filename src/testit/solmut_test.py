import unittest
from komponentit.solmut import Solmu


class testSolmu(unittest.TestCase):
    def setUp(self):
        self.solmu = Solmu((0, 0), 1)
    

    def test_alkuarvot(self):
        self.assertEqual(self.solmu.koordinaatit, (0, 0))
        self.assertEqual(self.solmu.tyyppi, 1)
        self.assertEqual(self.solmu.etaisyys, float("inf"))
        self.assertEqual(self.solmu.kasitelty, False)
        self.assertEqual(self.solmu.naapurit, [])
        self.assertEqual(self.solmu.edellinen, None)
        self.assertEqual(self.solmu.keossa, False)

