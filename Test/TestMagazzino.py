import unittest

from Gestione.GestoreMagazzino import GestoreMagazzino
from Magazzino.Bottiglia import Bottiglia
from Magazzino.Magazzino import Magazzino


class TestMagazzino(unittest.TestCase):

    def test_posizione_occupata(self):
        magazzino = Magazzino()
        gestore = GestoreMagazzino(magazzino)

        # Creazione di una bottiglia di prova e assegnazione di una posizione
        bottiglia = Bottiglia("Bottiglia di prova", 100, 50, 1, 1, 1)

        # Aggiunta della bottiglia al magazzino
        magazzino.aggiungi_bottiglia(bottiglia)

        # Verifica che la posizione sia occupata
        self.assertTrue(gestore.posizione_occupata(1, 1, 1))

        # Verifica che una posizione non occupata restituisca False
        self.assertFalse(gestore.posizione_occupata(2, 2, 2))

if __name__ == '__main__':
    unittest.main()