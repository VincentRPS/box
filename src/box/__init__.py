"""
box
~~~
Pincer extension adding extra features.

:copyright: 2021 VincentRPS
:license: GNU Affero
"""

__title__ = "box"
__author__ = "VincentRPS"
__license__ = "GNU Affero"
__copyright__ = "Copyright 2021 VincentRPS"
__version__ = "2021.12.18"

import logging

from .bot import *

logging.getLogger(__name__).addHandler(logging.NullHandler())
