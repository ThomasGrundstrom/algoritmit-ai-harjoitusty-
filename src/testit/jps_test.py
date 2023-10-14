import unittest
from algoritmit.jps import Jps


class TestJps(unittest.TestCase):
    def setUp(self):
        self.jps = Jps(None)

    def test_tapaukset(self):
        kartta = self.nollaa_kartta()
        self.jps = Jps(kartta)
        self.jps.reitinhaku()
        self.assertEqual(self.jps.loppusolmu.etaisyys, 1093)
        kartta = self.nollaa_kartta()
        for j in range(25):
            if j != 0:
                for i in range(179):
                    kartta[j*4][i] = 3
        for j in range(1, 24):
            for i in range(1, 180):
                kartta[j*4+2][i] = 3
        self.jps = Jps(kartta)
        self.jps.reitinhaku()
        self.assertEqual(self.jps.loppusolmu.etaisyys, 42272)
        kartta = self.nollaa_kartta()
        for i in range(179):
            kartta[20][i] = 3
        self.jps = Jps(kartta)
        self.jps.reitinhaku()
        self.assertEqual(self.jps.loppusolmu.etaisyys, 1330)
        kartta = self.nollaa_kartta()
        kartta[99][179] = 0
        kartta[99][0] = 2
        for i in range(179):
            kartta[20][i] = 3
        self.jps = Jps(kartta)
        self.jps.reitinhaku()
        self.assertEqual(self.jps.loppusolmu.etaisyys, 1988)
        kartta = self.nollaa_kartta()
        for j in range(25):
            if j != 0:
                for i in range(179):
                    kartta[j*4][i] = 3
        self.jps = Jps(kartta)
        self.jps.reitinhaku()
        self.assertEqual(self.jps.loppusolmu.etaisyys, 1378)
        kartta = self.nollaa_kartta()
        kartta[99][179] = 0
        kartta[99][0] = 2
        for j in range(25):
            if j != 0:
                for i in range(179):
                    kartta[j*4][i] = 3
        self.jps = Jps(kartta)
        self.jps.reitinhaku()
        self.assertEqual(self.jps.loppusolmu.etaisyys, 2264)
        kartta = self.nollaa_kartta()
        for j in range(25):
            for i in range(1, 179):
                kartta[j*4+2][i] = 3
        self.jps = Jps(kartta)
        self.jps.reitinhaku()
        self.assertEqual(self.jps.loppusolmu.etaisyys, 1378)
        kartta = self.nollaa_kartta()
        for j in range(25):
            if j != 0:
                for i in range(1, 179):
                    kartta[j*2][i] = 3
        self.jps = Jps(kartta)
        self.jps.reitinhaku()
        self.assertEqual(self.jps.loppusolmu.etaisyys, 1237)
        kartta = self.nollaa_kartta()
        for j in range(50):
            for i in range(1, 179):
                kartta[j*2][i] = 3
        self.jps = Jps(kartta)
        self.jps.reitinhaku()
        self.assertEqual(self.jps.loppusolmu.etaisyys, 1384)
        kartta = self.nollaa_kartta()
        for i in range(39):
            kartta[20][i] = 3
        for i in range(20, 98):
            kartta[i][39] = 3
        kartta[99][179] = 0
        kartta[39][0] = 2
        self.jps = Jps(kartta)
        self.jps.reitinhaku()
        self.assertEqual(self.jps.loppusolmu.etaisyys, 1005)

    def nollaa_kartta(self):
        kartta = [[0 for i in range(180)] for j in range(100)]
        kartta[0][0] = 1
        kartta[99][179] = 2
        return kartta
