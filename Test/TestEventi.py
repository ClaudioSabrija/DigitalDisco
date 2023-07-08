import os.path
import pickle
import unittest

from Evento.Evento import Evento
from Gestione.GestoreEventi import GestoreEventi


class Test(unittest.TestCase):
    def setUp(self):
        self.gestore = GestoreEventi()
        self.gestore.lettura_eventi()

    def test_rimuovi_evento(self):
        evento = Evento("Evento1", "2023-07-08", "Concerto", 10.0, 50.0, 100.0)
        self.gestore.lista_eventi.append(evento)
        self.gestore.rimuovi_evento(evento)
        self.assertNotIn(evento, self.gestore.lista_eventi)

if __name__ == '__main__':
    unittest.main()



