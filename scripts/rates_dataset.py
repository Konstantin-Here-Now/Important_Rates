from scripts.data_getters.get_cb_data import get_necessary_cb_curses, get_key_rate, get_latest_date, get_previous_date
from scripts.data_getters.get_moex_data import get_moex_usd, get_moex_eur
from scripts.singleton import Singleton


class RatesDataset(metaclass=Singleton):
    def __init__(self):
        self.key_rate = ""
        self.current_cb_usd = ""
        self.current_cb_eur = ""
        self.previous_cb_usd = ""
        self.previous_cb_eur = ""
        self.moex_usd = ""
        self.moex_eur = ""
        self.latest_date = ""
        self.previous_date = ""
        self.update()

    def update(self):
        cb_curses = get_necessary_cb_curses()
        self.key_rate = get_key_rate()
        self.current_cb_usd = cb_curses["current"][0]
        self.current_cb_eur = cb_curses["current"][1]
        self.previous_cb_usd = cb_curses["previous"][0]
        self.previous_cb_eur = cb_curses["previous"][1]
        self.moex_usd = get_moex_usd()
        self.moex_eur = get_moex_eur()
        self.latest_date = get_latest_date()
        self.previous_date = get_previous_date(self.latest_date)

    def get_ui_packed_data(self):

        ui_data = {
            'main_rate': self.key_rate,
            'previous_date': self.previous_date,
            'current_date': self.latest_date,
            'previous_usd': self.previous_cb_usd,
            'current_usd': self.current_cb_usd,
            'previous_eur': self.previous_cb_eur,
            'current_eur': self.current_cb_eur,
            'previous_cny': "---",
            'current_cny': "---",
            'moex_usd': self.moex_usd,
            'moex_eur': self.moex_eur
        }
        return ui_data
