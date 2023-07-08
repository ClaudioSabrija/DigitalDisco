from datetime import date
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QComboBox,  QMessageBox

from Gestione.GestorePrenotazioni import GestorePrenotazioni
from Evento.Evento import Evento
from Attività.Prenotazione import Prenotazione

class VistaInserisciPrenotazione(QWidget):
    def __init__(self, evento_selezionato, callback_vista, callback, parent=None):
        super(VistaInserisciPrenotazione, self).__init__(parent)
        self.evento = evento_selezionato
        self.callback = callback
        self.callback_vista = callback_vista
        self.prenotazione = GestorePrenotazioni()

        # Creazione dei widget
        self.label_top = QLabel("Inserisci i dati del cliente:", self)
        self.label_nome = QLabel("NOME:", self)
        self.label_cognome = QLabel("COGNOME:", self)
        self.label_data_di_nascita = QLabel("DATA DI NASCITA:", self)
        self.label_codice_fiscale = QLabel("CODICE FISCALE:", self)
        self.label_servizio = QLabel("SERVIZIO:", self)
        self.label_note = QLabel("PARTECIPANTI:", self)

        self.line_edit_nome = QLineEdit(self)
        self.line_edit_cognome = QLineEdit(self)
        self.line_edit_data_di_nascita = QLineEdit(self)
        self.line_edit_codice_fiscale = QLineEdit(self)
        self.combo_box_servizio = QComboBox(self)
        self.line_edit_note = QLineEdit(self)

        button_conferma = QPushButton("Conferma", self)
        button_conferma.clicked.connect(self.add_prenotazione)

        self.combo_box_servizio.addItem(f'{self.evento.servizi["Ingresso"].get_nome_servizio()}')
        self.combo_box_servizio.addItem(f'{self.evento.servizi["Tavolo"].get_nome_servizio()}')
        self.combo_box_servizio.addItem(f'{self.evento.servizi["Prive"].get_nome_servizio()}')

        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
        self.setWindowTitle('Inserisci Prenotazione')
        self.setFixedSize(400, 600)  # Imposta la dimensione fissa della finestra di dialogo
        self.label_top.setFixedSize(300, 30)  # Imposta la dimensione fissa della label superiore


        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label_top)
        layout.addWidget(self.label_nome)
        layout.addWidget(self.line_edit_nome)
        layout.addWidget(self.label_cognome)
        layout.addWidget(self.line_edit_cognome)
        layout.addWidget(self.label_data_di_nascita)
        layout.addWidget(self.line_edit_data_di_nascita)
        layout.addWidget(self.label_codice_fiscale)
        layout.addWidget(self.line_edit_codice_fiscale)
        layout.addWidget(self.label_servizio)
        layout.addWidget(self.combo_box_servizio)
        layout.addWidget(self.label_note)
        layout.addWidget(self.line_edit_note)
        layout.addWidget(button_conferma)
        self.setLayout(layout)


    def add_prenotazione(self):
        # Ottenere i valori inseriti dall'utente
        nome = self.line_edit_nome.text().strip()
        cognome = self.line_edit_cognome.text().strip()
        data_di_nascita = self.line_edit_data_di_nascita.text().strip()
        codice_fiscale = self.line_edit_codice_fiscale.text().strip()
        servizio = self.combo_box_servizio.currentText()
        note = self.line_edit_note.text().strip()

        # Controllo dei campi compilati
        if not nome or not cognome or not data_di_nascita or not codice_fiscale:
            QMessageBox.warning(self, "Errore", "Tutti i campi devono essere compilati.")
            return

        try:
            giorno, mese, anno = data_di_nascita.split('/')
            data_inserita = QDate(int(anno), int(mese), int(giorno))  # invertito l'ordine dei parametri per QDate
            if not data_inserita.isValid():
                raise ValueError()

            # Converto la data dell'evento in un oggetto datetime.date
            data_evento_str = self.evento.data
            giorno_evento, mese_evento, anno_evento = map(int, data_evento_str.split('/')) #data_evento_str.split('/') divide la stringa data_evento_str in una lista
                                                                                            # di sottostringhe separate dal carattere '/'
                                                                                            #mentre La funzione map(int, ...) applica la funzione int() a ciascun elemento della lista.
                                                                                            #Ciò significa che ogni elemento della lista viene convertito in un intero
            data_evento = date(anno_evento, mese_evento, giorno_evento)

            # Calcolo dell'età dell'utente rispetto alla data dell'evento
            eta_minima = data_evento.year - 18
            data_18_anni_fa = date(eta_minima, data_evento.month, data_evento.day)

            if data_inserita > data_18_anni_fa:
                QMessageBox.critical(self, "Errore", "Per effettuare la prenotazione il cliente deve avere almeno 18 anni alla data dell'evento.")
                return

        except ValueError:
            QMessageBox.critical(self, "Errore", "Il formato della data inserita deve essere: dd/mm/yyyy.")
            return

        prenotazione = Prenotazione(nome, cognome, data_di_nascita, codice_fiscale, servizio)
        prenotazione.note.append(note)
        self.prenotazione.inserisci_prenotazione(self.evento, prenotazione)
        self.callback(self.evento)
        self.callback_vista(self.evento)
        self.close()
