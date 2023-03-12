from requests import get as requests_get
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver

CB_URL = 'https://cbr.ru'
USD_URL = "https://www.moex.com/ru/issue/USD000UTSTOM/CETS"
EUR_URL = "https://www.moex.com/ru/issue/EUR_RUB__TOM/CETS"


class RatesData:
    def __init__(self):
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
        self.get_moex_data()

    @staticmethod
    def soup_find_and_get_text(soup: BeautifulSoup, div_class: str, position: int):
        # instead of repeating lines like soup.find_all("div", {'class': "main-indicator_value"})[2].text.rstrip()
        return soup.find_all("div", {'class': div_class})[position].text.rstrip()

    def get_cb_data(self):
        request = requests_get(CB_URL)
        cb_soup = BeautifulSoup(request.text, 'html.parser')
        for key in self.data_dict.keys():
            self.data_dict[key] = self.soup_find_and_get_text(cb_soup, *self.data_dict[key])

    def get_moex_data(self):
        # Setting web driver and making it invisible (no window)
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.delete_all_cookies()

        # Getting data (and accepting cookies)
        driver.get(USD_URL)
        driver.find_element(By.LINK_TEXT, 'Согласен').click()
        moex_usd = driver.find_element(By.CLASS_NAME, 'last').text
        driver.delete_all_cookies()
        driver.get(EUR_URL)
        driver.find_element(By.LINK_TEXT, 'Согласен').click()
        moex_eur = driver.find_element(By.CLASS_NAME, 'last').text
        driver.delete_all_cookies()
        driver.quit()

        self.data_dict['moex_usd'] = moex_usd
        self.data_dict['moex_eur'] = moex_eur


RatesDataObj = RatesData()
