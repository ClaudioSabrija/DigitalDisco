import os.path, pickle

from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListView, QPushButton, QInputDialog, QLabel, QLineEdit

from Magazzino.Bottiglia import Bottiglia
from Magazzino.Prodotto import Prodotto



class VistaScegliProdotto(QWidget):
    def __init__(self, callback, parent=None):
        super().__init__(parent)

        self.callback = callback
        self.prodotti_selezionati = []



        self.layout = QVBoxLayout()

        # Barra di ricerca
        ricerca_layout = QHBoxLayout()
        ricerca_label = QLabel("Ricerca:")
        self.ricerca_line_edit = QLineEdit()
        self.ricerca_line_edit.textChanged.connect(self.ricerca_prodotti)
        ricerca_layout.addWidget(ricerca_label)
        ricerca_layout.addWidget(self.ricerca_line_edit)
        self.layout.addLayout(ricerca_layout)

        # ListView per i prodotti selezionati
        self.list_view = QListView()
        self.layout.addWidget(self.list_view)

        Prodotto.unione_lista_prodotti()
        self.popola_lista()

        # Layout per i bottoni
        buttons_layout = QHBoxLayout()

        # Bottone "Conferma"
        self.btn_conferma = QPushButton("Conferma")
        buttons_layout.addWidget(self.btn_conferma)
        self.btn_conferma.clicked.connect(self.add_prodotto_in_lista)

        self.layout.addLayout(buttons_layout)

        self.setLayout(self.layout)
        self.resize(650, 550)
        self.setWindowTitle("Scegli Prodotti")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

    def popola_lista(self):

        if os.path.isfile('Dati/lista_prodotti_salvati.pickle'):
            with open('Dati/lista_prodotti_salvati.pickle', 'rb') as f:
                prodotti = pickle.load(f)

                self.prodotti = prodotti

                self.list_view_model = QStandardItemModel(self.list_view)
                for prodotto in prodotti:
                    item = QStandardItem()
                    if isinstance(prodotto, Bottiglia): # se è una bottiglia allora mostra la disp. perchè la bottiglia ha essa come attributo
                        item.setText(f"{prodotto.get_nome()} - {prodotto.get_prezzo()}\u20AC "
                                     f"- Disponibilità:{prodotto.get_disponibilta()}") #\u20AC è l'unicode dell'Euro
                    else:   item.setText(f"{prodotto.get_nome()} - {prodotto.get_prezzo()}\u20AC")
                    item.setEditable(False)
                    font = item.font()
                    font.setPointSize(13)
                    item.setFont(font)
                    self.list_view_model.appendRow(item)
                self.list_view.setModel(self.list_view_model)

    def ricerca_prodotti(self):
        if os.path.isfile('Dati/lista_prodotti_salvati.pickle'):
            with open('Dati/lista_prodotti_salvati.pickle', 'rb') as f:
                prodotti = pickle.load(f)

        ricerca_text = self.ricerca_line_edit.text().lower()

        for row in range(self.list_view_model.rowCount()):
            item = self.list_view_model.item(row)
            prodotto = self.prodotti[row]
            nome_prodotto = prodotto.get_nome().lower()

            if ricerca_text and ricerca_text in nome_prodotto:  # Ho che se digito mi trova i prodotti con le lettere
                self.list_view.setRowHidden(row, False)         # che ho digitato altrimenti mi dà la lista completa
            else:
                self.list_view.setRowHidden(row, ricerca_text != "")

    def add_prodotto_in_lista(self):
        # Ottieni l'elemento selezionato dalla ListView
        indexes = self.list_view.selectedIndexes()
        if indexes:
            selected_index = indexes[0]
            item = self.list_view.model().itemData(selected_index)
            prodotto_selezionato = item[0]

            # Ottieni il nome del prodotto selezionato
            nome_prodotto = prodotto_selezionato.split(' - ')[0]

            # Ottieni il prodotto corrispondente dal tuo elenco di prodotti
            prodotto = None
            for p in self.prodotti:
                if p.get_nome() == nome_prodotto:
                    prodotto = p
                    break

            if prodotto is not None:
                if isinstance(prodotto, Bottiglia):
                    # Mostra la finestra di dialogo per l'inserimento della quantità
                    quantita, ok = QInputDialog.getInt(self, "Inserisci Quantità", "Quantità:", min=1,
                                                       max=prodotto.get_disponibilta_bottiglia())
                else:
                    quantita, ok = QInputDialog.getInt(self, "Inserisci Quantità", "Quantità:", min=1)

                if ok and quantita:
                    if isinstance(prodotto,Bottiglia):
                        # Sottrai la quantità selezionata dalla disponibilità del prodotto
                        prodotto.set_disponibilita_bottiglia(prodotto.get_disponibilta_bottiglia() - quantita)

                    with open('Dati/lista_prodotti_salvati.pickle', 'wb') as f:
                        pickle.dump(self.prodotti, f)

                if quantita <= 0:
                    return

                prezzo_totale = prodotto.get_prezzo() * quantita

                prodotti_selezionati = (prodotto, prezzo_totale)
                self.prodotti_selezionati.append(prodotti_selezionati)

                # Aggiungi il prodotto selezionato e confermato nella ListView della classe VistaNuovoOrdine
                self.callback()
                self.close()

    def get_selected_products(self):
        return self.prodotti_selezionati

    def closeEvent(self, event):
        with open('Dati/lista_prodotti_salvati.pickle', 'wb') as f:
            pickle.dump(self.prodotti, f)
        super().closeEvent(event)
