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
            self.aggiungi_bottiglia(Bottiglia(bottiglie["nome"], bottiglie["prezzo"], bottiglie["disponibilita"], bottiglie["posizione"]))

        if os.path.isfile('Dati/lista_cocktail_salvati.pickle'):
            with open('Dati/lista_cocktail_salvati.pickle', 'rb') as f:
                self.cocktail = pickle.load(f)
        else:
            with open('Dati/lista_cocktail.json') as f:
                cocktail_iniziali = json.load(f)
        for cocktail in cocktail_iniziali:
            self.aggiungi_cocktail(Cocktail(cocktail["nome"], cocktail["prezzo"]))

    def get_lista_bottiglie(self):
        return self.bottiglie

    def get_lista_cocktail(self):
        return self.cocktail

    def get_lista_magazzino(self):
        self.magazzino = self.bottiglie + self.cocktail
        return self.magazzino

    # Funzione che aggiunge alla lista delle bottiglie una bottiglia passata come parametro.
    def aggiungi_bottiglia(self, bottiglie):
        self.bottiglie.append(bottiglie)

    # Funzione che aggiunge alla lista dei cocktail un cocktail passato come parametro.
    def aggiungi_cocktail(self, cocktail):
        self.cocktail.append(cocktail)

    def rimuovi_bottiglia(self, bottiglie):
        self.bottiglie.remove(bottiglie)

    def rimuovi_cocktail(self, cocktail):
        self.cocktail.remove(cocktail)
