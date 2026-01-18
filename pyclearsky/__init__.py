# -*- coding: utf-8 -*-

"""Top-level package for pyclearsky."""

__author__ = """Santosh Philip"""
__email__ = 'santosh@example.com'
# __version__ = '0.3.0'
# src/your_package/__init__.py
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pyclearsky")   # must match [project] name =
except PackageNotFoundError:
    __version__ = "0.0.0.dev0"                   # fallback for editable installs / dev
