from Magazzino.Prodotto import Prodotto
class Bottiglia(Prodotto):
    def __init__(self):
        super().__init__()
        self.disponibilita = ""
        self.posizione = Posizione



    def is_disponible(self):
        if (disponibilita > 0) return true
        else return false

    def get_posizione(self):