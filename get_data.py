import requests
from bs4 import BeautifulSoup

URL = 'https://cbr.ru'
request = requests.get(URL)
soup = BeautifulSoup(request.text, 'html.parser')


def soup_find_and_get_text(div_class: str, position: int):
    # instead of repeating lines like soup.find_all("div", {'class': "main-indicator_value"})[2].text.rstrip()
    return soup.find_all("div", {'class': div_class})[position].text.rstrip()


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

    for key in data.keys():
        data[key] = soup_find_and_get_text(*data[key])

    return data
