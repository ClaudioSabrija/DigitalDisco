from datetime import date
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QComboBox,  QMessageBox


from GestorePrenotazioni.Controller.GestorePrenotazioni import GestorePrenotazioni
from GestoreEventi.Model.Evento import Evento
from GestorePrenotazioni.Model.Prenotazione import Prenotazione


class VistaVisualizzaPdf(QWidget):
    def __init__(self, prenotazione, parent=None):
        super(VistaVisualizzaPdf, self).__init__(parent)
        self.prenotazione = prenotazione


        dati_prenotazione_layout = QVBoxLayout()


        #Creazione widget per QrCode
        pixmap = QPixmap('Dati/qr_code.png')
        pixmap5 = pixmap.scaled(300, 300)
        self.label_qrcode = QLabel()
        self.label_qrcode.setPixmap(pixmap5)
        self.label_qrcode.setAlignment(Qt.AlignCenter)

        # Creazione dei widget
        self.label_titolo = QLabel("Dati cliente")
        self.label_nome = QLabel(f"Nome: {self.prenotazione.nome}", self)
        self.label_cognome = QLabel(f"Cognome: {self.prenotazione.cognome}", self)
        self.label_data_di_nascita = QLabel(f"Data di nascita: {self.prenotazione.data_di_nascita}", self)
        self.label_codice_fiscale = QLabel(f"Codice Fiscale: {self.prenotazione.codice_fiscale}", self)
        self.label_email = QLabel(f"E-mail: {self.prenotazione.email}", self)
        self.label_servizio = QLabel(f"Servizio: {self.prenotazione.servizio}", self)
        self.label_note = QLabel(f"Partecipanti: {self.prenotazione.note}", self)
        self.label_avviso = QLabel("Attenzione:Per l'accesso è obbligatorio un documento di riconoscimento in corso di validità\n ")
        #Impostazione del Font
        font = QFont('Arial Nova Light')
        font.setPointSize(15)

        self.labels = [self.label_titolo, self.label_nome, self.label_cognome, self.label_data_di_nascita, self.label_codice_fiscale,
                       self.label_email, self.label_servizio, self.label_note, self.label_avviso]  # Aggiungo tutte le tue label a questa lista

        for label in self.labels:
            label.setFont(font)
            label.setAlignment(Qt.AlignLeft)



        #Aggiunta delle label al layout
        dati_prenotazione_layout.addWidget(self.label_qrcode)
        dati_prenotazione_layout.addWidget(self.label_titolo)
        dati_prenotazione_layout.addWidget(self.label_nome)
        dati_prenotazione_layout.addWidget(self.label_cognome)
        dati_prenotazione_layout.addWidget(self.label_data_di_nascita)
        dati_prenotazione_layout.addWidget(self.label_codice_fiscale)
        dati_prenotazione_layout.addWidget(self.label_email)
        dati_prenotazione_layout.addWidget(self.label_servizio)
        dati_prenotazione_layout.addWidget(self.label_note)
        dati_prenotazione_layout.addWidget(self.label_avviso)

        # Creazione del layout principale
        layout = QVBoxLayout()
        layout.addLayout(dati_prenotazione_layout)

        # Impostazione del layout principale per il widget
        self.setLayout(layout)   #cioè tutti i widget di self hanno come layout il layout principale


        button_invia_pdf = QPushButton('INVIA PDF')
        button_invia_pdf.clicked.connect(self.invia_pdf)
        dati_prenotazione_layout.addWidget(button_invia_pdf)

        self.setMaximumSize(300,800)  #Fisso la dimensione massima della finestra
        self.resize(300, 800)  #Fisso la dimensione iniziale della finestra


        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Visualizza Prenotazione')

    def invia_pdf(self):
        if self.prenotazione.email:
            QMessageBox.information(self, 'Invio Pdf', f"Il file pdf della prenotazione a nome di {self.prenotazione.nome} {self.prenotazione.cognome} è stato correttamente inviato alla seguente email: {self.prenotazione.email}", QMessageBox.Ok)

