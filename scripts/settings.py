import os
import sys
from pathlib import Path

import yaml

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
    PLATFORM = "Windows"
else:
    BASE_DIR = str(Path(__file__).resolve().parent.parent)
    with open(os.path.join(BASE_DIR, r'config.yaml'), 'r', encoding="utf-8") as data_f:
        CONFIG = yaml.load(data_f, yaml.BaseLoader)

    PLATFORM = CONFIG["platform"]

sys.path.append(BASE_DIR)
