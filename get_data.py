import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver


def soup_find_and_get_text(soup: BeautifulSoup, div_class: str, position: int):
    # instead of repeating lines like soup.find_all("div", {'class': "main-indicator_value"})[2].text.rstrip()
    return soup.find_all("div", {'class': div_class})[position].text.rstrip()


def get_moex_data(data):
    # Define URL with a dynamic web content
    usd_url = "https://www.moex.com/ru/issue/USD000UTSTOM/CETS"
    eur_url = "https://www.moex.com/ru/issue/EUR_RUB__TOM/CETS"

    # Setting web driver and making it invisible (no window)
    driver = webdriver.Firefox()
    options = webdriver.FirefoxOptions()
    options.headless = True

    # Getting data (and accepting cookies)
    driver.get(usd_url)
    driver.find_element(By.LINK_TEXT, 'Согласен').click()
    moex_usd = driver.find_element(By.CLASS_NAME, 'last').text
    driver.delete_all_cookies()
    driver.get(eur_url)
    driver.find_element(By.LINK_TEXT, 'Согласен').click()
    moex_eur = driver.find_element(By.CLASS_NAME, 'last').text
    driver.quit()

    data['moex_usd'] = moex_usd
    data['moex_eur'] = moex_eur
    return data


def get_cb_data():
    data = dict(
        {
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
    )
    cb_url = 'https://cbr.ru'
    request = requests.get(cb_url)
    cb_soup = BeautifulSoup(request.text, 'html.parser')
    for key in data.keys():
        data[key] = soup_find_and_get_text(cb_soup, *data[key])
    return data


def main():
    # creating dict, which once contains keys and sources, then received values instead sources

    data = get_cb_data()
    data = get_moex_data(data)

    return data
