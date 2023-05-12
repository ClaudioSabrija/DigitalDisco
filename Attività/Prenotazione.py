from Servizio import Servizio
from Evento import Evento

class Prenotazione():
    def __init__(self, nome, cognome, data_di_nascita, codice_fiscale, servizio):
        self.nome = nome
        self.cognome = cognome
        self.data_di_nascita = data_di_nascita
        self.codice_fiscale = codice_fiscale
        self.servizio = servizio



    # Funzione per creare una prenotazione, CONTROLLA SE USARE QUESTA O QUELLA IN GESTIONE PRENOTAZIONI
    def inserisci_prenotazione(self nome, cognome, data_di_nascita, codice_fiscale, servizio):

        prenotazione = Prenotazione(nome, cognome, data_di_nascita, codice_fiscale, servizio)
        if servizio in self.servizi:
            self.servizi[servizio].prenota()
            prenotazione = Prenotazione(nome, cognome, self.servizi[servizio])
            self.prenotazioni.append(prenotazione)



#QUESTA FORSE DEVE ESSERE SPOSTATA NELLA PARTE DELLE VISTE O GESTIONE PRENOTAZIONI, RICONTROLLA SE VA BENE
    def ricerca_prenotazione(self, nome, cognome)
        trovato = False
        for prenotazione in prenotazioni:
            if prenotazione.nome == nome and prenotazione.cognome == cognome:
                trovato = True
                print(f"{nome} {cognome} ha prenotato il servizio {prenotazione.servizio}")
                break
        if not trovato:
        print(f"{nome} {cognome} non ha prenotazioni")


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