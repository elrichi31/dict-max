#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Patterns module - Password pattern generation and variations
"""

from typing import List


def generar_variaciones(palabra: str) -> List[str]:
    """Genera variaciones de una palabra"""
    variaciones = [
        palabra,
        palabra.lower(),
        palabra.upper(),
        palabra.capitalize(),
        palabra[::-1],
    ]
    
    # Leetspeak
    leet_map = {
        'a': ['@', '4'], 'e': ['3'], 'i': ['1', '!'], 
        'o': ['0'], 's': ['5', '$'], 't': ['7'], 
        'g': ['9'], 'b': ['8'], 'l': ['1']
    }
    
    palabra_leet = palabra.lower()
    for char, replacements in leet_map.items():
        if char in palabra_leet:
            palabra_leet = palabra_leet.replace(char, replacements[0])
    
    if palabra_leet != palabra.lower():
        variaciones.append(palabra_leet)
    
    return list(set(variaciones))
