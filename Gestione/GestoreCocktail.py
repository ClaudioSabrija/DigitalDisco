class GestoreCocktail():

    def __init__(self, cocktail):
        self.model = cocktail

    def get_cocktail(self):
        return self.model

    def set_cocktail(self, cocktail):
        self.model = cocktail

    def get_nome_cocktail(self):
        return self.model.nome

    def get_prezzo_cocktail(self):
        return self.model.prezzo