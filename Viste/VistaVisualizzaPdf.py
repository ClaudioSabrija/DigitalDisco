from datetime import date
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QComboBox,  QMessageBox


from Gestione.GestorePrenotazioni import GestorePrenotazioni
from Evento.Evento import Evento
from Attività.Prenotazione import Prenotazione


class VistaVisualizzaPdf(QWidget):
    def __init__(self, prenotazione):
        super(VistaInserisciPrenotazione, self).__init__(parent)
        self.prenotazione = prenotazione