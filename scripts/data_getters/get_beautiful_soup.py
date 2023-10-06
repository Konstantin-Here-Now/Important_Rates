from enum import Enum
from typing import Any, Sequence

import bs4
import requests


class HttpMethod(Enum):
    GET = requests.get
    POST = requests.post


def get_soup(url: str, http_method: HttpMethod, headers: Any = None, body: Any = None,
             parser: str | Sequence[str] = 'html.parser') -> bs4.BeautifulSoup:
    response: requests.Response = http_method(url, headers=headers, data=body)
    soup = bs4.BeautifulSoup(response.text, parser)

    return soup
