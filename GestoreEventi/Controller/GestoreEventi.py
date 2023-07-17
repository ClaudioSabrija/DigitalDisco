import os
import pickle

from GestoreEventi.Model.Evento import Evento

class GestoreEventi():
    def __init__(self):
        self.lista_eventi = []
        self.lettura_eventi()

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

    def RicercaEventoPerNome(self, nome):
        if os.path.isfile('Dati/lista_eventi.pickle'):
            with open('Dati/lista_eventi.pickle', 'rb') as f:
                eventi = pickle.load(f)
                for evento in eventi:
                    if evento.nome == nome:
                        return evento
        return None

    def inserisci_evento(self, evento):
        self.lista_eventi.append(evento)  # Aggiunge l'evento alla lista degli eventi
        with open('Dati/lista_eventi.pickle', 'wb') as f:
            pickle.dump(self.lista_eventi, f, pickle.HIGHEST_PROTOCOL)


    def rimuovi_evento(self, evento):
        for eventi in self.lista_eventi:
            if eventi.nome == evento.nome and eventi.data == evento.data:
                self.lista_eventi.remove(eventi)
                with open('Dati/lista_eventi.pickle', 'wb') as f:
                    pickle.dump(self.lista_eventi, f, pickle.HIGHEST_PROTOCOL)
                return

    def aggiorna_evento(self, evento, evento_modificato):
        for i in range(len(self.lista_eventi)):
            if self.lista_eventi[i].nome == evento.nome and self.lista_eventi[i].data == evento.data:
                self.lista_eventi[i] = evento_modificato
                with open('Dati/lista_eventi.pickle', 'wb') as f:
                    pickle.dump(self.lista_eventi, f, pickle.HIGHEST_PROTOCOL)

