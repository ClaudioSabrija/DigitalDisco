import pickle
import os


class Prodotto:
    def __init__(self):
        super(self, Prodotto).__init__()
        self.nome = ""
        self.prezzo = ""


    def get_nome(self):
        return self.nome

    def get_prezzo(self):
        return self.prezzo

    #ricordare:aggiungere return VistaProdotto(con le informazioni del prodotto)
    def ricerca_prodotto_per_nome(self, nome):
        if os.path.isfile('Dati/lista_prodotti_salvati.pickle'):
            with open('Dati/lista_prodotti_salvati', 'rb') as f:
                bottiglie = dict(pickle.load(f))
                for bottiglie in bottiglie.values(): # tutti i valori nel dict
                    if bottiglie.nome == nome:
                        return bottiglie
                return None
        else:
            return None