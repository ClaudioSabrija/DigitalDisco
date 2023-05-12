import pickle
import os

from Servizio.Servizio import Servizio


class Evento:
    def __init__(self, nome, data, prezzo_ingresso, prezzo_tavolo, prezzo_prive, disponibilita_ingressi, disponibilita_tavoli, disponibilita_prive):
        self.nome = nome
        self.data = data
        self.prezzo_ingresso = prezzo_ingresso
        self.prezzo_tavolo = prezzo_tavolo
        self.prezzo_prive = prezzo_prive
        self.disponibilita_ingressi = disponibilita_ingressi
        self.disponibilita_tavoli = disponibilita_tavoli
        self.disponibilita_prive = disponibilita_prive
        self.servizi = {
        "Ingresso": Servizio("Ingresso", prezzo_ingresso, disponibilita_ingressi),
        "Tavolo": Servizio("Tavolo", prezzo_tavolo, disponibilita_tavoli),
        "Prive": Servizio("Prive", prezzo_prive, disponibilita_prive)
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
# Inserire qualcosa per le prenotazioni per inserirle e associarle all'evento, una lista oppure un file pickle

    def inserisci_evento(self, nome, data, prezzo_ingresso, prezzo_tavolo, prezzo_prive, disponibilita_ingresso, disponibilita_tavoli, disponibilita_prive):
        self.nome = nome
        self.data = data
        self.servizi = {
            "Ingresso": Servizio("Ingresso", prezzo_ingresso, disponibilita_ingresso),
            "Tavolo": Servizio("Tavolo", prezzo_tavolo, disponibilita_tavoli),
            "Prive": Servizio("Prive", prezzo_prive, disponibilita_prive)
        }
        eventi = {} #dizionario di eventi
        if os.path.isfile('Dati/lista_eventi.pickle'):
            with open('Dati/lista_eventi.pickle', 'rb') as f:
                eventi = pickle.load(f)
        eventi[nome] = self #carica l'evento con quel nome nel dizionario
        with open('Dati/lista_eventi.pickle', 'wb') as f:
            pickle.dump(eventi, f, pickle.HIGHEST_PROTOCOL)

    def rimuovi_evento(self):
        if os.path.isfile('Dati/lista_eventi.pickle'):
            with open('Dati/lista_eventi.pickle', 'wb+') as f:
                eventi = pickle.load(f)
                del eventi[self.nome]
                pickle.dump(eventi, f, pickle.HIGHEST_PROTOCOL)

        self.nome = ""
        self.data = ""
        self.prezzo_ingresso = ""
        self.prezzo_tavolo = ""
        self.prezzo_prive = ""
        self.disponibilita_ingressi = ""
        self.disponibilita_tavoli = ""
        self.disponibilita_prive = ""
        self.servizi = {}
        del self


