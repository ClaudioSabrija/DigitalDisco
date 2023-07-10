from Magazzino.Magazzino import Magazzino
import pickle
import os

class GestoreMagazzino:
    def __init__(self):
        self.magazzino = Magazzino()

    def posizione_occupata(self, corridoio, scaffale, piano):
        for bottiglia in self.magazzino.bottiglie:
            if bottiglia.corridoio == corridoio and bottiglia.scaffale == scaffale and bottiglia.piano == piano:
                return True
        return False

    def rimuovi_bottiglia(self, bottiglie):
        for bottiglia in self.magazzino.bottiglie:
            if bottiglia.nome == bottiglie.nome:
                self.magazzino.bottiglie.remove(bottiglia)
                with open('Dati/lista_bottiglie_salvate.pickle', 'wb') as f:
                    pickle.dump(self.magazzino.bottiglie, f, pickle.HIGHEST_PROTOCOL)
                return

    def rimuovi_cocktail(self, cocktail):
        for this_cocktail in self.magazzino.cocktail:
            if this_cocktail.nome == cocktail.nome:
                self.magazzino.cocktail.remove(this_cocktail)
                with open('Dati/lista_cocktail_salvati.pickle', 'wb') as f:
                    pickle.dump(self.magazzino.cocktail, f, pickle.HIGHEST_PROTOCOL)
                return

    def aggiorna_bottiglie(self, bottiglia, bottiglia_modificata):
        for i in range(len(self.magazzino.bottiglie)):
            if self.magazzino.bottiglie[i].nome == bottiglia.nome:
                self.magazzino.bottiglie[i] = bottiglia_modificata
                with open('Dati/lista_bottiglie_salvate.pickle', 'wb') as f:
                    pickle.dump(self.magazzino.bottiglie, f, pickle.HIGHEST_PROTOCOL)

    def aggiorna_cocktail(self, cocktail, cocktail_modificato):
        for i in range(len(self.magazzino.cocktail)):
            if self.magazzino.cocktail[i].nome == cocktail.nome:
                self.magazzino.cocktail[i] = cocktail_modificato
                with open('Dati/lista_cocktail_salvati.pickle', 'wb') as f:
                    pickle.dump(self.magazzino.cocktail, f, pickle.HIGHEST_PROTOCOL)

    # Funzione che salva i file con i dati aggiornati.
    def save_data(self):
        with open('Dati/lista_bottiglie_salvate.pickle', 'wb') as handle:
            pickle.dump(self.magazzino.bottiglie, handle, pickle.HIGHEST_PROTOCOL)

        with open('Dati/lista_cocktail_salvati.pickle', 'wb') as handle:
            pickle.dump(self.magazzino.cocktail, handle, pickle.HIGHEST_PROTOCOL)

    @staticmethod
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