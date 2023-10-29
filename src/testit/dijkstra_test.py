import unittest
from math import sqrt
from algoritmit.dijkstra import Dijkstra


class testDijkstra(unittest.TestCase):
    def setUp(self):
        self.dijkstra = Dijkstra(None)

    def test_alkuarvot(self):
        self.assertEqual(self.dijkstra.solmut, [])
        self.assertEqual(self.dijkstra.alkusolmu, None)
        self.assertEqual(self.dijkstra.loppusolmu, None)
        self.assertEqual(self.dijkstra.polku, [])

    def test_tapaukset(self):
        kartta = self.nollaa_kartta()
        self.dijkstra = Dijkstra(kartta)
        self.dijkstra.reitinhaku()
        self.assertEqual(f"{self.dijkstra.loppusolmu.etaisyys:.2f}", f"{80+99*sqrt(2):.2f}")
        kartta = self.nollaa_kartta()
        for j in range(25):
            if j != 0:
                for i in range(179):
                    kartta[j*4][i] = 3
        for j in range(1, 24):
            for i in range(1, 180):
                kartta[j*4+2][i] = 3
        self.dijkstra = Dijkstra(kartta)
        self.dijkstra.reitinhaku()
        self.assertEqual(f"{self.dijkstra.loppusolmu.etaisyys:.2f}", f"{175+46*177+5*sqrt(2)+91*sqrt(2)+3:.2f}")
        kartta = self.nollaa_kartta()
        for i in range(179):
            kartta[20][i] = 3
        self.dijkstra = Dijkstra(kartta)
        self.dijkstra.reitinhaku()
        self.assertEqual(f"{self.dijkstra.loppusolmu.etaisyys:.2f}", f"{159+20*sqrt(2)+79:.2f}")
        kartta = self.nollaa_kartta()
        kartta[99][179] = 0
        kartta[99][0] = 2
        for i in range(179):
            kartta[20][i] = 3
        self.dijkstra = Dijkstra(kartta)
        self.dijkstra.reitinhaku()
        self.assertEqual(f"{self.dijkstra.loppusolmu.etaisyys:.2f}", f"{159+99*sqrt(2)+100:.2f}")
        kartta = self.nollaa_kartta()
        for j in range(25):
            if j != 0:
                for i in range(179):
                    kartta[j*4][i] = 3
        self.dijkstra = Dijkstra(kartta)
        self.dijkstra.reitinhaku()
        self.assertEqual(f"{self.dijkstra.loppusolmu.etaisyys:.2f}", f"{175+4*sqrt(2)+95:.2f}")
        kartta = self.nollaa_kartta()
        kartta[99][179] = 0
        kartta[99][0] = 2
        for j in range(25):
            if j != 0:
                for i in range(179):
                    kartta[j*4][i] = 3
        self.dijkstra = Dijkstra(kartta)
        self.dijkstra.reitinhaku()
        self.assertEqual(f"{self.dijkstra.loppusolmu.etaisyys:.2f}", f"{175+92+176+7*sqrt(2):.2f}")
        kartta = self.nollaa_kartta()
        for j in range(25):
            for i in range(1, 179):
                kartta[j*4+2][i] = 3
        self.dijkstra = Dijkstra(kartta)
        self.dijkstra.reitinhaku()
        self.assertEqual(f"{self.dijkstra.loppusolmu.etaisyys:.2f}", f"{94+175+1+4*sqrt(2):.2f}")
        kartta = self.nollaa_kartta()
        for j in range(25):
            if j != 0:
                for i in range(1, 179):
                    kartta[j*2][i] = 3
        self.dijkstra = Dijkstra(kartta)
        self.dijkstra.reitinhaku()
        self.assertEqual(f"{self.dijkstra.loppusolmu.etaisyys:.2f}", f"{48+128+51*sqrt(2):.2f}")
        kartta = self.nollaa_kartta()
        for j in range(50):
            for i in range(1, 179):
                kartta[j*2][i] = 3
        self.dijkstra = Dijkstra(kartta)
        self.dijkstra.reitinhaku()
        self.assertEqual(f"{self.dijkstra.loppusolmu.etaisyys:.2f}", f"{97+177+2*sqrt(2):.2f}")
        kartta = self.nollaa_kartta()
        for i in range(39):
            kartta[20][i] = 3
        for i in range(20, 98):
            kartta[i][39] = 3
        kartta[99][179] = 0
        kartta[39][0] = 2
        self.dijkstra = Dijkstra(kartta)
        self.dijkstra.reitinhaku()
        self.assertEqual(f"{self.dijkstra.loppusolmu.etaisyys:.2f}", f"{19+78+20+60*sqrt(2):.2f}")
        kartta = self.nollaa_kartta()
        for j in range(1, 50):
            for i in range(1, 90):
                kartta[j*2][i*2] = 3
        self.dijkstra = Dijkstra(kartta)
        self.dijkstra.reitinhaku()
        self.assertEqual(f"{self.dijkstra.loppusolmu.etaisyys:.2f}", f"{80+99*sqrt(2):.2f}")
        kartta = self.nollaa_kartta()
        for j in range(len(kartta)):
            kartta[j][5] = 3
        self.dijkstra = Dijkstra(kartta)
        self.dijkstra.reitinhaku()
        self.assertEqual(self.dijkstra.loppusolmu.etaisyys, float("inf"))

    def nollaa_kartta(self):
        kartta = [[0 for i in range(180)] for j in range(100)]
        kartta[0][0] = 1
        kartta[99][179] = 2
        return kartta
