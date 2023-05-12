import Prenotazione from Attività

class GestorePrenotazioni(self)



# Funzione per creare una prenotazione, CONTROLLA SE USARE QUESTA O QUELLA IN PRENOTAZIONE
def inserisci_prenotazione(self, nome, cognome, data_di_nascita, codice_fiscale, servizio):
    if servizio in self.servizi:  # servizi è contenuto dentro Evento
        self.servizi[servizio].prenota()  # prenota aumenta le prenotazioni di un certo servizio dentro un evento
        prenotazione = Prenotazione(nome, cognome, data_di_nascita, codice_fiscale, self.servizi[servizio])
        self.prenotazioni.append(prenotazione)

