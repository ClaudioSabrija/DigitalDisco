from GestorePrenotazioni.Model.Servizio import Servizio


class Evento:

    def __init__(self, nome, data, tipo, prezzo_ingresso, prezzo_tavolo, prezzo_prive):
        self.nome = nome
        self.data = data
        self.tipo = tipo
        self.prezzo_ingresso = prezzo_ingresso
        self.prezzo_tavolo = prezzo_tavolo
        self.prezzo_prive = prezzo_prive
        self.disponibilita_ingressi = 220
        self.disponibilita_tavoli = 8
        self.disponibilita_prive = 4
        self.servizi = {
        "Ingresso": Servizio("Ingresso", self.prezzo_ingresso, self.disponibilita_ingressi),
        "Tavolo": Servizio("Tavolo", self.prezzo_tavolo, self.disponibilita_tavoli),
        "Prive": Servizio("Prive", self.prezzo_prive, self.disponibilita_prive)
        }
        self.lista_prenotazioni = []

    def set_evento(self, nuovo_evento):
        self.nome = nuovo_evento.nome
        self.data = nuovo_evento.data
        self.tipo = nuovo_evento.tipo
        self.prezzo_ingresso = nuovo_evento.prezzo_ingresso
        self.prezzo_tavolo = nuovo_evento.prezzo_tavolo
        self.prezzo_prive = nuovo_evento.prezzo_prive

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

    def get_disponibilita_ingressi(self):
        return self.disponibilita_ingressi

    def get_disponibilita_tavoli(self):
        return self.disponibilita_tavoli

    def get_disponibilita_prive(self):
        return self.disponibilita_prive

    def get_lista_prenotazioni(self):
        return self.lista_prenotazioni

