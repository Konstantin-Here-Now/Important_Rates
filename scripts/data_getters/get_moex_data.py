from .get_beautiful_soup import get_soup, HttpMethod


async def get_moex_usd() -> str:
    url = "http://iss.moex.com/iss/engines/currency/markets/selt/securities.xml?securities=USD000UTSTOM"
    soup = await get_soup(url, HttpMethod.GET, parser="xml")
    moex_usd = soup.find_all("rows")[1].find_all_next("row")[1]['LAST']

    return moex_usd


async def get_moex_eur() -> str:
    url = "http://iss.moex.com/iss/engines/currency/markets/selt/securities.xml?securities=EUR_RUB__TOM"
    soup = await get_soup(url, HttpMethod.GET, parser="xml")
    moex_eur = soup.find_all("rows")[1].find_all_next("row")[1]['LAST']

    return moex_eur
