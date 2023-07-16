import pickle
import random
import string


class GestoreOrdini():
    def __init__(self):
        self.ordini = []

    def inserisci_ordine(self, ordine, evento_selezionato):
        self.ordine = ordine
        # Crea il codice ordine alfanumerico univoco
        codice_ord = self.genera_codice()
        self.ordine.prezzo_totale = sum(prezzo for _, _, prezzo in self.ordine.prodotti)

        self.ordine.codice = codice_ord

        # Salva l'ordine nel file pickle dell'evento selezionato
        with open(f'Dati/Ordini/ordini_{evento_selezionato}.pickle', 'ab') as file:
            pickle.dump(self, file)

    def elimina_ordine(self, index, evento_selezionato):
        if index < len(self.ordini):
            ordine_selezionato = self.ordini[index]
            self.ordini.pop(index)

            # Rimuovi l'ordine dal file pickle corrispondente all'evento selezionato
            file_pickle = f'Dati/Ordini/ordini_{evento_selezionato}.pickle'

            with open(file_pickle, 'wb') as file:
                # Scrivi nuovamente gli ordini rimanenti nel file pickle
                for ordine_in_lista in self.ordini:
                    pickle.dump(ordine_in_lista, file)
        return ordine_selezionato

    def genera_codice(self):
        length = 8  # Lunghezza del codice
        characters = string.ascii_letters + string.digits  # Caratteri ammissibili (lettere maiuscole/minuscole e numeri)
        codice = ''.join(random.choice(characters) for _ in range(length))
        return codice

    def get_lista_ordini(self):
        return self.ordini
