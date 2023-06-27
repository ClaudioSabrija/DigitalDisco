import os.path, pickle

from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListView, QPushButton, QInputDialog, QLabel, QLineEdit

from Magazzino.Prodotto import Prodotto



class VistaScegliProdotto(QWidget):
    def __init__(self):
        super().__init__()

        self.prodotti = []

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
        self.resize(350, 550)
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
                    item.setText(f"{prodotto.get_nome()} - {prodotto.get_prezzo()}\u20AC") #\u20AC è l'unicode dell'Euro
                    item.setEditable(False)
                    font = item.font()
                    font.setPointSize(13)
                    item.setFont(font)
                    self.list_view_model.appendRow(item)
                self.list_view.setModel(self.list_view_model)

    def add_prodotto_in_lista(self):
        pass

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
