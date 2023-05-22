import pickle
import os

from Magazzino.Prodotto import Prodotto


class Cocktail(Prodotto):
    def __init__(self, nome, prezzo):
        super(Cocktail, self).__init__(nome, prezzo)

    def inserisci_cocktail(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
        new_cocktail = dict()
        if os.path.isfile('Dati/lista_cocktail_salvati.pickle'):
            with open('Dati/lista_cocktail_salvati.pickle', 'rb') as f:
                cocktail = pickle.load(f)
        new_cocktail[nome] = self  # ho fatto una lista [] perché mi dava l'errore must be integer e allora ho messo append
        with open('Dati/lista_cocktail_salvati.pickle', 'wb') as f:
            pickle.dump(cocktail, f, pickle.HIGHEST_PROTOCOL)

    def rimuovi_cocktail(self):
        if os.path.isfile('Dati/lista_cocktail_salvati.pickle'):
            with open('Dati/lista_cocktail_salvati.pickle', 'wb+') as f:
                cocktail = pickle.load(f)
                del cocktail[self.nome]
                pickle.dump(cocktail, f, pickle.HIGHEST_PROTOCOL)

        # Rimette i valori di Default
        self.rimuovi_prodotto()
        del self
