from dataset import Dataset

from scripts.get_cb_data import get_key_rate, get_cb_usd, get_cb_eur
from scripts.get_moex_data import get_moex_usd, get_moex_eur

if __name__ == "__main__":
    dataset = Dataset(
        key_rate=get_key_rate(),
        cb_usd=get_cb_usd(),
        cb_eur=get_cb_eur(),
        moex_usd=get_moex_usd(),
        moex_eur=get_moex_eur()
    )

    print(dataset.__dict__)
