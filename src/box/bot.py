"""
box - extra utilitys for pincer

Copyright (C) 2021 VincentRPS

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import logging
from typing import Optional
import pincer

_log = logging.getLogger(__name__)

class Bot(pincer.Client):
    """A Subclass of :class:`pincer.Client` adding extra features.
    
    .. versionadded:: 0.1.0
    """
    def __init__(self, prefix: Optional[None], prefix_only: bool = False):
        self.prefix_only = prefix_only
        self.prefix = prefix

    @callable
    async def command(self):
        """Makes a **PREFIXED** command."""
        pass

    @callable
    async def slash_command(self):
        if self.prefix_only == True:
            _log.fatal("Please use `Bot.command` instead for prefixed only commands.")