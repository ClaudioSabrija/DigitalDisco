from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QComboBox, QDateTimeEdit, QMessageBox

from Viste import VistaInserisciEvento
from Evento.Evento import Evento
from Gestione.GestoreEventi import GestoreEventi

class VistaVisualizzaEvento(QWidget):
    def __init__(self, elimina_callback, parent=None):
        super(VistaVisualizzaEvento, self).__init__(parent)
        self.elimina_callback = elimina_callback
        self.info_evento_layout = QVBoxLayout()
        self.dati_evento_layout = QVBoxLayout()
        self.scelte_evento = QVBoxLayout()

        # Creazione dei widget
        label_nome = QLabel("NOME:", self)
        label_tipo = QLabel("TIPO:", self)
        label_data = QLabel("DATA:", self)
        label_ingresso = QLabel("INGRESSO:", self)
        label_tavolo = QLabel("TAVOLO:", self)
        label_prive = QLabel("PRIVE:", self)

        #Aggiunta delle label al layout delle informazioni

        info_evento_layout.addWidget(label_nome)
        info_evento_layout.addWidget(label_tipo)
        info_evento_layout.addWidget(label_data)

        #Aggiunta delle label alla griglia
        dati_evento_layout.addWidget(label_ingresso, 0, 0)  # riga 0, colonna 0
        dati_evento_layout.addWidget(label_tavolo, 1, 0)  # riga 1, colonna 0
        dati_evento_layout.addWidget(label_prive, 2, 0)  # riga 2, colonna 0

        dati_evento_layout.addWidget(line_edit_ingresso.text(), 0, 1)  # riga 0, colonna 1
        dati_evento_layout.addWidget(line_edit_tavolo.text(), 1, 1)  # riga 1, colonna 1
        dati_evento_layout.addWidget(line_edit_prive.text(), 2, 1)  # riga 2, colonna 1

        dati_evento_layout.addWidget('', 0, 2)  # riga 0, colonna 2
        dati_evento_layout.addWidget('', 1, 2)  # riga 1, colonna 2
        dati_evento_layout.addWidget('', 2, 2)  # riga 2, colonna 2

        button_modifica_evento = QPushButton("MODIFICA EVENTO", self)
        button_modifica_evento.clicked.connect(self.go_modifica_evento)
        v_layout.addWidget(button_modifica_evento)

        button_elimina_evento = QPushButton('ELIMINA EVENTO')
        button_elimina_evento.clicked.connect(lambda: self.elimina_evento_click(evento))
        v_layout.addWidget(button_elimina_evento)

        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Visualizza Evento')
        self.setFixedSize(500, 1000)  # Imposta la dimensione fissa della finestra di dialogo


    def elimina_evento_click(self, evento):
        if isinstance(evento, Evento):
            evento.rimuovi_evento()
        self.elimina_callback()
        self.close()

    def go_modifica_evento(self):
        pass