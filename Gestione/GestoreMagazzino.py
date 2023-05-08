
from Magazzino import Bottiglia

# Funzione che aggiunge alla lista delle bottiglie una bottiglia passata come parametro.
    def aggiungi_bottiglia(self, bottiglia):
        self.bottiglie.append(bottiglia)

    # Funzione che aggiunge alla lista dei cocktail un cocktail passato come parametro.
    def aggiungi_cocktail(self, cocktail):
        self.cocktail.append(cocktail)

    def rimuovi_bottiglia(self, bottiglie):
        self.bottiglie.remove(bottiglie)

    def rimuovi_cocktail(self, cocktail):
        self.cocktail.remove(cocktail)