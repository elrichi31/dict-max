#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parser module - Word and number processing utilities
"""

from typing import List


def procesar_palabra(palabra: str) -> List[str]:
    """Procesa una palabra generando variaciones sin espacios"""
    variaciones = [palabra]
    
    # Si tiene espacios, generar variaciones
    if ' ' in palabra:
        # Sin espacios (junto)
        variaciones.append(palabra.replace(' ', ''))
        # Con guión
        variaciones.append(palabra.replace(' ', '-'))
        # Con guión bajo
        variaciones.append(palabra.replace(' ', '_'))
        # Con punto
        variaciones.append(palabra.replace(' ', '.'))
        # Capitalizado sin espacios
        variaciones.append(''.join(word.capitalize() for word in palabra.split()))
        # Solo primera letra de cada palabra
        variaciones.append(''.join(word[0] for word in palabra.split() if word))
        # Solo primera letra mayúsculas
        variaciones.append(''.join(word[0].upper() for word in palabra.split() if word))
    
    return list(set(variaciones))


def extraer_partes_numeros(numero) -> List[str]:
    """Extrae partes relevantes de números largos (cédulas, teléfonos)"""
    numero_str = str(numero)
    partes = [numero_str]  # Número completo
    
    # Si el número es muy largo (cédula, teléfono - más de 8 dígitos)
    if len(numero_str) >= 8:
        # Extraer fragmentos de TODAS las longitudes (4, 5, 6, 7, 8) con ventana deslizante
        for longitud in [4, 5, 6, 7, 8]:
            if len(numero_str) >= longitud:
                for i in range(len(numero_str) - longitud + 1):
                    partes.append(numero_str[i:i+longitud])
        
        # También incluir primeros y últimos dígitos de varias longitudes
        for longitud in [4, 5, 6, 7, 8]:
            if len(numero_str) >= longitud:
                partes.append(numero_str[:longitud])   # Primeros N
                partes.append(numero_str[-longitud:])  # Últimos N
    
    # Si el número tiene longitud media (6-7 dígitos)
    elif len(numero_str) >= 6:
        # Fragmentos de 4 y 5 dígitos
        for longitud in [4, 5]:
            if len(numero_str) >= longitud:
                for i in range(len(numero_str) - longitud + 1):
                    partes.append(numero_str[i:i+longitud])
    
    # Filtrar solo números de longitud razonable para contraseñas (4-10 dígitos)
    partes_filtradas = [p for p in partes if 4 <= len(p) <= 10]
    
    return list(set(partes_filtradas))
