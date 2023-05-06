import pickle
import os

from Magazzino.Prodotto import Prodotto


class Bottiglia(Prodotto):

    def __init__(self):
        super().__init__()
        self.disponibilita = ""
        self.posizione = " "

    def aggiungi_bottiglia(self, nome, prezzo, posizione):
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

    def rimuovi_bottiglia(self):
        if os.path.isfile('Dati/lista_bottiglie_salvate.pickle'):
            with open('Dati/lista_bottiglie_salvate.pickle', 'wb+') as f:
                bottiglie = pickle.load(f)
                del bottiglie[self.nome]
                pickle.dump(bottiglie, f, pickle.HIGHEST_PROTOCOL)

        # Rimette i valori di Default
        self.rimuovi_prodotto()
        self.disponibilita = ""
        self.posizione = ""
        del self


