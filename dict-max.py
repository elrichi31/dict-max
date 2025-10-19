#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dict-Max - Professional Wordlist Generator
Advanced password dictionary generator for penetration testing
"""

import json
import os
import sys
import argparse
from datetime import datetime
from typing import List, Set

__version__ = "1.3.0"
__author__ = "Nicolas"

class Colors:
    """ANSI color codes"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def print_banner():
    """Imprime el banner de Dict-Max"""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
    ██████╗ ██╗ ██████╗████████╗      ███╗   ███╗ █████╗ ██╗  ██╗
    ██╔══██╗██║██╔════╝╚══██╔══╝      ████╗ ████║██╔══██╗╚██╗██╔╝
    ██║  ██║██║██║        ██║   █████╗██╔████╔██║███████║ ╚███╔╝ 
    ██║  ██║██║██║        ██║   ╚════╝██║╚██╔╝██║██╔══██║ ██╔██╗ 
    ██████╔╝██║╚██████╗   ██║         ██║ ╚═╝ ██║██║  ██║██╔╝ ██╗
    ╚═════╝ ╚═╝ ╚═════╝   ╚═╝         ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
{Colors.RESET}
{Colors.WHITE}    Professional Wordlist Generator for Penetration Testing{Colors.RESET}
{Colors.YELLOW}    Version: {__version__} | Author: {__author__}{Colors.RESET}
{Colors.RED}    ⚠️  For authorized security testing only{Colors.RESET}
{Colors.CYAN}    ═══════════════════════════════════════════════════════════════{Colors.RESET}
"""
    print(banner)

class DictMax:
    def __init__(self):
        self.informacion = {
            "nombres": [],
            "apellidos": [],
            "apodos": [],
            "fechas": [],
            "mascotas": [],
            "lugares": [],
            "empresas": [],
            "palabras_clave": [],
            "numeros_importantes": []
        }
        self.wordlist = set()
        self.verbose = False
        
    def log(self, message, level="info"):
        """Logger con colores"""
        if level == "info":
            print(f"{Colors.CYAN}[*]{Colors.RESET} {message}")
        elif level == "success":
            print(f"{Colors.GREEN}[+]{Colors.RESET} {message}")
        elif level == "error":
            print(f"{Colors.RED}[-]{Colors.RESET} {message}")
        elif level == "warning":
            print(f"{Colors.YELLOW}[!]{Colors.RESET} {message}")
        elif level == "verbose" and self.verbose:
            print(f"{Colors.WHITE}[~]{Colors.RESET} {message}")
    
    def procesar_palabra(self, palabra):
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
    
    def cargar_json(self, archivo):
        """Carga información desde un archivo JSON"""
        if not os.path.exists(archivo):
            self.log(f"El archivo '{archivo}' no existe", "error")
            return False
        
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            total = 0
            for key in self.informacion.keys():
                if key in datos and isinstance(datos[key], list):
                    for item in datos[key]:
                        # Procesar cada palabra para generar variaciones
                        variaciones = self.procesar_palabra(item)
                        self.informacion[key].extend(variaciones)
                        total += len(variaciones)
            
            self.log(f"Datos cargados desde '{archivo}'", "success")
            self.log(f"Total de elementos (con variaciones): {total}", "info")
            return True
            
        except json.JSONDecodeError:
            self.log(f"Error al decodificar JSON en '{archivo}'", "error")
            return False
        except Exception as e:
            self.log(f"Error: {str(e)}", "error")
            return False
    
    def generar_variaciones(self, palabra: str) -> List[str]:
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
    
    def extraer_partes_numeros(self, numero):
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
    
    def generar_wordlist(self, min_length=0, max_length=100):
        """Genera el diccionario de contraseñas"""
        self.log("Iniciando generación de wordlist...", "info")
        
        # Verificar datos
        total_items = sum(len(items) for items in self.informacion.values())
        if total_items == 0:
            self.log("No hay información para generar wordlist", "error")
            return False
        
        # Recopilar palabras base
        palabras_base = []
        for categoria in ["nombres", "apellidos", "apodos", "mascotas", 
                         "lugares", "empresas", "palabras_clave"]:
            palabras_base.extend(self.informacion[categoria])
        
        fechas = self.informacion["fechas"]
        numeros_originales = self.informacion["numeros_importantes"]
        
        # Extraer partes de números largos (cédulas, teléfonos)
        numeros = []
        for num in numeros_originales:
            numeros.extend(self.extraer_partes_numeros(num))
        numeros = list(set(numeros))  # Eliminar duplicados
        
        self.log(f"Procesados {len(numeros)} números (incluyendo fragmentos)", "verbose")
        
        simbolos = ["", "!", "@", "#", "$", "*", ".", "_", "-", "123", "321"]
        
        # Proceso de generación
        self.log("Generando variaciones de palabras...", "verbose")
        for palabra in palabras_base:
            for var in self.generar_variaciones(palabra):
                if min_length <= len(var) <= max_length:
                    self.wordlist.add(var)
        
        self.log("Combinando palabras con fechas y números...", "verbose")
        for palabra in palabras_base:
            for numero in (fechas + numeros):  # Usar TODOS los números
                combinaciones = [
                    f"{palabra}{numero}",
                    f"{palabra.lower()}{numero}",
                    f"{palabra.capitalize()}{numero}",
                    f"{numero}{palabra}",
                    f"{numero}{palabra.lower()}",
                    f"{numero}{palabra.capitalize()}"
                ]
                for comb in combinaciones:
                    if min_length <= len(comb) <= max_length:
                        self.wordlist.add(comb)
        
        self.log("Añadiendo símbolos comunes...", "verbose")
        for palabra in palabras_base[:15]:
            for numero in (fechas + numeros)[:30]:  # Aumentar a 30
                for simbolo in simbolos[:5]:
                    if simbolo:
                        comb1 = f"{palabra}{simbolo}{numero}"
                        comb2 = f"{palabra.capitalize()}{simbolo}{numero}"
                        if min_length <= len(comb1) <= max_length:
                            self.wordlist.add(comb1)
                        if min_length <= len(comb2) <= max_length:
                            self.wordlist.add(comb2)
        
        self.log("Generando combinaciones nombre+apellido...", "verbose")
        nombres = self.informacion["nombres"]
        apellidos = self.informacion["apellidos"]
        
        for nombre in nombres[:10]:
            for apellido in apellidos[:10]:
                combinaciones = [
                    f"{nombre}{apellido}",
                    f"{nombre.lower()}{apellido.lower()}",
                    f"{nombre}{apellido}".lower(),
                    f"{nombre}{apellido}".capitalize(),
                    f"{nombre}_{apellido}",
                    f"{nombre}.{apellido}",
                    f"{nombre}-{apellido}"
                ]
                for comb in combinaciones:
                    if min_length <= len(comb) <= max_length:
                        self.wordlist.add(comb)
                
                # Con fechas
                for fecha in fechas[:5]:
                    combinaciones_fecha = [
                        f"{nombre}{apellido}{fecha}",
                        f"{nombre}{fecha}",
                        f"{apellido}{fecha}",
                        f"{nombre.lower()}{apellido.lower()}{fecha}"
                    ]
                    for comb in combinaciones_fecha:
                        if min_length <= len(comb) <= max_length:
                            self.wordlist.add(comb)
        
        self.log("Combinando palabras entre sí...", "verbose")
        for i, palabra1 in enumerate(palabras_base[:15]):
            for palabra2 in palabras_base[:15]:
                if palabra1 != palabra2:
                    combinaciones = [
                        f"{palabra1}{palabra2}",
                        f"{palabra1}_{palabra2}",
                        f"{palabra1}{palabra2}".lower(),
                        f"{palabra1}{palabra2}".capitalize()
                    ]
                    for comb in combinaciones:
                        if min_length <= len(comb) <= max_length:
                            self.wordlist.add(comb)
        
        self.log("Generando formatos de fechas...", "verbose")
        for fecha in fechas:
            if min_length <= len(fecha) <= max_length:
                self.wordlist.add(fecha)
                self.wordlist.add(fecha[::-1])
            
            if len(fecha) == 8:
                formatos = [
                    f"{fecha[:2]}/{fecha[2:4]}/{fecha[4:]}",
                    f"{fecha[:2]}-{fecha[2:4]}-{fecha[4:]}",
                    f"{fecha[:2]}.{fecha[2:4]}.{fecha[4:]}"
                ]
                for fmt in formatos:
                    if min_length <= len(fmt) <= max_length:
                        self.wordlist.add(fmt)
        
        self.log("Añadiendo patrones comunes...", "verbose")
        patrones_comunes = ["password", "admin", "user", "root", "welcome", "qwerty"]
        for patron in patrones_comunes:
            for numero in (fechas + numeros)[:5]:
                combinaciones = [
                    f"{patron}{numero}",
                    f"{patron}{numero}!",
                    f"{patron.capitalize()}{numero}"
                ]
                for comb in combinaciones:
                    if min_length <= len(comb) <= max_length:
                        self.wordlist.add(comb)
        
        self.log("Añadiendo sufijos comunes...", "verbose")
        sufijos = ["123", "321", "!", "@", "#", ".", "_", "01", "00"]
        for palabra in palabras_base[:20]:
            for sufijo in sufijos:
                comb1 = f"{palabra}{sufijo}"
                comb2 = f"{palabra.capitalize()}{sufijo}"
                if min_length <= len(comb1) <= max_length:
                    self.wordlist.add(comb1)
                if min_length <= len(comb2) <= max_length:
                    self.wordlist.add(comb2)
        
        self.log(f"Wordlist generada: {len(self.wordlist):,} contraseñas únicas", "success")
        return True
    
    def guardar_wordlist(self, archivo_salida):
        """Guarda el wordlist en un archivo"""
        if not self.wordlist:
            self.log("No hay wordlist para guardar", "error")
            return False
        
        try:
            # Crear directorio si no existe
            directorio = os.path.dirname(archivo_salida)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)
                self.log(f"Directorio creado: {directorio}", "verbose")
            
            self.log(f"Ordenando {len(self.wordlist):,} contraseñas...", "verbose")
            palabras_ordenadas = sorted(self.wordlist, key=lambda x: (len(x), x.lower()))
            
            self.log(f"Guardando en '{archivo_salida}'...", "info")
            with open(archivo_salida, 'w', encoding='utf-8') as f:
                for palabra in palabras_ordenadas:
                    f.write(palabra + '\n')
            
            # Estadísticas
            longitudes = [len(p) for p in self.wordlist]
            tamaño_mb = os.path.getsize(archivo_salida) / (1024 * 1024)
            
            print(f"\n{Colors.GREEN}{Colors.BOLD}{'='*70}{Colors.RESET}")
            print(f"{Colors.GREEN}{Colors.BOLD}    WORDLIST GENERADA EXITOSAMENTE{Colors.RESET}")
            print(f"{Colors.GREEN}{Colors.BOLD}{'='*70}{Colors.RESET}")
            print(f"{Colors.CYAN}📄 Archivo:{Colors.RESET}      {archivo_salida}")
            print(f"{Colors.CYAN}📊 Contraseñas:{Colors.RESET}  {len(self.wordlist):,}")
            print(f"{Colors.CYAN}📏 Long. mín:{Colors.RESET}    {min(longitudes)} caracteres")
            print(f"{Colors.CYAN}📏 Long. máx:{Colors.RESET}    {max(longitudes)} caracteres")
            print(f"{Colors.CYAN}📏 Long. prom:{Colors.RESET}   {sum(longitudes)//len(longitudes)} caracteres")
            print(f"{Colors.CYAN}💾 Tamaño:{Colors.RESET}       {tamaño_mb:.2f} MB")
            print(f"{Colors.GREEN}{'='*70}{Colors.RESET}")
            
            # Ejemplos de uso
            print(f"\n{Colors.YELLOW}{Colors.BOLD}💡 EJEMPLOS DE USO:{Colors.RESET}")
            print(f"{Colors.WHITE}  hydra -l admin -P {archivo_salida} ssh://192.168.1.100{Colors.RESET}")
            print(f"{Colors.WHITE}  john --wordlist={archivo_salida} hash.txt{Colors.RESET}")
            print(f"{Colors.WHITE}  hashcat -m 0 -a 0 hash.txt {archivo_salida}{Colors.RESET}")
            print(f"{Colors.GREEN}{'='*70}{Colors.RESET}\n")
            
            return True
            
        except Exception as e:
            self.log(f"Error al guardar archivo: {str(e)}", "error")
            return False
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas de la información cargada"""
        print(f"\n{Colors.CYAN}{'='*70}{Colors.RESET}")
        print(f"{Colors.CYAN}{Colors.BOLD}    INFORMACIÓN DEL OBJETIVO{Colors.RESET}")
        print(f"{Colors.CYAN}{'='*70}{Colors.RESET}")
        
        for categoria, items in self.informacion.items():
            if items:
                print(f"{Colors.YELLOW}▸ {categoria.upper()}{Colors.RESET} ({len(items)} elementos)")
                # Mostrar hasta 5 items
                for i, item in enumerate(items[:5]):
                    print(f"  • {item}")
                if len(items) > 5:
                    print(f"  {Colors.WHITE}... y {len(items)-5} más{Colors.RESET}")
        
        total = sum(len(items) for items in self.informacion.values())
        print(f"{Colors.CYAN}{'='*70}{Colors.RESET}")
        print(f"{Colors.GREEN}Total de elementos: {total}{Colors.RESET}")
        print(f"{Colors.CYAN}{'='*70}{Colors.RESET}\n")

