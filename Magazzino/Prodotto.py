import pickle
import os


class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

    def unione_lista_prodotti(self):

        with open('lista_bottiglie_salvate.pickle', 'rb') as f1, open('lista_cocktail_salvati.pickle', 'rb') as f2:
            data1 = pickle.load(f1)
            data2 = pickle.load(f2)

        merged_data = [data1, data2]

        with open('lista_prodotti_salvati.pickle', 'wb') as f:
            pickle.dump(merged_data, f)

    def get_nome(self):
        return self.nome

    def get_prezzo(self):
        return self.prezzo

    #ricordare:aggiungere return VistaProdotto(con le informazioni del prodotto)
    def ricerca_prodotto_per_nome(self, nome):
        if os.path.isfile('Dati/lista_prodotti_salvati.pickle'):
            with open('Dati/lista_prodotti_salvati', 'rb') as f:
                prodotti = dict(pickle.load(f))
                for prodotti in prodotti.values():  # tutti i valori nel dict
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


