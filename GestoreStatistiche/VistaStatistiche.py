from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QComboBox, QWidget
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtCore import Qt
from GestoreStatistiche.GestoreStatistiche import GestoreStatistiche


class VistaStatistiche(QWidget):
    def __init__(self):
        super().__init__()
        self.gestore_statistiche = GestoreStatistiche()


        self.setWindowTitle("Statistiche")
        self.resize(700, 500)

        self.combo_box = QComboBox()
        self.combo_box.currentIndexChanged.connect(self.update_chart)

        self.chart = QChart()
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignRight)

        self.chart_view = QChartView(self.chart)

        layout = QVBoxLayout(self)
        layout.addWidget(self.combo_box)
        layout.addWidget(self.chart_view)

        self.populate_combo_box()
        self.update_chart()

    def populate_combo_box(self):
        for month in range(1, 13):
            self.combo_box.addItem(self.get_month_name(month), month)

    def get_month_name(self, month):
        # Replace this with your own implementation to get the month name
        month_names = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]
        return month_names[month - 1]

    def update_chart(self):
        #selected_month = self.combo_box.currentText()
        selected_month_number = self.combo_box.currentIndex() + 1

        series = QPieSeries()
        for month in range(1, 13):
            month_name = self.get_month_name(month)
            incassi = self.gestore_statistiche.calcola_incassi_mensili_biglietti(month)
            if month == selected_month_number:
                series.append(f"{month_name} (Selected)", incassi)
            else:
                series.append(month_name, 0)

        self.chart.removeAllSeries()
        self.chart.addSeries(series)
        self.chart.setTitle("Incassi Biglietti per Mese")

        self.chart_view.setChart(self.chart)
        self.chart_view.repaint()