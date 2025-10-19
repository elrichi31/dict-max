#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dict-Max - Professional Wordlist Generator
Advanced password dictionary generator for penetration testing
"""

__version__ = "1.3.0"
__author__ = "Nicolas"

from .core import DictMax
from .utils import Colors, print_banner

__all__ = ['DictMax', 'Colors', 'print_banner', '__version__', '__author__']
