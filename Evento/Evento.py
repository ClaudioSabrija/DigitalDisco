import pickle
import os

from Servizio.Servizio import Servizio


class Evento:
    def __init__(self):
        self.nome = ''
        self.data = ''
        self.tipo = ''
        self.prezzo_ingresso = ''
        self.prezzo_tavolo = ''
        self.prezzo_prive = ''
        self.disponibilita_ingressi = 200
        self.disponibilita_tavoli = 20
        self.disponibilita_prive = 10
        self.servizi = {
        "Ingresso": Servizio("Ingresso", self.prezzo_ingresso, self.disponibilita_ingressi),
        "Tavolo": Servizio("Tavolo", self.prezzo_tavolo, self.disponibilita_tavoli),
        "Prive": Servizio("Prive", self.prezzo_prive, self.disponibilita_prive)
        }
        self.prenotazioni = []

    # Metodi get degli attributi
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

    def RicercaEventoPerNome(self, nome):
        if os.path.isfile('Dati/lista_eventi.pickle'):
            with open('Dati/lista_eventi.pickle', 'rb') as f:
                eventi = dict(pickle.load(f))
                for eventi in eventi.values():
                    if eventi.nome == nome:
                        return eventi
                return None
        else:
            return None
