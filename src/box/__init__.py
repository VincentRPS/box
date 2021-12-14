"""
box
~~~
Pincer extension adding extra features.

:copyright: 2021 VincentRPS
:license: GNU Affero
"""

__title__ = 'box'
__author__ = 'VincentRPS'
__license__ = 'GNU Affero'
__copyright__ = 'Copyright 2021 VincentRPS'
__version__ = '2021.x.x' # TODO: Specify release at some point

import logging
from typing import NamedTuple, Literal

from . import *

logging.getLogger(__name__).addHandler(logging.NullHandler())
