import os
import pickle

from Magazzino.Prodotto import Prodotto


class Ordine():
    def __init__(self):
        self.lista_prodotti = {}
        self.quantita_prodotto = ''
        self.importo_totale = ''

    def aggiungi_prodotto_ordine(self, nome_prodotto):
        with open('Dati/lista_ prodotti_salvati.pickle', 'rb') as f:
            prodotti = pickle.load(f)
        # Controlla se l'oggetto desiderato è presente
            for prodotto in prodotti:
                if prodotto.nome == nome_prodotto:
                    self.lista_prodotti[prodotto.nome] = prodotto
                else:
                    print('L\'oggetto con il nome "prodotto.nome" non è presente nel file pickle.')

    def rimuovi_prodotto_ordine(self, nome_prodotto):
        if nome_prodotto in self.lista_prodotti:
            del self.lista_prodotti[nome_prodotto]

