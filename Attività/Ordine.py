import os
import pickle

from Magazzino.Prodotto import Prodotto


class Ordine():
    def __init__(self):
        self.lista_ordini = dict()

    def nuovo_ordine(self, prodotti, bottiglie, cocktail):
        self.prodotti = prodotti
        self.bottiglie = bottiglie
        self.cocktail = cocktail

        ordini = {}
        if os.path.isfile('Dati/lista_ordini.pickle'):
            with open('Dati/lista_ordini.pickle', 'rb') as f:
                ordini = pickle.load(f)
        ordini[prodotti, bottiglie, cocktail] = self
        with open('Dati/lista_ordini.pickle', 'wb') as f:
            pickle.dump(ordini, f, pickle.HIGHEST_PROTOCOL)


    def aggiungi_prodotto_ordine(self, prodotto):
        if(isinstance(prodotto, Prodotto)):
            self.lista_ordini[prodotto.nome] = prodotto
        else:
            raise Exception("Not ProdottoOrdine")

    def aggiungi_bottiglia_ordine(self, bottiglia):
        self.bottiglie.append(bottiglia)

    def aggiungi_cocktail_ordine(self, cocktail):
        self.cocktail.append(cocktail)

    def rimuovi_prodotto_ordine(self, prodotto):
        self.prodotti.remove(prodotto)

    def rimuovi_bottiglia_ordine(self, bottiglia):
        self.bottiglie.remove(bottiglia)

    def rimuovi_cocktail_ordine(self, cocktail):
        self.cocktail.remove(cocktail)