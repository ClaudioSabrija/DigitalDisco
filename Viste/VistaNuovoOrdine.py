from PyQt5.QtGui import QIcon, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListView, QPushButton

from Viste.VistaScegliProdotto import VistaScegliProdotto
from Magazzino.Prodotto import Prodotto


class VistaNuovoOrdine(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        # ListView per i prodotti selezionati
        self.list_view = QListView()
        self.layout.addWidget(self.list_view)

        # Layout per i bottoni
        buttons_layout = QHBoxLayout()

        # Bottone "Inserisci Prodotto"
        self.btn_inserisci_prodotto = QPushButton("Inserisci Prodotto")
        buttons_layout.addWidget(self.btn_inserisci_prodotto)
        self.btn_inserisci_prodotto.clicked.connect(self.scegli_prodotto)

        # Bottone "Conferma"
        self.btn_conferma = QPushButton("Conferma")
        buttons_layout.addWidget(self.btn_conferma)
        self.btn_conferma.clicked.connect(self.add_prodotto)

        self.layout.addLayout(buttons_layout)

        self.setLayout(self.layout)
        self.resize(400, 450)
        self.setWindowTitle("Nuovo Ordine")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

    def scegli_prodotto(self):
        self.vista_scegli_prdotto = VistaScegliProdotto()
        self.vista_scegli_prdotto.show()

    def add_prodotto(self):
        pass