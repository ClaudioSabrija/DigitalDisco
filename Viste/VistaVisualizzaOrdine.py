from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListView, QPushButton, QInputDialog, QLabel, QLineEdit, \
    QMessageBox


class VistaVisualizzaOrdine(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()

        # Aggiunta della label "Ordine" centrata
        label_ordine = QLabel("Ordine")
        label_ordine.setAlignment(Qt.AlignCenter)
        label_ordine.setFont(QFont("Arial", 20))
        self.layout.addWidget(label_ordine)

        # ListView per i prodotti selezionati
        self.list_view = QListView()
        self.layout.addWidget(self.list_view)

        # Layout per i bottoni
        buttons_layout = QHBoxLayout()

        # Bottone "Conferma"
        self.btn_stampa = QPushButton("Stampa Ordine")
        buttons_layout.addWidget(self.btn_stampa)
        self.btn_stampa.clicked.connect(self.stampa_ordine)

        self.layout.addLayout(buttons_layout)

        self.setLayout(self.layout)
        self.resize(500, 450)
        self.setWindowTitle("Visualizza Ordine")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

    def stampa_ordine(self):
        # Creazione e visualizzazione della finestra di dialogo QMessageBox
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Stampa Ordine")  # Impostazione del titolo della finestra
        msg_box.setWindowIcon(QIcon('Dati/DigitalDisco.png'))  # Impostazione dell'icona della finestra
        msg_box.setText("Il tuo Ordine è stato stampato correttamente!")
        msg_box.exec_()
