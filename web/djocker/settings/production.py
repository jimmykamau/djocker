import os

from config.settings.base import *


DEBUG = os.getenv("DEBUG", default=False)
