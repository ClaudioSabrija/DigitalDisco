from datetime import datetime
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QComboBox, QMessageBox

from GestoreEventi.Model.Evento import Evento

class VistaModificaEvento(QWidget):
    def __init__(self, evento, callback, callback_vista, parent=None):
        super(VistaModificaEvento, self).__init__(parent)
        self.callback = callback
        self.evento = evento
        self.callback_vista = callback_vista

        # Creazione dei widget
        self.label_top = QLabel("Modifica i dati dell'evento:", self)
        self.label_nome = QLabel("NOME:", self)
        self.label_tipo = QLabel("TIPO:", self)
        self.label_data = QLabel("DATA:", self)
        self.label_prezzi = QLabel("Inserisci i prezzi dei servizi:", self)
        self.label_ingresso = QLabel("INGRESSO:", self)
        self.label_tavolo = QLabel("TAVOLO:", self)
        self.label_prive = QLabel("PRIVE:", self)

        self.line_edit_nome = QLineEdit(self)
        self.combo_box_tipo = QComboBox(self)
        self.line_edit_data = QLineEdit(self)
        self.line_edit_ingresso = QLineEdit(self)
        self.line_edit_tavolo = QLineEdit(self)
        self.line_edit_prive = QLineEdit(self)

        self.button_conferma = QPushButton("Conferma", self)
        self.button_conferma.clicked.connect(self.modifica_evento)

        self.combo_box_tipo.addItem("Musica Commerciale")
        self.combo_box_tipo.addItem("Musica Latina")
        self.combo_box_tipo.addItem("Musica Techno")
        self.combo_box_tipo.addItem("Musica Rap")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Inserisci Evento')
        self.setFixedSize(400, 600)  # Imposta la dimensione fissa della finestra di dialogo

        self.label_top.setFixedSize(300, 30)  # Imposta la dimensione fissa della label superiore
        self.label_prezzi.setFixedSize(300, 30)  # Imposta la dimensione fissa della label "Inserisci i prezzi dei servizi"

        # Inizializza i campi con i valori attuali dell'evento
        self.line_edit_nome.setText(self.evento.nome)
        self.line_edit_data.setText(self.evento.data)
        self.line_edit_ingresso.setText(str(self.evento.prezzo_ingresso))
        self.line_edit_tavolo.setText(str(self.evento.prezzo_tavolo))
        self.line_edit_prive.setText(str(self.evento.prezzo_prive))

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label_top)
        layout.addWidget(self.label_nome)
        layout.addWidget(self.line_edit_nome)
        layout.addWidget(self.label_tipo)
        layout.addWidget(self.combo_box_tipo)
        layout.addWidget(self.label_data)
        layout.addWidget(self.line_edit_data)
        layout.addWidget(self.label_prezzi)
        layout.addWidget(self.label_ingresso)
        layout.addWidget(self.line_edit_ingresso)
        layout.addWidget(self.label_tavolo)
        layout.addWidget(self.line_edit_tavolo)
        layout.addWidget(self.label_prive)
        layout.addWidget(self.line_edit_prive)
        layout.addWidget(self.button_conferma)
        self.setLayout(layout)

    def modifica_evento(self):
        #Ottenere i valori inseriti dall'utente
        nome = self.line_edit_nome.text().strip()
        tipo = self.combo_box_tipo.currentText()
        data = self.line_edit_data.text().strip()
        ingresso = self.line_edit_ingresso.text().strip()
        tavolo = self.line_edit_tavolo.text().strip()
        prive = self.line_edit_prive.text().strip()

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
        try:
            giorno, mese, anno = data.split('/')
            data_inserita = QDate(int(giorno), int(mese), int(anno))
        except ValueError:
            QMessageBox.critical(self, "Errore", "Il formato della data inserita dev'essere:(dd/mm/yyyy).")
            return

        data_inserita = self.line_edit_data.text().strip()

        # Controllo se la data è precedente alla data odierna
        data_odierna = datetime.today().strftime("%d/%m/%Y")

        if datetime.strptime(data_inserita, "%d/%m/%Y") < datetime.strptime(data_odierna, "%d/%m/%Y"):
            QMessageBox.warning(self, "Errore", "La data dell'evento selezionato è precedente alla data odierna.\nPertanto non è più possibile modificare l'evento.")
            return

        evento_modificato = Evento(nome, data, tipo, ingresso, tavolo, prive)

        self.callback(self.evento, evento_modificato)
        self.callback_vista(evento_modificato)
        self.close()

