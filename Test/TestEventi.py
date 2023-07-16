import os.path
import pickle
import unittest

from GestoreEventi.Model.Evento import Evento
from GestoreEventi.Controller.GestoreEventi import GestoreEventi


class Test(unittest.TestCase):
    def setUp(self):
        self.gestore = GestoreEventi()
        self.gestore.lettura_eventi()

    def test_inserisci_evento(self):
        # Creazione di un evento di prova
        evento = Evento("Concerto", "08/07/2023", "Musica", 10, 20, 30)

        # Chiamata al metodo da testare
        self.gestore.inserisci_evento(evento)

        # Verifica dell'inserimento dell'evento nella lista degli eventi
        lista_eventi = self.gestore.get_lista_eventi()
        self.assertIn(evento, lista_eventi)

    def test_rimuovi_evento(self):
        evento = Evento("Evento1", "08/07/2023", "Concerto", 10, 50, 10)
        self.gestore.lista_eventi.append(evento)
        self.gestore.rimuovi_evento(evento)
        self.assertNotIn(evento, self.gestore.lista_eventi)

if __name__ == '__main__':
    unittest.main()



