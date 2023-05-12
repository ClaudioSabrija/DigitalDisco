import Prenotazione from Attività

class GestorePrenotazioni(self)



# Funzione per creare una prenotazione, CONTROLLA SE USARE QUESTA O QUELLA IN PRENOTAZIONE
def inserisci_prenotazione(self, nome, cognome, data_di_nascita, codice_fiscale, servizio):
    if servizio in self.servizi:  # servizi è contenuto dentro Evento
        self.servizi[servizio].prenota()  # prenota aumenta le prenotazioni di un certo servizio dentro un evento
        prenotazione = Prenotazione(nome, cognome, data_di_nascita, codice_fiscale, self.servizi[servizio])
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
