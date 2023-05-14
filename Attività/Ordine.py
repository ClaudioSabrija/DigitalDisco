import os
import pickle

from Magazzino.Prodotto import Prodotto


class Ordine():
    def __init__(self):
        self.lista_prodotti = dict()

    def aggiungi_prodotto_ordine(self, prodotto):
        if(isinstance(prodotto, Prodotto)):
            self.lista_prodotti[prodotto.nome] = prodotto
        else:
            raise Exception("Not ProdottoOrdine")

    def rimuovi_prodotto_ordine(self, nome):
        del(self.lista_prodotti[nome])

