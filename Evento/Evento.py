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


