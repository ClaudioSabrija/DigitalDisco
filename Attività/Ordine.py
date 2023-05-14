import os
import pickle

from Magazzino.Prodotto import Prodotto


class Ordine():
    def __init__(self):





    def aggiungi_prodotto_ordine(self, prodotto):
        if(isinstance(prodotto, Prodotto)):
            self.lista_ordini[prodotto.nome] = prodotto
        else:
            raise Exception("Not ProdottoOrdine")

    def rimuovi_prodotto_ordine(self, nome):
        del(self.lista_ordini[nome])

