from scripts.rates_dataset import RatesDataset


def console_main():
    dataset = RatesDataset()
    for key, value in dataset.__dict__.items():
        print(f"{key} : {value}")


if __name__ == "__main__":
    console_main()
