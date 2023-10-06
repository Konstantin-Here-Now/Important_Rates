from scripts.rates_dataset import RatesDataset
from scripts.ui import get_ui


def console_main():
    dataset = RatesDataset()
    for key, value in dataset.__dict__.items():
        print(f"{key} : {value}")

    get_ui(dataset.get_ui_packed_data())


if __name__ == "__main__":
    console_main()
