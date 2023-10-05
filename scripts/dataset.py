# from subprocess import CREATE_NO_WINDOW

from bs4 import BeautifulSoup
from requests import get as requests_get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import app_logger
from scripts.get_cb_data import get_key_rate
from scripts.singleton import Singleton

CB_URL = 'https://cbr.ru'
USD_URL = "https://www.moex.com/ru/issue/USD000UTSTOM/CETS"
EUR_URL = "https://www.moex.com/ru/issue/EUR_RUB__TOM/CETS"

logger = app_logger.get_logger('data')


class Dataset(metaclass=Singleton):
    def __init__(self, key_rate, cb_usd, cb_eur, moex_usd, moex_eur):
        self.key_rate = key_rate
        self.cb_usd = cb_usd
        self.cb_eur = cb_eur
        self.moex_usd = moex_usd
        self.moex_eur = moex_eur


class RatesData:
    def __init__(self):
        logger.info('App starts.')
        logger.info('Collecting all data...')
        self.data_dict = {
            # key : sources for function soup_find_and_get_text
            'main_rate': ("main-indicator_value", 2),
            'previous_date': ("col-md-2 col-xs-7 _right", 0),
            'current_date': ("col-md-2 col-xs-7 _right", 1),
            'previous_usd': ("col-md-2 col-xs-9 _right mono-num", 0),
            'current_usd': ("col-md-2 col-xs-9 _right mono-num", 1),
            'previous_eur': ("col-md-2 col-xs-9 _right mono-num", 2),
            'current_eur': ("col-md-2 col-xs-9 _right mono-num", 3),
            'previous_cny': ("col-md-2 col-xs-9 _right mono-num", 4),
            'current_cny': ("col-md-2 col-xs-9 _right mono-num", 5)
        }
        self.get_cb_data()

        self.driver = self.get_browser()
        self.get_moex_data()

    @staticmethod
    def soup_find_and_get_text(soup: BeautifulSoup, div_class: str, position: int):
        # instead of repeating lines like soup.find_all("div", {'class': "main-indicator_value"})[2].text.rstrip()
        return soup.find_all("div", {'class': div_class})[position].text.rstrip()

    def get_cb_data(self):
        logger.info('   Collecting Central bank data...')
        request = requests_get(CB_URL)
        cb_soup = BeautifulSoup(request.text, 'html.parser')
        for key in self.data_dict.keys():
            self.data_dict[key] = self.soup_find_and_get_text(cb_soup, *self.data_dict[key])
        logger.info('   Got Central bank data.')

    @staticmethod
    def get_browser():
        # Setting web driver and making it invisible (no window)
        try:
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service(executable_path='logs/geckodriver.exe', log_path='../logs/geckodriver.log')
            service.creation_flags = CREATE_NO_WINDOW
            driver = webdriver.Firefox(options=options, service=service)
            logger.info('      Firefox started.')
            driver.switch_to.default_content()
        except Exception as e:
            driver = 'NO DRIVER'
            logger.error('!!!!!No Firefox in System.')
            logger.error(e)
        return driver

    def get_moex_data(self):
        logger.info('   Collecting MOEX data...')

        ruble_symbol = '₽'
        moex_usd = 'NO DATA'
        moex_eur = 'NO DATA'

        # Getting data (and accepting cookies)
        try:
            waiting = WebDriverWait(driver=self.driver, timeout=5)

            self.driver.get(USD_URL)
            waiting.until(EC.presence_of_element_located((By.LINK_TEXT, 'Согласен'))).click()
            moex_usd = waiting.until(EC.presence_of_element_located((By.CLASS_NAME, 'last'))).text
            logger.info('      Got MOEX-usd data.')
            self.driver.get(EUR_URL)
            moex_eur = waiting.until(EC.presence_of_element_located((By.CLASS_NAME, 'last'))).text
            logger.info('      Got MOEX-eur data.')
            self.driver.quit()
        except Exception as e:
            logger.error('!!!!!Something went wrong.')
            logger.error(e)
        finally:
            self.data_dict['moex_usd'] = moex_usd + ' ' + ruble_symbol
            self.data_dict['moex_eur'] = moex_eur + ' ' + ruble_symbol
            logger.info('   Got MOEX data.')


RatesDataset = RatesData()
