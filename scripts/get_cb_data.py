from datetime import date, timedelta

from get_beautiful_soup import get_soup
from scripts.get_beautiful_soup import HttpMethod


def get_key_rate() -> str:
    url = "https://cbr.ru/DailyInfoWebServ/DailyInfo.asmx?op=GetCursOnDate"
    body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <KeyRateXML xmlns="http://web.cbr.ru/">
          <fromDate>{(date.today() - timedelta(days=1)).isoformat()}</fromDate>
          <ToDate>{date.today().isoformat()}</ToDate>
        </KeyRateXML>
      </soap12:Body>
    </soap12:Envelope>"""
    headers = {'content-type': 'application/soap+xml',
               'content-length': str(len(body))}

    soup = get_soup(url, HttpMethod.POST, headers=headers, body=body, parser="xml")
    key_rate = soup.find_all("Rate")[-1].text

    return key_rate


def get_curses() -> dict[str, dict[str, str]]:
    output_dict = {}

    url = "https://cbr.ru/DailyInfoWebServ/DailyInfo.asmx?op=GetCursOnDate"
    body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <GetCursOnDate xmlns="http://web.cbr.ru/">
          <On_date>{date.today().isoformat()}</On_date>
        </GetCursOnDate>
      </soap12:Body>
    </soap12:Envelope>"""
    headers = {'content-type': 'application/soap+xml',
               'content-length': str(len(body))}

    soup = get_soup(url, HttpMethod.POST, headers=headers, body=body, parser="xml")

    for elem in soup.find_all("ValuteCursOnDate"):
        output_dict[elem.find("Vname").text.strip()] = {
            "Vnom": elem.find("Vnom").text,
            "Vcurs": elem.find("Vcurs").text,
            "Vcode": elem.find("Vcode").text,
            "VchCode": elem.find("VchCode").text,
            "VunitRate": elem.find("VunitRate").text
        }

    return output_dict


def get_cb_usd() -> str:
    curses = get_curses()
    cb_usd = curses["Доллар США"]["Vcurs"]
    return cb_usd


def get_cb_eur() -> str:
    curses = get_curses()
    cb_eur = curses["Евро"]["Vcurs"]
    return cb_eur
