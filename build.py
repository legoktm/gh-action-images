#!/usr/bin/env python3
"""
Copyright (C) 2020 Kunal Mehta <legoktm@debian.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from collections import defaultdict
from pathlib import Path
import subprocess
import sys

DOCKER = '/usr/bin/docker'
root = Path('images')


def image_name(image, tag):
    return f'legoktm/gh-action-{image}:{tag}'


def main():
    image, tag = sys.argv[1].split(':', 1)
    name = image_name(image, tag)
    print(f"Building {name}")
    subprocess.check_call([DOCKER, 'build', (root / image / tag).resolve(), f'--tag={name}'])
    if '--push' in sys.argv:
        subprocess.check_call([DOCKER, 'push', name])
        subprocess.check_call([DOCKER, 'rmi', name])


if __name__ == '__main__':
    main()
