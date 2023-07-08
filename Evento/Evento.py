from Servizio.Servizio import Servizio


class Evento:

    def __init__(self, nome, data, tipo, prezzo_ingresso, prezzo_tavolo, prezzo_prive):
        self.nome = nome
        self.data = data
        self.tipo = tipo
        self.prezzo_ingresso = prezzo_ingresso
        self.prezzo_tavolo = prezzo_tavolo
        self.prezzo_prive = prezzo_prive
        self.disponibilita_ingressi = 200
        self.disponibilita_tavoli = 20
        self.disponibilita_prive = 10
        self.servizi = {
        "Ingresso": Servizio("Ingresso", self.prezzo_ingresso, self.disponibilita_ingressi),
        "Tavolo": Servizio("Tavolo", self.prezzo_tavolo, self.disponibilita_tavoli),
        "Prive": Servizio("Prive", self.prezzo_prive, self.disponibilita_prive)
        }
        self.prenotazioni = []

    def get_nome(self):
        return self.nome

    def get_data(self):
        return self.data

    def get_tipo(self):
        return self.tipo

    def get_prezzo_ingresso(self):
        return self.prezzo_ingresso

    def get_prezzo_tavolo(self):
        return self.prezzo_tavolo

    def get_prezzo_prive(self):
        return self.prezzo_prive

    def get_disponibilita_ingresso(self):
        return self.disponibilita_ingressi

    def get_disponibilita_tavolo(self):
        return self.disponibilita_tavoli

    def get_disponibilita_prive(self):
        return self.disponibilita_prive

    def __eq__(self, other): #Metodo che mi potrebbe servire quando vado a confrontare gli eventi in altre parti del programma
        if isinstance(other, Evento):
            return (
                    self.nome == other.nome and
                    self.data == other.data and
                    self.tipo == other.tipo  and
                    self.prezzo_ingresso == other.tipo.prezzo_ingresso and
                    self.prezzo_tavolo == other.prezzo_tavolo and
                    self.prezzo_prive == other.prezzo_prive and
                    self.disponibilita_ingressi == other.disponibilita_ingressi and
                    self.disponibilita_tavoli == other.disponibilita_tavoli and
                    self.disponibilita_prive == other.disponibilita_prive and
                    self.servizi == other.servizi
            )
        return False
