import pickle
import os

from Magazzino.Prodotto import Prodotto


class Cocktail(Prodotto):
    def __init__(self, nome, prezzo):
        super().__init__(nome, prezzo)

    def aggiungi_cocktail(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
        cocktail = {}
        if os.path.isfile('Dati/lista_cocktail_salvati.pickle'):
            with open('Dati/lista_cocktail_salvati.pickle', 'rb') as f:
                cocktail = pickle.load(f)
            cocktail[nome] = self
            with open('Dati/lista_cocktail_salvati.pickle', 'wb') as f:
                pickle.dump(cocktail, f, pickle.HIGHEST_PROTOCOL)
