import pickle
import os
from Magazzino.Prodotto import Prodotto
from Magazzino.Posizione import Posizione, occupa_posizione


class Bottiglia(Prodotto):

    def __init__(self, nome, prezzo, disponibilita, posizione):
        super(Bottiglia, self).__init__(nome, prezzo)
        self.disponibilita = disponibilita
        self.posizione = posizione

    def inserisci_bottiglia(self, nome, prezzo, posizione):
        self.nome = nome
        self.prezzo = prezzo
        self.posizione = posizione
        bottiglie = {}
        if os.path.isfile('Dati/lista_bottiglie_salvate.pickle'):
            with open('Dati/lista_bottiglie_salvate.pickle', 'rb') as f:
                bottiglie = pickle.load(f)
            bottiglie[nome] = self
            with open('Dati/lista_bottiglie_salvate.pickle', 'wb') as f:
                pickle.dump(bottiglie, f, pickle.HIGHEST_PROTOCOL)
        occupa_posizione(self.posizione)