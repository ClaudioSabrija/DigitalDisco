from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QMessageBox

from GestoreMagazzino.Controller.GestoreMagazzino import GestoreMagazzino
from GestoreMagazzino.Model.Bottiglia import Bottiglia
from GestoreMagazzino.Model.Magazzino import Magazzino


class VistaModificaBottiglia(QWidget):
    def __init__(self, bottiglia, callback, callback_modifica, parent=None):
        super(VistaModificaBottiglia, self).__init__(parent)

        self.callback_modifica = callback_modifica
        self.bottiglia = bottiglia
        self.callback = callback
        self.magazzino = Magazzino()
        self.controller = GestoreMagazzino(self.magazzino)

        # Creazione dei widget
        label_top = QLabel("Modifica i dati del prodotto:", self)
        label_nome = QLabel("NOME:", self)
        label_prezzo = QLabel("PREZZO:", self)
        label_disponibilita = QLabel("DISPONIBILITA':", self)
        label_posizione = QLabel("Posizione:", self)
        label_corridio = QLabel("CORRIDOIO: (1-2)", self)
        label_scaffale = QLabel("SCAFFALE: (1-20)", self)
        label_piano = QLabel("PIANO: (1-5)", self)

        self.line_edit_nome = QLineEdit(self)
        self.line_edit_prezzo = QLineEdit(self)
        self.line_edit_disponibilita = QLineEdit(self)
        self.line_edit_corridoio = QLineEdit(self)
        self.line_edit_scaffale = QLineEdit(self)
        self.line_edit_piano = QLineEdit(self)

        button_conferma = QPushButton("Conferma", self)
        button_conferma.clicked.connect(self.modifica_bottiglia)

        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Modifica Bottiglia')
        self.setFixedSize(400, 400)
        label_top.setFixedSize(300, 30)

        # Inizializza i campi con i valori attuali della bottiglia
        self.line_edit_nome.setText(self.bottiglia.nome)
        self.line_edit_prezzo.setText(str(self.bottiglia.prezzo))
        self.line_edit_disponibilita.setText(str(self.bottiglia.disponibilita))
        self.line_edit_corridoio.setText(str(self.bottiglia.corridoio))
        self.line_edit_scaffale.setText(str(self.bottiglia.scaffale))
        self.line_edit_piano.setText(str(self.bottiglia.piano))

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(label_top)
        layout.addWidget(label_nome)
        layout.addWidget(self.line_edit_nome)
        layout.addWidget(label_prezzo)
        layout.addWidget(self.line_edit_prezzo)
        layout.addWidget(label_disponibilita)
        layout.addWidget(self.line_edit_disponibilita)
        layout.addWidget(label_posizione)
        layout.addWidget(label_corridio)
        layout.addWidget(self.line_edit_corridoio)
        layout.addWidget(label_scaffale)
        layout.addWidget(self.line_edit_scaffale)
        layout.addWidget(label_piano)
        layout.addWidget(self.line_edit_piano)
        layout.addWidget(button_conferma)

        self.setLayout(layout)

    def modifica_bottiglia(self):
        nome = self.line_edit_nome.text().strip()
        prezzo = self.line_edit_prezzo.text().strip()
        disponibilita = self.line_edit_disponibilita.text().strip()
        corridoio = self.line_edit_corridoio.text().strip()
        scaffale = self.line_edit_scaffale.text().strip()
        piano = self.line_edit_piano.text().strip()

        if not nome or not prezzo or not disponibilita or not corridoio or not scaffale or not piano:
            QMessageBox.warning(self, "Errore", "Tutti i campi devono essere compilati.")
            return

        try:
            prezzo = int(prezzo)
            disponibilita = int(disponibilita)
            corridoio = int(corridoio)
            scaffale = int(scaffale)
            piano = int(piano)
        except ValueError:
            QMessageBox.warning(self, "Errore", "I campi di ingresso: (Prezzo, Disponibilità, Corridoio, Scaffale,"
                                                "Piano) devono essere scritti in numero.")
            return

        if corridoio not in range(1, 3) or scaffale not in range(1, 21) or piano not in range(1, 6):
            QMessageBox.critical(self, "Errore", "I valori di corridoio, scaffale e piano devono essere numeri interi "
                                                 "compresi tra i seguenti intervalli:\n"
                                                 "Corridoio: 1-2\n"
                                                 "Scaffale: 1-20\n"
                                                 "Piano: 1-5")
            return

        # Controlla la posizione se è disponibile,se inserisco le stesse posizioni di quelle già presenti non da errore
        if (corridoio != self.bottiglia.corridoio or scaffale != self.bottiglia.scaffale or piano != self.bottiglia.piano) and \
                self.controller.posizione_occupata(corridoio, scaffale, piano):
            QMessageBox.warning(self, "Errore", "In questa posizione è già situata un'altra bottiglia.")
            return

        # Aggiorna i valori della bottiglia
        self.bottiglia.nome = nome
        self.bottiglia.prezzo = prezzo
        self.bottiglia.disponibilita = disponibilita
        self.bottiglia.corridoio = corridoio
        self.bottiglia.scaffale = scaffale
        self.bottiglia.piano = piano

        bottiglia_modificata = Bottiglia(nome, prezzo, disponibilita, corridoio, scaffale, piano)

        self.callback_modifica(bottiglia_modificata)
        self.callback(self.bottiglia, bottiglia_modificata)
        self.close()
