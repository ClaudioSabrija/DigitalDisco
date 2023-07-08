import unittest

from Magazzino.Bottiglia import Bottiglia
from Magazzino.Magazzino import Magazzino


class Test(unittest.TestCase):
    def setUp(self):
        self.magazzino = Magazzino()

    def test_aggiungi_bottiglia(self):
        bottiglia = Bottiglia("Bottiglia1", 100, 10, 1, 2, 3)
        self.magazzino.aggiungi_bottiglia(bottiglia)

        # Verifica che la bottiglia sia stata aggiunta correttamente alla lista delle bottiglie
        self.assertIn(bottiglia, self.magazzino.get_lista_bottiglie())

        # Verifica che la bottiglia sia stata correttamente aggiunta alla lista delle bottiglie
        bottiglie_magazzino = self.magazzino.get_lista_bottiglie()
        self.assertTrue(any(
            b.nome == "Bottiglia1" and
            b.prezzo == 100 and
            b.disponibilita == 10 and
            b.corridoio == 1 and
            b.scaffale == 2 and
            b.piano == 3
            for b in bottiglie_magazzino))

    def test_set_disponibilita_bottiglia(self):
        bottiglia = Bottiglia("Bottiglia2", 15, 50, 4, 5, 6)
        bottiglia.set_disponibilita_bottiglia(75)

        # Verifica che la disponibilità della bottiglia sia stata impostata correttamente
        self.assertEqual(bottiglia.get_disponibilta_bottiglia(), 75)

