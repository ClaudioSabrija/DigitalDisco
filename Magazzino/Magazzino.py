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
            for bottiglia in bottiglie_iniziali:
                self.aggiungi_bottiglia(Bottiglia(bottiglia["nome"], bottiglia["prezzo"], bottiglia["disponibilita"], bottiglia["corridoio"], bottiglia["scaffale"], bottiglia["piano"]))

        if os.path.isfile('Dati/lista_cocktail_salvati.pickle'):
            with open('Dati/lista_cocktail_salvati.pickle', 'rb') as f:
                self.cocktail = pickle.load(f)
        else:
            with open('Dati/lista_cocktail.json') as f:
                cocktail_iniziali = json.load(f)
            for cocktail in cocktail_iniziali:
                self.aggiungi_cocktail(Cocktail(cocktail["nome"], cocktail["prezzo"]))

        self.magazzino = self.bottiglie + self.cocktail

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
        self.bottiglie.append(bottiglia)

    def aggiungi_cocktail(self, cocktail):
        return self.cocktail.append(cocktail)

    def get_bottiglia_by_index_(self, index):
        return self.bottiglie[index]

    def get_cocktail_by_index(self, index):
        return self.cocktail[index]

    def posizione_occupata(self, corridoio, scaffale, piano):
        for bottiglia in self.bottiglie:
            if bottiglia.corridoio == corridoio and bottiglia.scaffale == scaffale and bottiglia.piano == piano:
                return True
        return False

    def rimuovi_bottiglia(self, bottiglie):
        for bottiglia in self.bottiglie:
            if bottiglia.nome == bottiglie.nome:
                self.bottiglie.remove(bottiglia)
                with open('Dati/lista_bottiglie_salvate.pickle', 'wb') as f:
                    pickle.dump(self.bottiglie, f, pickle.HIGHEST_PROTOCOL)
                return

    def rimuovi_cocktail(self, cocktail):
        for this_cocktail in self.cocktail:
            if this_cocktail.nome == cocktail.nome:
                self.cocktail.remove(this_cocktail)
                with open('Dati/lista_cocktail_salvati.pickle', 'wb') as f:
                    pickle.dump(self.cocktail, f, pickle.HIGHEST_PROTOCOL)
                return

    def aggiorna_bottiglie(self, bottiglia, bottiglia_modificata):
        for i in range(len(self.bottiglie)):
            if self.bottiglie[i].nome == bottiglia.nome:
                self.bottiglie[i] = bottiglia_modificata
                with open('Dati/lista_bottiglie_salvate.pickle', 'wb') as f:
                    pickle.dump(self.bottiglie, f, pickle.HIGHEST_PROTOCOL)

    def aggiorna_cocktail(self, cocktail, cocktail_modificato):
        for i in range(len(self.cocktail)):
            if self.cocktail[i].nome == cocktail.nome:
                self.cocktail[i] = cocktail_modificato
                with open('Dati/lista_cocktail_salvati.pickle', 'wb') as f:
                    pickle.dump(self.cocktail, f, pickle.HIGHEST_PROTOCOL)

    # Funzione che salva i file con i dati aggiornati.
    def save_data(self):
        with open('Dati/lista_bottiglie_salvate.pickle', 'wb') as handle:
            pickle.dump(self.bottiglie, handle, pickle.HIGHEST_PROTOCOL)

        with open('Dati/lista_cocktail_salvati.pickle', 'wb') as handle:
            pickle.dump(self.cocktail, handle, pickle.HIGHEST_PROTOCOL)



