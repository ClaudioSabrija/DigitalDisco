from Magazzino.Prodotto import Prodotto
class Bottiglia(Prodotto):
    def __init__(self):
        super().__init__(nome, prezzo)
        self.disponibilita = ""
        self.posizione = ""
