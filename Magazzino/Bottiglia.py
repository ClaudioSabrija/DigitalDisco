import pickle
import os
from Magazzino.Prodotto import Prodotto
from Magazzino.Posizione import Posizione


class Bottiglia(Prodotto):

    def __init__(self, nome, prezzo, disponibilita, corridoio, scaffale, piano):
        super(Bottiglia, self).__init__(nome, prezzo)
        self.posizione = Posizione(corridoio, scaffale, piano)
        self.disponibilita = disponibilita
        self.posizione_bottiglia = ''
        self.corridoio = corridoio
        self.scaffale = scaffale
        self.piano = piano


    def inserisci_bottiglia(self, nome, prezzo, disponibilita, corridoio, scaffale, piano):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibilita = disponibilita
        self.posizione_bottiglia = Posizione(corridoio, scaffale, piano)
        bottiglie = []
        if os.path.isfile('Dati/lista_bottiglie_salvate.pickle'):
            with open('Dati/lista_bottiglie_salvate.pickle', 'rb') as f:
                bottiglie = pickle.load(f)
        bottiglie.append(self)
        with open('Dati/lista_bottiglie_salvate.pickle', 'wb') as f:
            pickle.dump(bottiglie, f, pickle.HIGHEST_PROTOCOL)
        self.posizione.occupa_posizione(corridoio, scaffale, piano)

    def preleva_bottiglia(self, lista_bottiglie_salvate, nome_prodotto):
        for bottiglia in lista_bottiglie_salvate:
            if bottiglia.nome == nome_prodotto:
                if bottiglia.disponibilita > 0:
                    bottiglia.disponibilita -= 1
