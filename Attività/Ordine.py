import os
import pickle


class Ordine():
    def __init__(self):
        super(Ordine, self).__init__()
        self.prodotti = []
        self.bottiglie = []
        self.cocktail = []

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



    # Modificare perchè bisogna aggiungere il prodotto alla lista dell'ordine non alla lista dei prodotti
    def aggiungi_prodotto_ordine(self, prodotto):
        self.prodotti.append(prodotto)

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