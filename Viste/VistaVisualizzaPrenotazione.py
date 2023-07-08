import pickle
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, \
    QComboBox, QDateTimeEdit, QMessageBox, QHBoxLayout

from Viste import VistaInserisciEvento
from Viste.VistaModificaEvento import VistaModificaEvento
from Evento.Evento import Evento
from Gestione.GestoreEventi import GestoreEventi
from Viste import VistaCalendarioEventi



class VistaVisualizzaPrenotazione(QWidget):
    def __init__(self, evento,prenotazione, callback_aggioramento, elimina_prenotazione_callback=None, modifica_prenotazione_callback=None, visualizza_pdf_callback=None, parent=None):
        super(VistaVisualizzaPrenotazione, self).__init__(parent)
        self.evento = evento
        self.prenotazione = prenotazione
        self.elimina_prenotazione_callback = elimina_prenotazione_callback
        self.modifica_prenotazione_callback = modifica_prenotazione_callback
        self.visualizza_pdf_callback = visualizza_pdf_callback
        self.callback_aggioramento = callback_aggioramento

        dati_prenotazione_layout = QVBoxLayout()
        scelte_prenotazione_layout = QVBoxLayout()


        # Creazione dei widget
        self.label_titolo = QLabel("Dettagli Prenotazione\n")
        self.label_nome = QLabel(f"Nome: {self.prenotazione.nome}", self)
        self.label_cognome = QLabel(f"Cognome: {self.prenotazione.cognome}", self)
        self.label_data_di_nascita = QLabel(f"Data di nascita: {self.prenotazione.data_di_nascita}", self)
        self.label_codice_fiscale = QLabel(f"Codice Fiscale: {self.prenotazione.codice_fiscale}", self)
        self.label_email = QLabel(f"E-mail: {self.prenotazione.email}", self)
        self.label_servizio = QLabel(f"Servizio: {self.prenotazione.servizio}", self)
        self.label_note = QLabel(f"Partecipanti: {self.prenotazione.note}", self)

        #Impostazione del Font
        font = QFont('Arial Nova Light')
        font.setPointSize(15)

        self.labels = [self.label_nome, self.label_cognome, self.label_data_di_nascita, self.label_codice_fiscale, self.label_email, self.label_servizio, self.label_note]  # Aggiungo tutte le tue label a questa lista

        for label in self.labels:
            label.setFont(font)
            label.setAlignment(Qt.AlignLeft)

        font_titolo = QFont('Arial Nova Light')
        font_titolo.setPointSize(20)
        font_titolo.setBold(True)


        self.label_titolo.setFont(font_titolo)
        self.label_titolo.setAlignment(Qt.AlignLeft)

        #Aggiunta delle label al layout
        dati_prenotazione_layout.addWidget(self.label_titolo)
        dati_prenotazione_layout.addWidget(self.label_nome)
        dati_prenotazione_layout.addWidget(self.label_cognome)
        dati_prenotazione_layout.addWidget(self.label_data_di_nascita)
        dati_prenotazione_layout.addWidget(self.label_codice_fiscale)
        dati_prenotazione_layout.addWidget(self.label_email)
        dati_prenotazione_layout.addWidget(self.label_servizio)
        dati_prenotazione_layout.addWidget(self.label_note)

        # Creazione del layout principale
        layout = QVBoxLayout()
        layout.addLayout(dati_prenotazione_layout)
        layout.addLayout(scelte_prenotazione_layout)

        # Impostazione del layout principale per il widget
        self.setLayout(layout)   #cioè tutti i widget di self hanno come layout il layout principale


        button_modifica_prenotazione = QPushButton("MODIFICA PRENOTAZIONE")
        button_modifica_prenotazione.clicked.connect(self.modifica_prenotazione_callback)
        scelte_prenotazione_layout.addWidget(button_modifica_prenotazione)

        button_elimina_prenotazione = QPushButton('ELIMINA PRENOTAZIONE')
        button_elimina_prenotazione.clicked.connect(self.elimina_prenotazione_callback)
        scelte_prenotazione_layout.addWidget(button_elimina_prenotazione)

        button_visualizza_pdf = QPushButton('VISUALIZZA PDF')
        button_visualizza_pdf.clicked.connect(self.visualizza_pdf_callback)
        scelte_prenotazione_layout.addWidget(button_visualizza_pdf)

        self.setMaximumSize(800,300)  #Fisso la dimensione massima della finestra
        self.resize(800, 300)  #Fisso la dimensione iniziale della finestra



        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Visualizza Prenotazione')

    def update_ui_prenotazione(self, prenotazione):
        # Aggiorna l'evento visualizzato con le modifiche apportate
        self.label_nome.setText(f"NOME: {prenotazione.nome}")
        self.label_cognome.setText(f"COGNOME: {prenotazione.cognome}")
        self.label_data_di_nascita.setText(f"DATA DI NASCITA: {prenotazione.data_di_nascita}")
        self.label_codice_fiscale.setText(f"CODICE FISCALE: {prenotazione.codice_fiscale}")
        self.label_email.setText(f"EMAIL: {prenotazione.email}")
        self.label_servizio.setText(f"SERVIZIO: {prenotazione.servizio}")
        self.label_note.setText(f"PARTECIPANTI: {prenotazione.note}")
        self.callback_aggioramento(self.evento)

