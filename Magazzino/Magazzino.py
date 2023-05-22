import os
import pickle
import json

from Magazzino.Bottiglia import Bottiglia
from Magazzino.Cocktail import Cocktail


class Magazzino:
    def __init__(self):
        super(Magazzino, self).__init__()
        self.magazzino = []
        self.bottiglie = []
        self.cocktail = []

        if os.path.isfile('Dati/lista_bottiglie_salvate.pickle'):
            with open('Dati/lista_bottiglie_salvate.pickle', 'rb') as f:
                self.bottiglie = pickle.load(f)
        else:
            with open('Dati/lista_bottiglie.json') as f:
                bottiglie_iniziali = json.load(f)
            for bottiglie in bottiglie_iniziali:
                self.aggiungi_bottiglia(Bottiglia(bottiglie["nome"], bottiglie["prezzo"], bottiglie["posizione"]))

        if os.path.isfile('Dati/lista_cocktail_salvati.pickle'):
            with open('Dati/lista_cocktail_salvati.pickle', 'rb') as f:
                self.cocktail = pickle.load(f)
        else:
            with open('Dati/lista_cocktail.json') as f:
                cocktail_iniziali = json.load(f)
            for cocktail in cocktail_iniziali:
                self.aggiungi_cocktail(Cocktail(cocktail["nome"], cocktail["prezzo"]))

        #self.magazzino = self.bottiglie + self.cocktail

    # Funzione che restituisce la lista delle bottiglie
    def get_lista_bottiglie(self):
        return self.bottiglie

    # Funzione che restituisce la lista dei cocktail
    def get_lista_cocktail(self):
        return self.cocktail

    # Funzione che restituisce il magazzino
    def get_lista_magazzino(self):
        return self.magazzino

    def aggiungi_bottiglia(self, bottiglia):
        return self.bottiglie.append(bottiglia)

    def aggiungi_cocktail(self, cocktail):
        return self.bottiglie.append(cocktail)

    def get_presidio_by_index(self, index):
        return self.bottiglie[index]

    # Funzione che salva i file con i dati aggiornati.
    def save_data(self):
        with open('Dati/lista_bottiglie_salvate.pickle', 'wb') as handle:
            pickle.dump(self.bottiglie, handle, pickle.HIGHEST_PROTOCOL)

        with open('Dati/lista_cocktail_salvati.pickle', 'wb') as handle:
            pickle.dump(self.cocktail, handle, pickle.HIGHEST_PROTOCOL)



