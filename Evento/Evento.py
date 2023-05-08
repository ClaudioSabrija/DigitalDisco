import pickle
import os

class Evento:

    def __init__(self, nome, tipo, data, prezzo_ingresso, prezzo_tavolo, prezzo_prive):
        super().__init__()
        self.nome = nome
        self.tipo = tipo
        self.data = data
        self.prezzo_ingresso = prezzo_ingresso
        self.prezzo_tavolo = prezzo_tavolo
        self.prezzo_prive = prezzo_prive

    def inserisci_evento(self, nome, tipo, data, prezzo_ingresso, prezzo_tavolo, prezzo_prive):
        self.nome = nome
        self.tipo = tipo
        self.data = data
        self.prezzo_ingresso = prezzo_ingresso
        self.prezzo_tavolo = prezzo_tavolo
        self.prezzo_prive = prezzo_prive

        eventi = {}
        if os.path.isfile('Dati/lista_eventi.pickle'):
            with open('Dati/lista_eventi.pickle', 'rb') as f:
                eventi = pickle.load(f)
            eventi[nome] = self
            with open('Dati/lista_eventi.pickle', 'wb') as f:
                pickle.dump(eventi, f, pickle.HIGHEST_PROTOCOL)

    def rimuovi_evento(self):
        if os.path.isfile('Dati/lista_eventi.pickle'):
            with open('Dati/lista_eventi.pickle', 'wb+') as f:
                eventi = pickle.load(f)
                del eventi[self.nome]
                pickle.dump(eventi, f, pickle.HIGHEST_PROTOCOL)

        self.nome = "" #Rimette i valori di Default
        self.tipo = ""
        self.data = ""
        self.prezzo_ingresso = ""
        self.prezzo_tavolo = ""
        self.prezzo_prive = ""
        del self


    # Metodi get degli attributi

    def get_nome(self):
        return self.nome

    def get_tipo(self):
        return self.tipo

    def get_data(self):
        return self.data

    def get_prezzo_ingresso(self):
        return self.prezzo_ingresso

    def get_prezzo_tavolo(self):
        return self.prezzo_tavolo

    def get_prezzo_prive(self):
        return self.prezzo_prive