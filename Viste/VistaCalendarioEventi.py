from datetime import datetime
import calendar
import os
import pickle


from PyQt5.QtCore import Qt, QDate, QStringListModel
from PyQt5.QtGui import QFont, QIcon, QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QSizePolicy, \
    QHBoxLayout, QCalendarWidget, QListView

from Evento.Evento import Evento
from Viste.VistaInserisciEvento import VistaInserisciEvento
from Viste.VistaVisualizzaEvento import VistaVisualizzaEvento
from Viste.VistaModificaEvento import VistaModificaEvento
from Viste.VistaPrenotazioniEvento import VistaPrenotazioniEvento
from Gestione.GestoreEventi import GestoreEventi

class VistaCalendarioEventi(QWidget):
    def __init__(self, parent = None):
        super(VistaCalendarioEventi, self).__init__(parent)
        self.controller = GestoreEventi()
        self.evento_modificato = None

        font = QFont('Arial Nova Light', 15)

        self.calendario_eventi = self.init_calendario()
        v_layout_eventi = QVBoxLayout()
        self.list_view_eventi = QListView()
        self.update_ui()

        grid_layout = QGridLayout()
        calendar_layout = QVBoxLayout()
        calendar_layout.addWidget(self.calendario_eventi)

        label = QLabel("Lista Eventi:")
        font.setItalic(True)
        label.setFont(font)
        v_layout_eventi.addWidget(label)
        v_layout_eventi.addWidget(self.list_view_eventi)

        self.calendario_eventi.selectionChanged.connect(self.data_selezionata)
        self.label = QLabel('')
        calendar_layout.addWidget(self.label)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.get_generic_button("Inserisci Evento", self.show_vista_inserisci_evento))
        buttons_layout.addWidget(self.get_generic_button("Visualizza Evento", self.show_vista_visualizza_evento))

        grid_layout.addLayout(v_layout_eventi, 0, 1)
        grid_layout.addLayout(calendar_layout, 0, 0)
        grid_layout.addLayout(buttons_layout, 1, 1, alignment=Qt.AlignBottom)

        self.setLayout(grid_layout)
        self.setFont(QFont('Arial Nova Light'))
        self.setWindowTitle("Gestore Eventi")
        self.setWindowIcon(QIcon('Dati/DigitalDisco.png'))

        self.setMaximumSize(1000, 650)
        self.resize(910, 650)
        self.move(0, 0)

    # Funzione che inizializza il calendario dell'interfaccia grafica.
    def init_calendario(self):
        calendario = QCalendarWidget(self)
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
       #currentDay = datetime.now().day

        calendario.setMinimumDate(QDate(currentYear, currentMonth, 1))
        calendario.setMaximumDate(
            QDate(currentYear + 1, currentMonth, calendar.monthrange(currentYear, currentMonth)[1]))
        calendario.setSelectedDate(QDate(currentYear, currentMonth, 1))

        calendario.setFont(QFont('Arial Nova Light', 18))
        calendario.setStyleSheet('background-color: #4A4A4A;')

        calendario.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        calendario.setGeometry(200, 200, 300, 200)
        calendario.setGridVisible(True)
        return calendario

    # Funzione che viene richiamata per creare un bottone.
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setFont(QFont('Arial Nova Light', 15))
        button.clicked.connect(on_click)
        return button

    # Funzione che mostra la vista per l'inserimento dei dati, da parte dell'utente, per creare un nuovo evento.
    def show_vista_inserisci_evento(self):
        self.vista_inserisci_evento = VistaInserisciEvento(callback=self.update_ui)
        self.vista_inserisci_evento.show()

    # Funzione che restituisce la data selezionata.
    def data_selezionata(self):
        dataselezionata = self.calendario_eventi.selectedDate()
        data_selezionata = str(dataselezionata.toPyDate())
        self.setFont(QFont('Arial Nova Light', 12))
        self.label.setText("Data selezionata : " + data_selezionata)
        return data_selezionata

    def load_eventi(self):
        if os.path.isfile('Dati/lista_eventi.pickle'):
            with open('Dati/lista_eventi.pickle', 'rb') as f:
                self.controller.lista_eventi = pickle.load(f)

    # Funzione che popola le liste degli eventi
    def update_ui(self):
        self.load_eventi()
        list_view_model = QStandardItemModel(self.list_view_eventi)
        for eventi in self.controller.lista_eventi:
            item = QStandardItem()
            nome = f"{eventi.nome}"  # il type ci restituisce il nome della classe
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            list_view_model.appendRow(item)

        self.list_view_eventi.setModel(list_view_model)

    def show_vista_visualizza_evento(self):
        if self.list_view_eventi.selectedIndexes():
            indice_selezionato = self.list_view_eventi.selectedIndexes()[0].row()
            evento_selezionato = self.controller.get_evento_by_index_(indice_selezionato)

            self.vista_evento = VistaVisualizzaEvento(evento_selezionato, self.update_ui, self.elimina_evento, self.show_vista_modifica_evento, self.show_vista_prenotazioni_evento)
            self.vista_evento.show()

    def show_vista_modifica_evento(self):
        if self.list_view_eventi.selectedIndexes():
            indice_selezionato = self.list_view_eventi.selectedIndexes()[0].row()
            evento_selezionato = self.controller.get_evento_by_index_(indice_selezionato)

            self.vista_modifica_evento = VistaModificaEvento(evento_selezionato, self.controller.aggiorna_evento, self.vista_evento.update_ui_evento)
            self.vista_modifica_evento.show()
            self.vista_evento.close()

    def show_vista_prenotazioni_evento(self):
        if self.list_view_eventi.selectedIndexes():
            indice_selezionato = self.list_view_eventi.selectedIndexes()[0].row()
            evento_selezionato = self.controller.get_evento_by_index_(indice_selezionato)

            self.vista_prenotazioni = VistaPrenotazioniEvento(evento_selezionato)
            self.vista_prenotazioni.show()


    def elimina_evento(self):

        if self.list_view_eventi.selectedIndexes():
            selected_index = self.list_view_eventi.selectedIndexes()[0]
            row = selected_index.row()
            evento_selezionato = self.controller.lista_eventi[row]

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Sei sicuro di voler eliminare l'evento?")
            msg.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
            msg.setInformativeText("La decisione è irreversibile!")
            msg.setDetailedText("N.B. Verrà eliminata ogni informazione relativa all'evento.")
            msg.setWindowTitle("Conferma eliminazione")
            msg.setWindowIcon(QIcon('Dati/DigitalDisco.png'))
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)


            if msg.exec() == QMessageBox.Ok: #La funzione exec() blocca l'esecuzione del codice fino a quando l'utente non chiude la finestra di dialogo. Quando l'utente interagisce con la finestra di dialogo e preme un pulsante, exec() restituisce il valore corrispondente al pulsante premuto.

                self.controller.rimuovi_evento(evento_selezionato)
                self.update_ui()

                msg.close()
