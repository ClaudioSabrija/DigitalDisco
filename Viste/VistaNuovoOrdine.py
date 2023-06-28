import pickle, string, random
from abc import abstractmethod

from PyQt5.QtGui import QIcon, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListView, QPushButton
from Viste.VistaScegliProdotto import VistaScegliProdotto


class VistaNuovoOrdine(QWidget):
    def __init__(self, evento_selezionato, callback):
        super().__init__()

        self.evento_selezionato = evento_selezionato
        self.layout = QVBoxLayout()
        self.prodotti = []
        self.callback = callback

        # ListView per i prodotti selezionati
        self.list_view = QListView()
        self.layout.addWidget(self.list_view)
        self.list_view_model = QStandardItemModel(self.list_view)

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
        prodotti_selezionati = self.vista_scegli_prodotto.get_selected_products()

        if prodotti_selezionati:
            for prodotto, prezzo_totale in prodotti_selezionati:
                # Aggiungi il prodotto al list_view_model
                item = QStandardItem()
                item.setText(f"{prodotto.get_nome()} - Prezzo Totale: {prezzo_totale}\u20AC")
                item.setEditable(False)
                font = item.font()
                font.setPointSize(13)
                item.setFont(font)
                self.list_view_model.appendRow(item)

            # Imposta il list_view_model sulla list_view
            self.list_view.setModel(self.list_view_model)

    def conferma_ordine(self):
        # Crea il codice ordine alfanumerico univoco
        codice_ordine = self.genera_codice()

        # Crea il testo dell'ordine
        ordine_text = f"Ordine: {codice_ordine}\n"
        for prodotto, prezzo in self.prodotti:
            ordine_text += f"Prodotto: {prodotto} - Prezzo: {prezzo}\u20AC\n"

        # Salva l'ordine nel file pickle dell'evento selezionato
        with open(f'Dati/Ordini/ordini_{self.evento_selezionato}.pickle', 'ab') as file:
            pickle.dump(ordine_text, file)

        self.callback(ordine_text)
        self.close()

    @abstractmethod
    def genera_codice(self):
        length = 8  # Lunghezza del codice
        characters = string.ascii_letters + string.digits  # Caratteri ammissibili (lettere maiuscole/minuscole e numeri)
        codice = ''.join(random.choice(characters) for _ in range(length))
        return codice

