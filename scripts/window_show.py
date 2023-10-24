from rates_dataset import RatesDataset
from ui import get_ui


def show_window(dataset: RatesDataset = RatesDataset()):
    get_ui(dataset.get_ui_packed_data())


if __name__ == "__main__":
    show_window()
