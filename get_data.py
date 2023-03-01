import requests
from bs4 import BeautifulSoup

URL = 'https://cbr.ru'


def main():
    data = dict()
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, 'html.parser')

    data['main_rate'] = soup.find_all("div", {'class': "main-indicator_value"})[2].text.rstrip()
    data['previous_date'] = soup.find_all("div", {'class': "col-md-2 col-xs-7 _right"})[0].text
    data['current_date'] = soup.find_all("div", {'class': "col-md-2 col-xs-7 _right"})[1].text
    data['previous_usd'] = soup.find_all("div", {'class': "col-md-2 col-xs-9 _right mono-num"})[0].text.rstrip()
    data['current_usd'] = soup.find_all("div", {'class': "col-md-2 col-xs-9 _right mono-num"})[1].text.rstrip()
    data['previous_eur'] = soup.find_all("div", {'class': "col-md-2 col-xs-9 _right mono-num"})[2].text.rstrip()
    data['current_eur'] = soup.find_all("div", {'class': "col-md-2 col-xs-9 _right mono-num"})[3].text.rstrip()
    data['previous_cny'] = soup.find_all("div", {'class': "col-md-2 col-xs-9 _right mono-num"})[4].text.rstrip()
    data['current_cny'] = soup.find_all("div", {'class': "col-md-2 col-xs-9 _right mono-num"})[5].text.rstrip()

    return data
