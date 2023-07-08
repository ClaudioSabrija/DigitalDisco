import pickle, string, random

from PyQt5.QtGui import QIcon, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListView, QPushButton, QLabel, QMessageBox

from Attività.Ordine import Ordine
from Magazzino.Bottiglia import Bottiglia
from Viste.VistaScegliProdotto import VistaScegliProdotto


class VistaNuovoOrdine(QWidget):
    def __init__(self, evento_selezionato, ordine, callback):
        super().__init__()

        self.evento_selezionato = evento_selezionato
        self.layout = QVBoxLayout()
        self.callback = callback
        self.ordine = ordine
        self.ordine.prezzo_totale = 0

        # ListView per i prodotti selezionati
        self.list_view = QListView()
        self.layout.addWidget(self.list_view)
        self.list_view_model = QStandardItemModel(self.list_view)

        # Label "Importo"
        self.label_importo = QLabel("Importo: 0\u20AC")
        self.layout.addWidget(self.label_importo)

        # Layout per i bottoni
        buttons_layout = QHBoxLayout()

        # Bottone "Inserisci Prodotto"
        self.btn_inserisci_prodotto = QPushButton("Inserisci Prodotto")
        buttons_layout.addWidget(self.btn_inserisci_prodotto)
        self.btn_inserisci_prodotto.clicked.connect(self.scegli_prodotto)

        # Bottone "Conferma"
        self.btn_conferma = QPushButton("Conferma")
        buttons_layout.addWidget(self.btn_conferma)
        self.btn_conferma.clicked.connect(self.conferma_ordine)

        self.layout.addLayout(buttons_layout)

        self.setLayout(self.layout)
        self.resize(400, 450)
        self.setWindowTitle("Nuovo Ordine")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

    def scegli_prodotto(self):
        self.vista_scegli_prodotto = VistaScegliProdotto(callback=self.add_prodotto)
        self.vista_scegli_prodotto.show()

    def add_prodotto(self):
        # Ottieni i prodotti selezionati dall'istanza di VistaScegliProdotto
        self.prodotti_selezionati = self.vista_scegli_prodotto.get_selected_products()

        if self.prodotti_selezionati:
            for prodotto, quantita, prezzo_totale  in self.prodotti_selezionati:
                # Aggiungi il prodotto al list_view_model
                item = QStandardItem()
                item.setText(f"{prodotto.get_nome()} - Prezzo Totale: {prezzo_totale}\u20AC")
                item.setEditable(False)
                font = item.font()
                font.setPointSize(13)
                item.setFont(font)
                self.list_view_model.appendRow(item)
                self.ordine.prodotti.append((prodotto, quantita, prezzo_totale))

                if isinstance(prodotto, Bottiglia):
                    disponibilita_bottiglia = prodotto.get_disponibilta_bottiglia()
                    if disponibilita_bottiglia <= 1:
                        QMessageBox.critical(self, "Errore", "Aggiungi scorte in magazzino, prodotto indisponibile")
                        self.list_view_model.removeRow(self.list_view_model.rowCount() - 1) # Rimuovi l'elemento aggiunto
                        self.ordine.prodotti.pop()  # Rimuovi il prodotto dall'ordine
                        self.close()

            # Imposta il list_view_model sulla list_view
            self.list_view.setModel(self.list_view_model)
            # Calcola l'importo totale dei prodotti
            self.ordine.prezzo_totale += sum(prezzo for _, _, prezzo in self.prodotti_selezionati)
            # Aggiorna il testo della label dell'importo
            self.label_importo.setText(f"Importo: {self.ordine.prezzo_totale}\u20AC")

    def conferma_ordine(self):
        # Crea il codice ordine alfanumerico univoco
        codice_ord = self.genera_codice()
        self.ordine.prezzo_totale = sum(prezzo for _, _, prezzo in self.ordine.prodotti)

        ordine = Ordine()
        ordine.codice = codice_ord
        ordine.prezzo_totale = self.ordine.prezzo_totale

        # Salva l'ordine nel file pickle dell'evento selezionato
        with open(f'Dati/Ordini/ordini_{self.evento_selezionato}.pickle', 'ab') as file:
            pickle.dump(ordine, file)

        self.diminuisci_quantita()
        self.callback(ordine)
        self.close()

    def genera_codice(self):
        length = 8  # Lunghezza del codice
        characters = string.ascii_letters + string.digits  # Caratteri ammissibili (lettere maiuscole/minuscole e numeri)
        codice = ''.join(random.choice(characters) for _ in range(length))
        return codice

    def diminuisci_quantita(self):
        for prodotto, quantita, _ in self.prodotti_selezionati:
            if isinstance(prodotto, Bottiglia):
                disponibilita_bottiglia = prodotto.get_disponibilta_bottiglia()
                if quantita <= disponibilita_bottiglia:
                    prodotto.set_disponibilita_bottiglia(disponibilita_bottiglia - quantita)

                    # Aggiorna la bottiglia corrispondente nella lista delle bottiglie salvate
                    for bottiglia_salvata in self.vista_scegli_prodotto.bottiglie_salvate:
                        if bottiglia_salvata.get_nome() == prodotto.get_nome():
                            bottiglia_salvata.set_disponibilita_bottiglia(disponibilita_bottiglia - quantita)
                            break

                    # Salva le bottiglie aggiornate nel file
                    with open('Dati/lista_bottiglie_salvate.pickle', 'wb') as f:
                        pickle.dump(self.vista_scegli_prodotto.bottiglie_salvate, f)

        with open('Dati/lista_prodotti_salvati.pickle', 'wb') as f:
            pickle.dump(self.vista_scegli_prodotto.prodotti, f)
