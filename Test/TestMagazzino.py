import unittest
from Magazzino.Bottiglia import Bottiglia
from Magazzino.Magazzino import Magazzino


class TestMagazzino(unittest.TestCase):

    def test_posizione_occupata(self):
        magazzino = Magazzino()

        # Creazione di una bottiglia di prova e assegnazione di una posizione
        bottiglia = Bottiglia("Bottiglia di prova", 100, 50, 1, 1, 1)

        # Aggiunta della bottiglia al magazzino
        magazzino.aggiungi_bottiglia(bottiglia)

        # Verifica che la posizione sia occupata
        self.assertTrue(magazzino.posizione_occupata(1, 1, 1))

        # Verifica che una posizione non occupata restituisca False
        self.assertFalse(magazzino.posizione_occupata(2, 2, 2))

if __name__ == '__main__':
    unittest.main()