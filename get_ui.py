from PyQt6 import QtWidgets
from assets import cb_ui
import sys


class App(QtWidgets.QMainWindow, cb_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def set_values(self, data: dict):
        """
        Not a static method.
        :param data: dict
        :return: None
        """
        ruble_symbol = '₽'
        for key in data.keys():
            exec(f'self.{key}.setText(data["{key}"])')


def main(data):
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.set_values(data)  # setting got DATA
    window.show()
    app.exec()
