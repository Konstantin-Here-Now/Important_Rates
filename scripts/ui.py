from sys import argv

from PyQt6 import QtWidgets

from scripts import app_logger
from assets import cb_ui
from scripts.rates_dataset import RatesDataset

logger = app_logger.get_logger('ui')


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
        try:
            logger.info('Setting data...')
            for key in data.keys():
                exec(f'self.{key}.setText(data["{key}"])')
            logger.info('Data set.')
        except AttributeError as ex:
            logger.error("No attribute found!")
            logger.error(ex)
            self.key_rate.setText("Error! Check logs!")

    def update_data(self):
        logger.info('Updating data...')
        RatesDataset().update()
        data = RatesDataset().get_ui_packed_data()
        self.set_values(data)
        logger.info('Updated data.')


def get_ui(data):
    logger.info('Showing window...')
    app = QtWidgets.QApplication(argv)  # argv = sys.argv
    window = App()
    window.set_values(data)  # setting got DATA
    window.moex_update_btn.clicked.connect(window.update_data)  # connecting button to function
    window.show()
    logger.info('Window shown.')
    app.exec()
