from enum import Enum
from typing import Any, Sequence

import bs4
from aiohttp import ClientSession

from scripts import app_logger

logger = app_logger.get_logger('get_beautiful_soup')


class HttpMethod(Enum):
    GET = 'GET'
    POST = 'POST'


async def get_soup(url: str, http_method: HttpMethod, headers: Any = None, body: Any = None,
                   parser: str | Sequence[str] = 'html.parser') -> bs4.BeautifulSoup:
    logger.info(f"{http_method.value} {url}")
    async with ClientSession() as session:
        async with session.request(http_method.value, url, headers=headers, data=body) as response:
            soup = bs4.BeautifulSoup()
            try:
                soup = bs4.BeautifulSoup(await response.text(), parser)
            except ConnectionError as ex:
                logger.error(ex)
                soup = bs4.BeautifulSoup("<nodata>NoData</nodata>", "xml")
            finally:
                return soup
