from datetime import date, timedelta

from scripts.data_getters.get_beautiful_soup import get_soup, HttpMethod


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


def get_latest_date() -> str:
    url = "https://cbr.ru/DailyInfoWebServ/DailyInfo.asmx?op=GetLatestDate"
    body = """<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <GetLatestDate xmlns="http://web.cbr.ru/" />
      </soap12:Body>
    </soap12:Envelope>"""
    headers = {'content-type': 'application/soap+xml',
               'content-length': str(len(body))}

    soup = get_soup(url, HttpMethod.POST, headers=headers, body=body, parser="xml")
    year = soup.text[:4]
    month = soup.text[4:6]
    day = soup.text[6:]

    return f"{year}-{month}-{day}"


def get_previous_date(iso_date: str = get_latest_date()) -> str:
    previous_date = (date.fromisoformat(iso_date) - timedelta(days=1)).isoformat()
    return previous_date


def get_curs_on_date(iso_date: str = date.today().isoformat()) -> dict[str, dict[str, str]]:
    output_dict = {}

    url = "https://cbr.ru/DailyInfoWebServ/DailyInfo.asmx?op=GetCursOnDate"
    body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <GetCursOnDate xmlns="http://web.cbr.ru/">
          <On_date>{iso_date}</On_date>
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


# necessary_cb_curses are current_cb_usd, current_cb_eur, previous_cb_usd, previous_cb_eur
def get_necessary_cb_curses() -> dict[str, tuple[str, str]]:
    latest_date = get_latest_date()
    previous_date = get_previous_date(latest_date)
    current_curses = get_curs_on_date(latest_date)
    previous_curses = get_curs_on_date(previous_date)

    current_usd, current_eur = get_cb_usd(current_curses), get_cb_eur(current_curses)
    previous_usd, previous_eur = get_cb_usd(previous_curses), get_cb_eur(previous_curses)

    curses_dict = {
        "current": (current_usd, current_eur),
        "previous": (previous_usd, previous_eur)
    }

    return curses_dict


def get_cb_usd(curses: dict[str, dict[str, str]]) -> str:
    cb_usd = curses["Доллар США"]["Vcurs"]
    return cb_usd


def get_cb_eur(curses: dict[str, dict[str, str]]) -> str:
    cb_eur = curses["Евро"]["Vcurs"]
    return cb_eur
