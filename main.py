import sys
import time
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from Viste.VistaLogin import VistaLogin

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    vista_login = VistaLogin()
    vista_login.show()
    sys.exit(app.exec())


