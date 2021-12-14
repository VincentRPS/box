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
__version__ = '0.1'

import logging
from typing import NamedTuple, Literal

from . import *

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=2, minor=0, micro=0, releaselevel='alpha', serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())
