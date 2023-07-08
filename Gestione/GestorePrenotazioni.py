import pickle
from Attività.Prenotazione import Prenotazione
from Servizio.Servizio import Servizio
from Evento.Evento import Evento

class GestorePrenotazioni():

    def get_prenotazione_by_index(self, evento, index):
        lista_prenotazioni = evento.get_lista_prenotazioni()
        prenotazione = lista_prenotazioni[index]
        return prenotazione

    def inserisci_prenotazione(self, evento, prenotazione):
        evento.lista_prenotazioni.append(prenotazione)  # Aggiunge l'evento alla lista degli eventi
        with open(f'Dati/Prenotazioni/prenotazioni_{evento.nome}.pickle', 'wb') as f:
            pickle.dump(evento.lista_prenotazioni, f, pickle.HIGHEST_PROTOCOL)

    def rimuovi_prenotazione(self, evento ,prenotazione):
        for prenotazioni in evento.lista_prenotazioni:
            if prenotazioni.codice_fiscale == prenotazione.codice_fiscale:
                evento.lista_prenotazioni.remove(prenotazione)
                with open(f'Dati/Prenotazioni/prenotazioni_{evento.nome}.pickle', 'wb') as f:
                    pickle.dump(evento.lista_prenotazioni, f, pickle.HIGHEST_PROTOCOL)
                return

    def aggiorna_prenotazione(self, evento, prenotazione, prenotazione_modificata):
        for i in range(len(evento.lista_prenotazioni)):
            if evento.lista_prenotazioni[i].codice_fiscale == prenotazione.codice_fiscale:
                evento.lista_prenotazioni[i] = prenotazione_modificata
                with open(f'Dati/Prenotazioni/prenotazioni_{evento.nome}.pickle', 'wb') as f:
                    pickle.dump(evento.lista_prenotazioni, f, pickle.HIGHEST_PROTOCOL)
