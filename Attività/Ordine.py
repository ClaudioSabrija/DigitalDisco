
class Ordine:
    def __init__(self):
        self.codice = ""
        self.prodotti = []
        self.prezzo_totale = 0

    def get_codice(self):
        return self.codice

    def get_prodotti(self):
        return self.prodotti

    def get_prezzo_totale(self):
        return self.prezzo_totale


