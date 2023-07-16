
from GestoreMagazzino.Model.Prodotto import Prodotto


class Cocktail(Prodotto):
    def __init__(self, nome, prezzo):
        super(Cocktail, self).__init__(nome, prezzo)

    def get_cocktail(self):
        return Cocktail(self.nome, self.prezzo)

    def set_cocktail(self, cocktail):
        if isinstance(cocktail, Cocktail):
            self.nome = cocktail.nome
            self.prezzo = cocktail.prezzo

    def get_nome_cocktail(self):
        return self.nome

    def get_prezzo_cocktail(self):
        return self.prezzo
