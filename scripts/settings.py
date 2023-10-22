import os
from pathlib import Path

import yaml

BASE_DIR = Path(__file__).resolve().parent.parent

with open(os.path.join(BASE_DIR, r'config.yaml'), 'r', encoding="utf-8") as data_f:
    CONFIG = yaml.load(data_f, yaml.BaseLoader)

PLATFORM = CONFIG["platform"]
