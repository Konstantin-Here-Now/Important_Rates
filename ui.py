from sys import argv

from PyQt6 import QtWidgets

import app_logger
from assets import cb_ui
from dataset import RatesDataset

logger = app_logger.get_logger(' ui ')


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
        logger.info('Setting data...')
        for key in data.keys():
            exec(f'self.{key}.setText(data["{key}"])')
        logger.info('Data set.')

    def update_moex_data(self):
        logger.info('Updating MOEX data...')
        RatesDataset.get_moex_data()
        data = RatesDataset.data_dict
        self.moex_usd.setText(data['moex_usd'])
        self.moex_eur.setText(data['moex_eur'])
        logger.info('Updated MOEX data.')


def get_ui(data):
    logger.info('Showing window...')
    app = QtWidgets.QApplication(argv)  # argv = sys.argv
    window = App()
    window.set_values(data)  # setting got DATA
    window.moex_update_btn.clicked.connect(window.update_moex_data)  # connecting button to function
    window.show()
    logger.info('Window shown.')
    app.exec()
