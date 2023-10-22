import logging
from datetime import date
import os

_log_format = f"[%(asctime)s] - %(name)s - [%(levelname)s] : %(message)s"


def get_logger(name):
    if not os.path.isdir("../logs"):
        os.mkdir("../logs")

    filename = f"../logs/{date.today()}.log"
    with open(filename, "a"):
        pass
    logger = logging.getLogger(name)
    logging.basicConfig(level=logging.INFO, filename=filename,
                        format=_log_format)
    return logger
