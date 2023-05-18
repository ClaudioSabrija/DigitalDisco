from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QComboBox, QDateTimeEdit, QMessageBox

from Evento.Evento import Evento
from Gestione.GestoreEventi import GestoreEventi
from Viste import VistaCalendarioEventi

class VistaInserisciEvento(QWidget):
    def __init__(self, callback, parent=None):
        super(VistaInserisciEvento, self).__init__(parent)
        self.callback = callback
        # Creazione dei widget
        label_top = QLabel("Inserisci i dati dell'evento:", self)
        label_nome = QLabel("NOME:", self)
        label_tipo = QLabel("TIPO:", self)
        label_data = QLabel("DATA:", self)
        label_prezzi = QLabel("Inserisci i prezzi dei servizi:", self)
        label_ingresso = QLabel("INGRESSO:", self)
        label_tavolo = QLabel("TAVOLO:", self)
        label_prive = QLabel("PRIVE:", self)

        self.line_edit_nome = QLineEdit(self)
        self.combo_box_tipo = QComboBox(self)
        self.date_edit_data = QDateTimeEdit(self)

        self.line_edit_ingresso = QLineEdit(self)
        self.line_edit_tavolo = QLineEdit(self)
        self.line_edit_prive = QLineEdit(self)

        button_conferma = QPushButton("Conferma", self)
        button_conferma.clicked.connect(self.add_evento)

        self.combo_box_tipo.addItem("Musica Commerciale")
        self.combo_box_tipo.addItem("Musica Latina")
        self.combo_box_tipo.addItem("Musica Techno")
        self.combo_box_tipo.addItem("Musica Rap")

        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Inserisci Evento')
        self.setFixedSize(400, 600)  # Imposta la dimensione fissa della finestra di dialogo
        label_top.setFixedSize(300, 30)  # Imposta la dimensione fissa della label superiore
        label_prezzi.setFixedSize(300, 30)  # Imposta la dimensione fissa della label "Inserisci i prezzi dei servizi"

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(label_top)
        layout.addWidget(label_nome)
        layout.addWidget(self.line_edit_nome)
        layout.addWidget(label_tipo)
        layout.addWidget(self.combo_box_tipo)
        layout.addWidget(label_data)
        layout.addWidget(self.date_edit_data)
        layout.addWidget(label_prezzi)
        layout.addWidget(label_ingresso)
        layout.addWidget(self.line_edit_ingresso)
        layout.addWidget(label_tavolo)
        layout.addWidget(self.line_edit_tavolo)
        layout.addWidget(label_prive)
        layout.addWidget(self.line_edit_prive)
        layout.addWidget(button_conferma)

        self.setLayout(layout)

    def add_evento(self):
        # Ottenere i valori inseriti dall'utente
        nome = self.line_edit_nome.text().strip()
        tipo = self.combo_box_tipo.currentText()
        data = self.date_edit_data.dateTime().toString("yyyy-MM-dd")
        ingresso = self.line_edit_ingresso.text().strip()
        tavolo = self.line_edit_tavolo.text().strip()
        prive = self.line_edit_prive.text().strip()

        # Controllo dei campi compilati
        if not nome or not tipo or not data or not ingresso or not tavolo or not prive:
            QMessageBox.warning(self, "Errore", "Tutti i campi devono essere compilati.")
            return

        # Controllo se i campi d'ingresso, tavolo e prive sono interi
        try:
            ingresso = int(ingresso)
            tavolo = int(tavolo)
            prive = int(prive)
        except ValueError:
            QMessageBox.warning(self, "Errore", "I campi di ingresso, tavolo e prive devono essere numeri interi.")
            return

        evento = GestoreEventi()

        evento.inserisci_evento(nome, tipo, data, ingresso, tavolo, prive)

        self.callback()
        self.close()



