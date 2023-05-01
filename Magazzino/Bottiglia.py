from Magazzino.Prodotto import Prodotto
class Bottiglia(Prodotto):
    def __init__(self, nome, prezzo, disponibilita, posizione):
        super().__init__(nome, prezzo)
        self.disponibilita = disponibilita
        self.posizione = posizione