import os
import pickle

from Servizio.Servizio import Servizio
from Evento.Evento import Evento

class GestoreEventi():
    def __init__(self):
        self.lista_eventi = []
        self.lettura_eventi()
        self.model = Evento

    def lettura_eventi(self):
        if os.path.isfile('Dati/lista_eventi.pickle'):
            with open('Dati/lista_eventi.pickle', 'rb') as file:
                self.lista_eventi = pickle.load(file)

    def get_lista_eventi(self):
        return self.lista_eventi

    def get_evento_by_index_(self, index):
        evento = self.lista_eventi[index]
        return Evento(evento.nome, evento.data, evento.tipo, evento.prezzo_ingresso, evento.prezzo_tavolo,
                      evento.prezzo_prive)

    def inserisci_evento(self, nome, data, tipo, prezzo_ingresso, prezzo_tavolo, prezzo_prive):
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
        self.lista_eventi.append(self)  # Aggiungi l'evento alla lista degli eventi

        with open('Dati/lista_eventi.pickle', 'wb') as f:
            pickle.dump(self.lista_eventi, f, pickle.HIGHEST_PROTOCOL)


    def rimuovi_evento(self, evento):
        for eventi in self.lista_eventi:
            if eventi.nome == evento.nome and eventi.data == evento.data:
                self.lista_eventi.remove(eventi)
                with open('Dati/lista_eventi.pickle', 'wb') as f:
                    pickle.dump(self.lista_eventi, f, pickle.HIGHEST_PROTOCOL)
                return

    def set_evento(self, evento):
        self.model = evento