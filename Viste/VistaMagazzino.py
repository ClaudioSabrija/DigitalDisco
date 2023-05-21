from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QSizePolicy, \
    QListView, QHBoxLayout

from Magazzino.Magazzino import Magazzino
from Viste.VistaInserisciBottiglia import VistaInserisciBottiglia
from Viste.VistaInserisciCocktail import VistaInserisciCocktail


class VistaMagazzino(QWidget):
    def __init__(self, parent = None):
        super(VistaMagazzino, self).__init__(parent)

        self.controller = Magazzino()

        grid_layout = QGridLayout()
        v_layout_bottiglie = QVBoxLayout()
        v_layout_cocktail = QVBoxLayout()
        v_layout_ricerca = QHBoxLayout()

        self.list_view_bottiglie = QListView()
        self.list_view_cocktail = QListView()
        self.update_ui_bottiglie()
        self.update_ui_cocktail()

        font = QFont('Arial Nova Light', 14)

        label_ricerca = QLabel("Nome:")
        self.label_ricerca = QLineEdit()
        v_layout_ricerca.addWidget(label_ricerca)
        v_layout_ricerca.addWidget(self.label_ricerca)

        button_ricerca = QPushButton('RICERCA')
        button_ricerca.clicked.connect(self.ricerca_prodotto)

        label_bottiglie = QLabel("Lista Bottiglie:")
        font.setItalic(True)
        label_bottiglie.setFont(font)
        v_layout_bottiglie.addWidget(label_bottiglie)
        v_layout_bottiglie.addWidget(self.list_view_bottiglie)

        label_cocktail = QLabel("Lista Cocktail:")
        font.setItalic(True)
        label_cocktail.setFont(font)
        v_layout_cocktail.addWidget(label_cocktail)
        v_layout_cocktail.addWidget(self.list_view_cocktail)

        buttons_bottiglie = QVBoxLayout()
        open_prodotto = QPushButton("Visualizza Bottiglia")
        open_prodotto.clicked.connect(self.show_selected_bottiglia)
        buttons_bottiglie.addWidget(open_prodotto)
        preleva_prodotto = QPushButton("Preleva Bottiglia")
        preleva_prodotto.clicked.connect(self.preleva_selected_bottiglia)
        buttons_bottiglie.addWidget(preleva_prodotto)
        inserisci_prodotto = QPushButton("Inserisci Bottiglia")
        inserisci_prodotto.clicked.connect(self.inserisci_bottiglia)
        buttons_bottiglie.addWidget(inserisci_prodotto)

        buttons_cocktail = QVBoxLayout()
        open_prodotto1 = QPushButton("Visualizza Cocktail")
        open_prodotto1.clicked.connect(self.show_selected_cocktail)
        buttons_cocktail.addWidget(open_prodotto1)
        inserisci_prodotto1 = QPushButton("Inserisci Cocktail")
        inserisci_prodotto1.clicked.connect(self.inserisci_cocktail)
        buttons_cocktail.addWidget(inserisci_prodotto1)

        grid_layout.addLayout(v_layout_ricerca, 0, 0)
        grid_layout.addLayout(v_layout_bottiglie, 1, 0)
        grid_layout.addLayout(v_layout_cocktail, 1, 1)
        grid_layout.addLayout(buttons_bottiglie, 2, 0)
        grid_layout.addLayout(buttons_cocktail, 2, 1)
        grid_layout.addWidget(button_ricerca, 0, 1, 1, 1, alignment=Qt.AlignBottom)

        self.setLayout(grid_layout)
        self.setFont(QFont('Arial Nova Light'))
        self.setWindowTitle("Gestione Magazzino")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

        self.setMaximumSize(900, 400)
        self.resize(900, 500)
        self.move(200, 200)

    # Funzione che mostra il prodotto selezionato.
    def show_selected_bottiglia(self):
        pass

    # Funzione che preleva il prodotto selezionato.
    def preleva_selected_bottiglia(self):
        pass

    # Funzione che mostra la vista che permette l'inserimento di un nuovo prodotto.
    def inserisci_bottiglia(self):
        self.vista_inserisci_bottiglia = VistaInserisciBottiglia(callback=self.update_ui_bottiglie)
        self.vista_inserisci_bottiglia.show()

    # Funzione che mostra il prodotto selezionato..
    def show_selected_cocktail(self):
        pass

    # Funzione che mostra la vista che permette l'inserimento di un nuovo prodotto.
    def inserisci_cocktail(self):
        self.vista_inserisci_cocktail = VistaInserisciCocktail(callback=self.update_ui_cocktail)
        self.vista_inserisci_cocktail.show()

    def ricerca_prodotto(self):
        pass

    #Funzione che popola le liste dei prodotti presenti nel magazzino
    def update_ui_bottiglie(self):
        self.list_view_bottiglie_model = QStandardItemModel(self.list_view_bottiglie)
        for bottiglie in self.controller.get_lista_bottiglie():
            item = QStandardItem()
            item.setText(bottiglie.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(15)
            item.setFont(font)
            self.list_view_bottiglie_model.appendRow(item)
        self.list_view_bottiglie.setModel(self.list_view_bottiglie_model)

    def update_ui_cocktail(self):
        self.list_view_cocktail_model = QStandardItemModel(self.list_view_cocktail)
        for cocktail in self.controller.get_lista_cocktail():
            item = QStandardItem()
            item.setText(cocktail.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(15)
            item.setFont(font)
            self.list_view_cocktail_model.appendRow(item)
        self.list_view_cocktail.setModel(self.list_view_cocktail_model)

    # Funzione che richiama il metodo del controllore che salva i dati aggiornati.
    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()

