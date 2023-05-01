


class Ordine():
    def __init__(self):
        super(Ordine, self).__init__()
        self.prodotti = []
        self.bottiglie = []
        self.cocktail = []

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