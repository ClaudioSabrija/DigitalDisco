from GestoreMagazzino.Model.Prodotto import Prodotto


class Bottiglia(Prodotto):

    def __init__(self, nome, prezzo, disponibilita, corridoio, scaffale, piano):
        super(Bottiglia, self).__init__(nome, prezzo)
        self.disponibilita = disponibilita
        self.corridoio = corridoio
        self.scaffale = scaffale
        self.piano = piano

    def get_bottiglia(self):
        return Bottiglia(self.nome, self.prezzo, self.disponibilita, self.corridoio, self.scaffale, self.piano)

    def set_bottiglia(self, bottiglia):
        if isinstance(bottiglia, Bottiglia):
            self.nome = bottiglia.nome
            self.prezzo = bottiglia.prezzo
            self.disponibilita = bottiglia.disponibilita
            self.corridoio = bottiglia.corridoio
            self.scaffale = bottiglia.scaffale
            self.piano = bottiglia.piano

    def get_nome_bottiglia(self):
        return self.nome

    def get_prezzo_bottiglia(self):
        return self.prezzo

    def get_corridoio_bottiglia(self):
        return self.corridoio

    def get_scaffale_bottiglia(self):
        return self.scaffale

    def get_piano_bottiglia(self):
        return self.piano

    # Metodi che servono per il prelievo delle bottiglie
    def get_disponibilta_bottiglia(self):
        return self.disponibilita

    def set_disponibilita_bottiglia(self, nuova_disponibilita):
        self.disponibilita = nuova_disponibilita