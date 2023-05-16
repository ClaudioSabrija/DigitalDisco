from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
     QComboBox, QDateTimeEdit


class VistaInserisciEvento(QWidget):
    def __init__(self, parent=None):
        super(VistaInserisciEvento, self).__init__(parent)

        # Creazione dei widget
        label_top = QLabel("Inserisci i dati dell'evento:", self)
        label_nome = QLabel("NOME:", self)
        label_tipo = QLabel("TIPO:", self)
        label_data = QLabel("DATA:", self)
        label_prezzi = QLabel("Inserisci i prezzi dei servizi:", self)
        label_ingresso = QLabel("INGRESSO:", self)
        label_tavolo = QLabel("TAVOLO:", self)
        label_prive = QLabel("PRIVE:", self)

        line_edit_nome = QLineEdit(self)
        combo_box_tipo = QComboBox(self)
        date_edit_data = QDateTimeEdit(self)

        line_edit_ingresso = QLineEdit(self)
        line_edit_tavolo = QLineEdit(self)
        line_edit_prive = QLineEdit(self)

        button_conferma = QPushButton("Conferma", self)
        button_conferma.clicked.connect(self.add_evento)

        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Inserisci Evento')
        self.setFixedSize(400, 600)  # Imposta la dimensione fissa della finestra di dialogo
        label_top.setFixedSize(300, 30)  # Imposta la dimensione fissa della label superiore
        label_prezzi.setFixedSize(300, 30)  # Imposta la dimensione fissa della label "Inserisci i prezzi dei servizi"

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(label_top)
        layout.addWidget(label_nome)
        layout.addWidget(line_edit_nome)
        layout.addWidget(label_tipo)
        layout.addWidget(combo_box_tipo)
        layout.addWidget(label_data)
        layout.addWidget(date_edit_data)
        layout.addWidget(label_prezzi)
        layout.addWidget(label_ingresso)
        layout.addWidget(line_edit_ingresso)
        layout.addWidget(label_tavolo)
        layout.addWidget(line_edit_tavolo)
        layout.addWidget(label_prive)
        layout.addWidget(line_edit_prive)
        layout.addWidget(button_conferma)

        self.setLayout(layout)

    def add_evento(self):
        pass


