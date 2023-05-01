from Magazzino.Prodotto import Prodotto


class Cocktail(Prodotto):
    def __init__(self, nome, prezzo, disponibilita, posizione):
        super().__init__(nome, prezzo)