def main():
    parser = argparse.ArgumentParser(
        description='Dict-Max - Professional Wordlist Generator for Penetration Testing',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
{Colors.CYAN}Ejemplos de uso:{Colors.RESET}
  dict-max.py -u target.json -o wordlist.txt
  dict-max.py -u target.json -o /root/wordlists/custom.txt -v
  dict-max.py -u target.json -o output.txt --min 8 --max 16
  dict-max.py -u target.json -o output.txt --stats

{Colors.YELLOW}Uso con herramientas:{Colors.RESET}
  hydra -l admin -P wordlist.txt ssh://192.168.1.100
  john --wordlist=wordlist.txt hash.txt
  hashcat -m 0 -a 0 hash.txt wordlist.txt

{Colors.RED}⚠️  Solo para uso autorizado en pentesting{Colors.RESET}
        """
    )
    
    parser.add_argument('-u', '--user-data', 
                       required=True,
                       metavar='FILE',
                       help='Archivo JSON con información del objetivo')
    
    parser.add_argument('-o', '--output',
                       required=True,
                       metavar='FILE',
                       help='Archivo de salida para el wordlist')
    
    parser.add_argument('--min',
                       type=int,
                       default=0,
                       metavar='N',
                       help='Longitud mínima de contraseñas (default: 0)')
    
    parser.add_argument('--max',
                       type=int,
                       default=100,
                       metavar='N',
                       help='Longitud máxima de contraseñas (default: 100)')
    
    parser.add_argument('-v', '--verbose',
                       action='store_true',
                       help='Modo verbose (muestra más detalles)')
    
    parser.add_argument('--stats',
                       action='store_true',
                       help='Muestra estadísticas de la información cargada')
    
    parser.add_argument('--version',
                       action='version',
                       version=f'Dict-Max v{__version__}')
    
    # Mostrar banner
    print_banner()
    
    args = parser.parse_args()
    
    # Crear instancia
    dict_max = DictMax()
    dict_max.verbose = args.verbose
    
    # Cargar datos
    if not dict_max.cargar_json(args.user_data):
        sys.exit(1)
    
    # Mostrar estadísticas si se solicita
    if args.stats:
        dict_max.mostrar_estadisticas()
    
    # Generar wordlist
    if not dict_max.generar_wordlist(args.min, args.max):
        sys.exit(1)
    
    # Guardar wordlist
    if not dict_max.guardar_wordlist(args.output):
        sys.exit(1)
    
    dict_max.log("Proceso completado exitosamente", "success")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[!]{Colors.RESET} Proceso interrumpido por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}[-]{Colors.RESET} Error fatal: {str(e)}")
        sys.exit(1)
