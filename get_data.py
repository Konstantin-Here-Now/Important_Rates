import requests
from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient


def soup_find_and_get_text(soup: BeautifulSoup, div_class: str, position: int):
    # instead of repeating lines like soup.find_all("div", {'class': "main-indicator_value"})[2].text.rstrip()
    return soup.find_all("div", {'class': div_class})[position].text.rstrip()


def get_moex_data(data):
    # Define URL with a dynamic web content
    usd_url = "https://www.moex.com/ru/issue/USD000UTSTOM/CETS"
    eur_url = "https://www.moex.com/ru/issue/EUR_RUB__TOM/CETS"
    # Create a ScrapingAntClient instance
    client = ScrapingAntClient(token='efc9f455d10c40c79cd922533a11ce9e')
    # Get the HTML page rendered content
    usd_page_content = client.general_request(usd_url).content
    eur_page_content = client.general_request(eur_url).content
    # Parse content with BeautifulSoup
    usd_soup = BeautifulSoup(usd_page_content, features="lxml")
    eur_soup = BeautifulSoup(eur_page_content, features="lxml")
    moex_usd = usd_soup.find("li", {"class": "last", "title": "Курс последней сделки"}).text
    moex_eur = eur_soup.find("li", {"class": "last", "title": "Курс последней сделки"}).text
    data['moex_usd'] = moex_usd
    data['moex_eur'] = moex_eur
    return data


def get_cb_data(data: dict):
    cb_url = 'https://cbr.ru'
    request = requests.get(cb_url)
    cb_soup = BeautifulSoup(request.text, 'html.parser')
    for key in data.keys():
        data[key] = soup_find_and_get_text(cb_soup, *data[key])
    return data


def main():
    # creating dict, which once contains keys and sources, then received values instead sources
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

    data = get_cb_data(data)
    data = get_moex_data(data)

    return data
