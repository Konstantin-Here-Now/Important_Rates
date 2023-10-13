import asyncio

from scripts import app_logger
from scripts.data_getters.get_cb_data import get_necessary_cb_curses, get_key_rate, get_latest_date, get_previous_date
from scripts.data_getters.get_moex_data import get_moex_usd, get_moex_eur
from scripts.singleton import Singleton

logger = app_logger.get_logger('rates_dataset')


class RatesDataset(metaclass=Singleton):
    def __init__(self):
        self.key_rate = "NO DATA"
        self.current_cb_usd = "NO DATA"
        self.current_cb_eur = "NO DATA"
        self.current_cb_cny = "NO DATE"
        self.previous_cb_usd = "NO DATA"
        self.previous_cb_eur = "NO DAYA"
        self.previous_cb_cny = "NO DATA"
        self.moex_usd = "NO DATA"
        self.moex_eur = "NO DATA"
        self.latest_date = "NO DATA"
        self.previous_date = "NO DATA"

        asyncio.run(self.update())

    async def update(self) -> None:
        try:
            coroutine_0 = self._get_cb_data_key_rate()
            coroutine_1 = self._get_cb_data_curses()
            coroutine_2 = self._get_moex_usd()
            coroutine_3 = self._get_moex_eur()
            coroutine_4 = self._get_dates()

            await asyncio.gather(coroutine_0, coroutine_1, coroutine_2, coroutine_3, coroutine_4)

        except Exception as ex:
            logger.error(ex)
            self.__init__()

    async def _get_cb_data_key_rate(self):
        self.key_rate = get_key_rate() + '' + '%'

    async def _get_cb_data_curses(self):
        cb_curses = get_necessary_cb_curses()
        self.current_cb_usd = cb_curses["current"][0] + ' ' + '₽'
        self.current_cb_eur = cb_curses["current"][1] + ' ' + '₽'
        self.current_cb_cny = cb_curses["current"][2] + ' ' + '₽'
        self.previous_cb_usd = cb_curses["previous"][0] + ' ' + '₽'
        self.previous_cb_eur = cb_curses["previous"][1] + ' ' + '₽'
        self.previous_cb_cny = cb_curses["previous"][2] + ' ' + '₽'

    async def _get_moex_usd(self):
        self.moex_usd = get_moex_usd() + ' ' + '₽'

    async def _get_moex_eur(self):
        self.moex_eur = get_moex_eur() + ' ' + '₽'

    async def _get_dates(self):
        self.latest_date = get_latest_date()
        self.previous_date = get_previous_date(self.latest_date)

    def get_ui_packed_data(self) -> dict[str, str]:
        ui_data = {
            'key_rate': self.key_rate,
            'previous_date': self.previous_date,
            'latest_date': self.latest_date,
            'previous_cb_usd': self.previous_cb_usd,
            'current_cb_usd': self.current_cb_usd,
            'previous_cb_eur': self.previous_cb_eur,
            'current_cb_eur': self.current_cb_eur,
            'previous_cb_cny': self.previous_cb_cny,
            'current_cb_cny': self.current_cb_cny,
            'moex_usd': self.moex_usd,
            'moex_eur': self.moex_eur
        }

        return ui_data
