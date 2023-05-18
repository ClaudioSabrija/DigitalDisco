import pickle
import os

from Servizio.Servizio import Servizio


class Evento:
    def __init__(self, nome, tipo, data, prezzo_ingresso, prezzo_tavolo, prezzo_prive):
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
        "Ingresso": Servizio("Ingresso", prezzo_ingresso, self.disponibilita_ingressi),
        "Tavolo": Servizio("Tavolo", prezzo_tavolo, self.disponibilita_tavoli),
        "Prive": Servizio("Prive", prezzo_prive, self.disponibilita_prive)
        }
        self.prenotazioni = []

    # Metodi get degli attributi
    def get_nome(self):
        return self.nome

    def get_data(self):
        return self.data

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

