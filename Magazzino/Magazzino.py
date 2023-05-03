
class Magazzino():
    def __init__(self):
        super(Magazzino, self).__init__()
        self.magazzino = []
        self.bottiglie = []
        self.cocktail = []


    def get_lista_bottiglie(self):
        return self.bottiglie
    def get_lista_cocktail(self):
        return self.cocktail
    def get_lista_magazzino(self):
        self.magazzino = self.bottiglie + self.cocktail
        return self.magazzino
    