import pickle
import os


class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo


    def unione_lista_prodotti():
        data1 = []
        data2 = []
        if os.path.isfile('Dati/lista_bottiglie_salvate.pickle'):
            with open('Dati/lista_bottiglie_salvate.pickle', 'rb') as f1:
                data1 = pickle.load(f1)

        if os.path.isfile('Dati/lista_cocktail_salvati.pickle'):
            with open('Dati/lista_cocktail_salvati.pickle', 'rb') as f2:
                data2 = pickle.load(f2)

        merged_data = data1 + data2

        with open('Dati/lista_prodotti_salvati.pickle', 'wb+') as f:
            pickle.dump(merged_data, f, pickle.HIGHEST_PROTOCOL)

    def get_nome(self):
        return self.nome

    def get_prezzo(self):
        return self.prezzo
