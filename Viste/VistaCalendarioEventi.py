from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QSizePolicy, \
    QHBoxLayout
from pyqt5_plugins.examplebuttonplugin import QtGui



class VistaCalendarioEventi(QWidget):
    def __init__(self, parent = None):
        super(VistaCalendarioEventi, self).__init__(parent)

