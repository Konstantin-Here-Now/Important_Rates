import logging
import os
from datetime import date

from settings import BASE_DIR


def get_logger(name):
    _log_format = f"[%(asctime)s] - [%(levelname)s] - %(name)s : %(message)s"

    if not os.path.isdir(BASE_DIR + "/logs"):
        os.mkdir(BASE_DIR + "/logs")

    filename = f"{BASE_DIR}/logs/{date.today()}.log"
    with open(filename, "a"):
        pass
    logger = logging.getLogger(name)
    logging.basicConfig(level=logging.INFO, filename=filename,
                        format=_log_format)
    return logger
