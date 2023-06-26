import pickle
import os
from Magazzino.Prodotto import Prodotto
from Magazzino.Posizione import Posizione


class Bottiglia(Prodotto):

    def __init__(self, nome, prezzo, disponibilita, corridoio, scaffale, piano):
        super(Bottiglia, self).__init__(nome, prezzo)
        self.disponibilita = disponibilita
        self.corridoio = corridoio
        self.scaffale = scaffale
        self.piano = piano


    def inserisci_bottiglia(self, nome, prezzo, disponibilita, corridoio, scaffale, piano):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibilita = disponibilita
        self.posizione = Posizione(corridoio, scaffale, piano)
        bottiglie = []
        if os.path.isfile('Dati/lista_bottiglie_salvate.pickle'):
            with open('Dati/lista_bottiglie_salvate.pickle', 'rb') as f:
                bottiglie = pickle.load(f)
        bottiglie.append(self)
        with open('Dati/lista_bottiglie_salvate.pickle', 'wb') as f:
            pickle.dump(bottiglie, f, pickle.HIGHEST_PROTOCOL)
        self.posizione.occupa_posizione(corridoio, scaffale, piano)

    # Metodi che servono per il prelievo delle bottiglie
    def get_disponibilta_bottiglia(self):
        return self.disponibilita

    def set_disponibilita_bottiglia(self, nuova_disponibilita):
        self.disponibilita = nuova_disponibilita