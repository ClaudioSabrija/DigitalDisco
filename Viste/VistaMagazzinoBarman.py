from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, \
    QListView, QHBoxLayout, QInputDialog

from Magazzino.Magazzino import Magazzino


class VistaMagazzinoBarman(QWidget):
    def __init__(self, parent=None):
        super(VistaMagazzinoBarman, self).__init__(parent)

        self.controller = Magazzino()

        v_layout = QVBoxLayout()  # Layout principale
        v_layout.setAlignment(Qt.AlignCenter)  # Allinea il layout al centro

        h_layout_ricerca = QHBoxLayout()
        self.list_view_bottiglie = QListView()
        self.update_ui()

        font = QFont('Arial Nova Light', 14)

        label_ricerca = QLabel("Nome:")
        self.label_ricerca = QLineEdit()

        label_bottiglie = QLabel("Lista Bottiglie:")
        font.setItalic(True)
        label_bottiglie.setFont(font)

        buttons_bottiglie = QVBoxLayout()
        preleva_prodotto = QPushButton("Preleva Bottiglia")
        preleva_prodotto.clicked.connect(self.preleva_selected_bottiglia)
        buttons_bottiglie.addWidget(preleva_prodotto)

        v_layout.addWidget(label_bottiglie)
        v_layout.addWidget(self.list_view_bottiglie)
        v_layout.addLayout(buttons_bottiglie)

        self.setLayout(v_layout)
        self.setFont(QFont('Arial Nova Light'))
        self.setWindowTitle("Magazzino: Barman")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

        self.setMaximumSize(400, 500)
        self.resize(400, 500)
        self.move(200, 200)

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

    # Funzione che richiama il metodo del controllore che salva i dati aggiornati.
    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()