from Servizio import Servizio


class Prenotazione():
    def __init__(self, nome, cognome, data_di_nascita, codice_fiscale, servizio):
        self.nome = nome
        self.cognome = cognome
        self.data_di_nascita = data_di_nascita
        self.codice_fiscale = codice_fiscale
        self.servizio = servizio


    # Funzione per selezionare il servizio corrispondente
    def seleziona_servizio(self, servizio):
        if isinstance(servizio, Servizio):
                return servizio
        else raise ValueError("Tipo di servizio non disponibile.")



    # Funzione per creare una prenotazione
    def inserisci_prenotazione(self nome, cognome, data_di_nascita, codice_fiscale,servizio):
        servizio = seleziona_servizio(tipo_servizio)
        prenotazione = Prenotazione(nome, cognome, servizio, prezzo)
        return prenotazione

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def get_data_di_nascita(self):
        return self.data_di_nascita

    def get_codice_fiscale(self):
        return self.codice_fiscale

    def get_servizio(self):
        return self.servizio



def save_data(self):
    with open('calendariovaccini/data/elenco_appuntamenti_fissati.pickle', 'wb') as handle:
        pickle.dump(self.elenco_appuntamenti, handle, pickle.HIGHEST_PROTOCOL)