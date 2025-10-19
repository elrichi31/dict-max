#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utils module - Colors and display utilities
"""

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
    from . import __version__, __author__
    
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


def log(message, level="info", verbose=False):
    """Logger con colores"""
    if level == "info":
        print(f"{Colors.CYAN}[*]{Colors.RESET} {message}")
    elif level == "success":
        print(f"{Colors.GREEN}[+]{Colors.RESET} {message}")
    elif level == "error":
        print(f"{Colors.RED}[-]{Colors.RESET} {message}")
    elif level == "warning":
        print(f"{Colors.YELLOW}[!]{Colors.RESET} {message}")
    elif level == "verbose" and verbose:
        print(f"{Colors.WHITE}[~]{Colors.RESET} {message}")
