from sys import argv

from PyQt6 import QtWidgets

from assets import cb_ui
from get_data import RatesDataObj


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

    def update_moex_data(self):
        RatesDataObj.get_moex_data()
        data = RatesDataObj.data_dict
        self.moex_usd.setText(data['moex_usd'])
        self.moex_eur.setText(data['moex_eur'])


def main(data):
    app = QtWidgets.QApplication(argv)  # argv = sys.argv
    window = App()
    window.set_values(data)  # setting got DATA
    window.moex_update_btn.clicked.connect(window.update_moex_data)  # connecting button to function
    window.show()
    app.exec()
