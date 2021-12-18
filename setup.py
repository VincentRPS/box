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
import re

from setuptools import find_packages, setup

with open("src/box/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="box",
    version=version,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    project_utls={
        # "Documentation": "https://box.rtfd.io",
        "Issue Tracker": "https://github.com/VincentRPS/box/issues",
        "Pull Request Tracker": "https://github.com/VincentRPS/box/pulls",
    },
    url="https://github.com/VincentRPS/box",
    license="GNU Affero GPL",
    author="VincentRPS",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=requirements,
    description="Pythonic API Wrapper For Discord And Anime Enjoyers",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: AsyncIO",
        "Framework :: aiohttp",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
