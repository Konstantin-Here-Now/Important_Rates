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
        for key in data.keys():
            exec(f'self.{key}.setText(data["{key}"])')

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
