import unittest
import pygame
from tapahtumat.tapahtumat import Tapahtumat


class TestTapahtumat(unittest.TestCase):
    def setUp(self):
        self.tapahtumat = Tapahtumat()

    def test_hiirinappain(self):
        self.assertEqual(self.tapahtumat.tutki_tapahtumat(), None)
        pygame.event.post(pygame.event.Event(
            pygame.MOUSEBUTTONDOWN, pos=(0, 0)))
        self.assertEqual(self.tapahtumat.tutki_tapahtumat(), "click")
