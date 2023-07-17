import unittest

from GestoreMagazzino.Controller.GestoreMagazzino import GestoreMagazzino
from GestoreMagazzino.Model.Bottiglia import Bottiglia


class TestMagazzino(unittest.TestCase):

    def test_posizione_occupata(self):

        gestore = GestoreMagazzino()

        # Creazione di una bottiglia di prova e assegnazione di una posizione
        bottiglia = Bottiglia("Bottiglia di prova", 100, 50, 1, 1, 1)

        # Aggiunta della bottiglia al magazzino
        gestore.magazzino.aggiungi_bottiglia(bottiglia)

        # Verifica che la posizione sia occupata
        self.assertTrue(gestore.posizione_occupata(1, 1, 1))

        # Verifica che una posizione non occupata restituisca False
        self.assertFalse(gestore.posizione_occupata(3, 3, 3))

if __name__ == '__main__':
    unittest.main()