from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QComboBox, QDateTimeEdit, QMessageBox


class VistaInserisciBottiglia(QWidget):
    def __init__(self, callback, parent=None):
        super(VistaInserisciBottiglia, self).__init__(parent)
        self.callback = callback
        # Creazione dei widget
        label_top = QLabel("Inserisci i dati del prodotto:", self)
        label_nome = QLabel("NOME:", self)
        label_prezzo = QLabel("PREZZO:", self)
        label_disponibilta = QLabel("DISPONIBILITA':", self)
        label_posizione = QLabel("Posizione:", self)
        label_corridio = QLabel("CORRIDOIO: (1-2)", self)
        label_scaffale = QLabel("SCAFFALE: (1-20)", self)
        label_piano = QLabel("PIANO: (1-5)", self)

        self.line_edit_nome = QLineEdit(self)
        self.line_edit_prezzo = QLineEdit(self)
        self.line_edit_disponibilta = QLineEdit(self)
        self.line_edit_corridoio = QLineEdit(self)
        self.line_edit_scaffale = QLineEdit(self)
        self.line_edit_piano = QLineEdit(self)

        button_conferma = QPushButton("Conferma", self)
        button_conferma.clicked.connect(self.add_bottiglia)

        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Inserisci Bottiglia')
        self.setFixedSize(400, 600)  # Imposta la dimensione fissa della finestra di dialogo
        label_top.setFixedSize(300, 30)  # Imposta la dimensione fissa della label superiore
        label_posizione.setFixedSize(300, 30)  # Imposta la dimensione fissa della label "Inserisci i prezzi dei servizi"

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(label_top)
        layout.addWidget(label_nome)
        layout.addWidget(self.line_edit_nome)
        layout.addWidget(label_prezzo)
        layout.addWidget(self.line_edit_prezzo)
        layout.addWidget(label_disponibilta)
        layout.addWidget(self.line_edit_disponibilta)
        layout.addWidget(label_posizione)
        layout.addWidget(label_corridio)
        layout.addWidget(self.line_edit_corridoio)
        layout.addWidget(label_scaffale)
        layout.addWidget(self.line_edit_scaffale)
        layout.addWidget(label_piano)
        layout.addWidget(self.line_edit_piano)
        layout.addWidget(button_conferma)

        self.setLayout(layout)

    def add_bottiglia(self):
        pass