

class Prenotazione():
    def __init__(self, nome, cognome, data_di_nascita, codice_fiscale, servizio):
        self.nome = nome
        self.cognome = cognome
        self.data_di_nascita = data_di_nascita
        self.codice_fiscale = codice_fiscale
        self.servizio = servizio
        self.note = []

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

    def get_note(self):
        return self.note