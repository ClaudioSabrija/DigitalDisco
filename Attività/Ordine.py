import string
import pickle
import random

class Ordine:
    def __init__(self):
        self.codice = ""
        self.prodotti = []
        self.prezzo_totale = 0
        self.lista_ordini = []

    def get_codice(self):
        return self.codice

    def get_prodotti(self):
        return self.prodotti

    def get_prezzo_totale(self):
        return self.prezzo_totale

    def inserisci_ordine(self, evento_selezionato):
        # Crea il codice ordine alfanumerico univoco
        codice_ord = self.genera_codice()
        self.prezzo_totale = sum(prezzo for _, _, prezzo in self.prodotti)

        self.codice = codice_ord

        # Salva l'ordine nel file pickle dell'evento selezionato
        with open(f'Dati/Ordini/ordini_{evento_selezionato}.pickle', 'ab') as file:
            pickle.dump(self, file)

    def get_lista_ordini(self):
        return self.lista_ordini

    def genera_codice(self):
        length = 8  # Lunghezza del codice
        characters = string.ascii_letters + string.digits  # Caratteri ammissibili (lettere maiuscole/minuscole e numeri)
        codice = ''.join(random.choice(characters) for _ in range(length))
        return codice
