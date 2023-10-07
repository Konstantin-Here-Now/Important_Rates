from enum import Enum
from typing import Any, Sequence

import bs4
import requests

from scripts import app_logger

logger = app_logger.get_logger('rates_dataset')


class HttpMethod(Enum):
    GET = requests.get
    POST = requests.post


def get_soup(url: str, http_method: HttpMethod, headers: Any = None, body: Any = None,
             parser: str | Sequence[str] = 'html.parser') -> bs4.BeautifulSoup:
    soup = bs4.BeautifulSoup()
    try:
        response: requests.Response = http_method(url, headers=headers, data=body)
        soup = bs4.BeautifulSoup(response.text, parser)
    except ConnectionError as ex:
        logger.error(ex)
        soup = bs4.BeautifulSoup("<nodata>NoData</nodata>", "xml")
    finally:
        return soup
