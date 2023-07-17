from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QComboBox, QWidget
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtCore import Qt
from GestoreStatistiche.GestoreStatistiche import GestoreStatistiche

class VistaStatistiche(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ticket Revenue")
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

        self.gestore_statistiche = GestoreStatistiche()

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
        selected_month = self.combo_box.currentData()

        series = QPieSeries()
        for month in range(1, 13):
            month_name = self.get_month_name(month)
            revenue = self.gestore_statistiche.calcola_incassi_mensili_biglietti(month)
            if month == selected_month:
                series.append(f"{month_name} (Selected)", revenue)
            else:
                series.append(month_name, revenue)

        self.chart.removeAllSeries()
        self.chart.addSeries(series)
        self.chart.setTitle("Ticket Revenue by Month")

        self.chart_view.repaint()