from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, \
    QListView, QHBoxLayout, QInputDialog

from Magazzino.Magazzino import Magazzino
from Viste.VistaInserisciBottiglia import VistaInserisciBottiglia
from Viste.VistaInserisciCocktail import VistaInserisciCocktail
from Viste.VistaVisualizzaBottiglia import VistaVisualizzaBottiglia
from Viste.VistaVisualizzaCocktail import VistaVisualizzaCocktail


class VistaMagazzino(QWidget):
    def __init__(self, parent=None):
        super(VistaMagazzino, self).__init__(parent)

        self.controller = Magazzino()

        grid_layout = QGridLayout()
        v_layout_bottiglie = QVBoxLayout()
        v_layout_cocktail = QVBoxLayout()
        v_layout_ricerca = QHBoxLayout()

        self.list_view_bottiglie = QListView()
        self.list_view_cocktail = QListView()
        self.update_ui()

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

        self.setMaximumSize(1000, 600)
        self.resize(900, 500)
        self.move(200, 200)

    # Funzione che mostra il prodotto selezionato.
    def show_selected_bottiglia(self):
        if self.list_view_bottiglie.selectedIndexes():
            selected = self.list_view_bottiglie.selectedIndexes()[0].row()
            self.bottiglia_selezionata = self.controller.get_bottiglia_by_index_(selected)
            self.vista_visualizza_bottiglia = VistaVisualizzaBottiglia(self.bottiglia_selezionata)
            self.vista_visualizza_bottiglia.show()

    # Funzione che preleva il prodotto selezionato.
    def preleva_selected_bottiglia(self):
        selected_index = self.list_view_bottiglie.selectedIndexes()
        if not selected_index:
            return

        selected_row = selected_index[0].row()
        self.bottiglia_selezionata = self.controller.get_bottiglia_by_index_(selected_row)

        if self.bottiglia_selezionata:
            disponibilita = self.bottiglia_selezionata.get_disponibilta_bottiglia()
            if disponibilita == 0:
                QMessageBox.warning(self, "Errore", "La bottiglia selezionata non è disponibile.")
                return

            # Mostra la finestra di dialogo per chiedere la quantità di bottiglie da prelevare
            num_bottiglie, ok = QInputDialog.getInt(self, "Preleva bottiglia", "Quantità da prelevare:", min=1,
                                                    max=disponibilita)
            if ok:
                if num_bottiglie > disponibilita:
                    QMessageBox.warning(self, "Errore", "La quantità inserita supera la disponibilità della bottiglia.")
                    return

                # Effettua il prelievo delle bottiglie
                self.bottiglia_selezionata.set_disponibilita_bottiglia(disponibilita - num_bottiglie)
                QMessageBox.information(self, "Successo", "Bottiglie prelevate con successo.")

                # Aggiorna l'interfaccia utente
                self.update_ui()

    # Funzione che mostra la vista che permette l'inserimento di un nuovo prodotto.
    def inserisci_bottiglia(self):
        self.vista_inserisci_bottiglia = VistaInserisciBottiglia(callback=self.controller.aggiungi_bottiglia)
        self.update_ui()
        self.vista_inserisci_bottiglia.show()

    # Funzione che mostra il prodotto selezionato..
    def show_selected_cocktail(self):
        if self.list_view_cocktail.selectedIndexes():
            selected = self.list_view_cocktail.selectedIndexes()[0].row()
            cocktail_selezionato = self.controller.get_cocktail_by_index(selected)
            self.vista_visualizza_cocktail = VistaVisualizzaCocktail(cocktail_selezionato)
            self.vista_visualizza_cocktail.show()

    # Funzione che mostra la vista che permette l'inserimento di un nuovo prodotto.
    def inserisci_cocktail(self):
        self.vista_inserisci_cocktail = VistaInserisciCocktail(callback=self.controller.aggiungi_cocktail)
        self.vista_inserisci_cocktail.show()

    def ricerca_prodotto(self):
        nome_prodotto = self.label_ricerca.text()  # il nome viene preso da quello che scrivo nella Label

        for index in range(self.list_view_bottiglie_model.rowCount()):  # scorre con l'iteratore index nella list_view delle bottiglie
            item = self.list_view_bottiglie_model.item(index)  # viene ottenuto l'elemento corrente del modello
            if item.text() == nome_prodotto:  # confronta l'elemento con il nome da noi cercato
                self.list_view_bottiglie.setCurrentIndex(item.index())  # viene ottenuto l'elemento corrente del modello se si trova una corrispondenza
                self.show_selected_bottiglia()
                return

        for index in range(self.list_view_cocktail_model.rowCount()):
            item = self.list_view_cocktail_model.item(index)
            if item.text() == nome_prodotto:
                self.list_view_cocktail.setCurrentIndex(item.index())
                self.show_selected_cocktail()
                return

        # Se il prodotto non viene trovato, mostra un messaggio di avviso
        QMessageBox.warning(self, "Prodotto non trovato", "Il prodotto cercato non è stato trovato.")

    def update_ui(self):
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

