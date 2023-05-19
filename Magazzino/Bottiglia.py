import pickle
import os
from Magazzino.Prodotto import Prodotto
from Magazzino.Posizione import Posizione, occupa_posizione


class Bottiglia(Prodotto):

    def __init__(self, nome, prezzo, disponibilita):
        super(Bottiglia, self).__init__(nome, prezzo)
        self.disponibilita = disponibilita
        self.posizione_bottiglia = ''

    def inserisci_bottiglia(self, nome, prezzo, disponibilita, corridoio, scaffale, piano):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibilita = disponibilita
        self.posizione_bottiglia = Posizione(corridoio, scaffale, piano)
        bottiglie = {}
        if os.path.isfile('Dati/lista_bottiglie_salvate.pickle'):
            with open('Dati/lista_bottiglie_salvate.pickle', 'rb') as f:
                bottiglie = pickle.load(f)
        bottiglie[nome] = self
        with open('Dati/lista_bottiglie_salvate.pickle', 'wb') as f:
            pickle.dump(bottiglie, f, pickle.HIGHEST_PROTOCOL)
        occupa_posizione(corridoio, scaffale, piano)

    def preleva_bottiglia(self, lista_bottiglie_salvate, nome_prodotto):
        for bottiglia in lista_bottiglie_salvate:
            if bottiglia.nome == nome_prodotto:
                if bottiglia.disponibilita > 0:
                    bottiglia.disponibilita -= 1




