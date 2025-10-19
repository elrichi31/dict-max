#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dict-Max - Professional Wordlist Generator
Command-line interface for generating custom wordlists
"""

import sys
import argparse

from dict_max import DictMax, print_banner, __version__, __author__
from dict_max.utils import Colors


def main():
    parser = argparse.ArgumentParser(
        description="Dict-Max - Professional Wordlist Generator for Penetration Testing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  dict-max.py -u target.json -o wordlist.txt
  dict-max.py -u target.json -o /root/wordlists/custom.txt -v
  dict-max.py -u target.json -o output.txt --min 8 --max 16
  dict-max.py -u target.json -o output.txt --stats

Uso con herramientas:
  hydra -l admin -P wordlist.txt ssh://192.168.1.100
  john --wordlist=wordlist.txt hash.txt
  hashcat -m 0 -a 0 hash.txt wordlist.txt

Solo para uso autorizado en pentesting
        """
    )
    
    parser.add_argument("-u", "--user-data", 
                       required=True,
                       metavar="FILE",
                       help="Archivo JSON con información del objetivo")
    
    parser.add_argument("-o", "--output",
                       required=True,
                       metavar="FILE",
                       help="Archivo de salida para el wordlist")
    
    parser.add_argument("--min",
                       type=int,
                       default=0,
                       metavar="N",
                       help="Longitud mínima de contraseñas (default: 0)")
    
    parser.add_argument("--max",
                       type=int,
                       default=100,
                       metavar="N",
                       help="Longitud máxima de contraseñas (default: 100)")
    
    parser.add_argument("-v", "--verbose",
                       action="store_true",
                       help="Modo verbose (muestra más detalles)")
    
    parser.add_argument("--stats",
                       action="store_true",
                       help="Muestra estadísticas de la información cargada")
    
    parser.add_argument("--version",
                       action="version",
                       version=f"Dict-Max v{__version__}")
    
    print_banner()
    
    args = parser.parse_args()
    
    dict_max = DictMax()
    dict_max.verbose = args.verbose
    
    if not dict_max.cargar_json(args.user_data):
        sys.exit(1)
    
    if args.stats:
        dict_max.mostrar_estadisticas()
    
    if not dict_max.generar_wordlist(args.min, args.max):
        sys.exit(1)
    
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
