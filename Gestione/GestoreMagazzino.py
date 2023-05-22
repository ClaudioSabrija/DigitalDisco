from Magazzino.Magazzino import Magazzino


class GestoreMagazzino:
    def __init__(self):
        self.Magazzino = Magazzino()

    # Funzione che aggiunge alla lista delle bottiglie una bottiglia passata come parametro.
    def aggiungi_bottiglia_lista(self, bottiglia):
        self.Magazzino.bottiglie.append(bottiglia)

    # Funzione che aggiunge alla lista dei cocktail un cocktail passato come parametro.
    def aggiungi_cocktail_lista(self, cocktail):
        self.Magazzino.cocktail.append(cocktail)

    def rimuovi_bottiglia_lista(self, bottiglie):
        self.Magazzino.bottiglie.remove(bottiglie)

    def rimuovi_cocktail_lista(self, cocktail):
        self.Magazzino.cocktail.remove(cocktail)
