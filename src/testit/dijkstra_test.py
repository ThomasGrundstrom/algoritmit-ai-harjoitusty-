import unittest
from algoritmit.dijkstra import Dijkstra


class testDijkstra(unittest.TestCase):
    def setUp(self):
        self.dijkstra = Dijkstra()

    def test_alkuarvot(self):
        self.assertEqual(self.dijkstra.solmut, [])
        self.assertEqual(self.dijkstra.keko, [])
        self.assertEqual(self.dijkstra.alkusolmu, None)
        self.assertEqual(self.dijkstra.loppusolmu, None)
        self.assertEqual(self.dijkstra.polku, [])
