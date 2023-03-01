from PyQt6 import QtWidgets
from assets import cb_ui
import sys


class App(QtWidgets.QMainWindow, cb_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def set_values(self, data: dict):
        self.main_rate.setText(data['main_rate'])
        self.previous_date.setText(data['previous_date'])
        self.current_date.setText(data['current_date'])
        self.current_usd.setText(data['current_usd'])
        self.current_eur.setText(data['current_eur'])
        self.current_cny.setText(data['current_cny'])
        self.previous_usd.setText(data['previous_usd'])
        self.previous_eur.setText(data['previous_eur'])
        self.previous_cny.setText(data['previous_cny'])

    def set_styles(self):
        self.setStyleSheet(
            """
            font-size: 18px;
            """
        )


def main(data):
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.set_values(data)  # setting got DATA
    window.set_styles()  # setting general styles
    window.show()
    app.exec()
