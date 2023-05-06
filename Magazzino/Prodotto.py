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
                prodotti = dict(pickle.load(f))
                for prodotti in prodotti.values(): # tutti i valori nel dict
                    if prodotti.nome == nome:
                        return prodotti
                return None
        else:
            return None

    def rimuovi_prodotto(self):
        if os.path.isfile('Dati/lista_prodotti_salvati.pickle'):
            with open('Dati/lista_prodotti_salvati.pickle', 'wb+') as f:
                prodotti = pickle.load(f)
                del prodotti[self.nome]
                pickle.dump(prodotti, f, pickle.HIGHEST_PROTOCOL)

        # Rimette i valori di Default
        self.nome = ""
        self.prezzo = ""
        del self

