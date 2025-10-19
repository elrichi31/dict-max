# 🔐 Dict-Max - Generador Profesional de Wordlists

```
    ██████╗ ██╗ ██████╗████████╗      ███╗   ███╗ █████╗ ██╗  ██╗
    ██╔══██╗██║██╔════╝╚══██╔══╝      ████╗ ████║██╔══██╗╚██╗██╔╝
    ██║  ██║██║██║        ██║   █████╗██╔████╔██║███████║ ╚███╔╝ 
    ██║  ██║██║██║        ██║   ╚════╝██║╚██╔╝██║██╔══██║ ██╔██╗ 
    ██████╔╝██║╚██████╗   ██║         ██║ ╚═╝ ██║██║  ██║██╔╝ ██╗
    ╚═════╝ ╚═╝ ╚═════╝   ╚═╝         ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
```

Generador profesional de diccionarios de contraseñas para pentesting y auditorías de seguridad.

## ⚠️ AVISO LEGAL

**Solo para uso autorizado en pentesting y auditorías de seguridad. El uso no autorizado es ILEGAL.**

Este proyecto es exclusivamente para:
- Auditorías de seguridad autorizadas
- Pentesting con permiso explícito por escrito
- Evaluaciones de seguridad de sistemas propios
- Propósitos educativos en entornos controlados

## 🚀 Inicio Rápido

```bash
python dict-max.py -u example_target.json -o wordlist.txt
```

## 💻 Uso

### Sintaxis Básica
```bash
python dict-max.py -u <archivo_json> -o <salida> [opciones]
```

### Opciones Disponibles
```
-u, --user-data FILE    Archivo JSON con información del objetivo (requerido)
-o, --output FILE       Archivo de salida para el wordlist (requerido)
--min N                 Longitud mínima de contraseñas (default: 0)
--max N                 Longitud máxima de contraseñas (default: 100)
-v, --verbose           Modo verbose (más detalles)
--stats                 Muestra estadísticas de la información cargada
--version               Muestra la versión
-h, --help              Muestra ayuda
```

### Ejemplos

```bash
# Básico
python dict-max.py -u target.json -o wordlist.txt

# Con estadísticas y modo verbose
python dict-max.py -u target.json -o wordlist.txt -v --stats

# Filtrar longitud (8-16 caracteres, recomendado)
python dict-max.py -u target.json -o wordlist.txt --min 8 --max 16

# Ruta personalizada
python dict-max.py -u target.json -o C:\wordlists\custom.txt
```

## 📋 Formato del Archivo JSON

Crea un archivo JSON con información del objetivo:

```json
{
  "nombres": ["John", "Jane", "Michael"],
  "apellidos": ["Smith", "Johnson"],
  "apodos": ["Johnny", "Mike"],
  "fechas": ["15081990", "1990", "2023"],
  "mascotas": ["Max", "Luna", "Rocky"],
  "lugares": ["New York", "Miami"],
  "empresas": ["Tech Corp", "Digital Solutions"],
  "palabras_clave": ["admin", "password", "welcome"],
  "numeros_importantes": ["123456", "5551234567"]
}
```

### Categorías Explicadas

- **nombres**: Nombres del objetivo, familiares
- **apellidos**: Apellidos
- **apodos**: Nicknames, usernames, alias
- **fechas**: Cumpleaños (DDMMYYYY), años importantes
- **mascotas**: Nombres de perros, gatos, etc.
- **lugares**: Ciudad, país, direcciones
- **empresas**: Lugar de trabajo, universidad, organizaciones
- **palabras_clave**: Hobbies, deportes, acrónimos
- **numeros_importantes**: Cédulas, teléfonos, números de identificación

## 🎯 Características Principales

### ✅ Generación Inteligente de Wordlists
- Múltiples variaciones (mayúsculas, minúsculas, leetspeak, invertidas)
- Combinaciones avanzadas de palabras + fechas + números + símbolos
- Patrones comunes (nombre+apellido+fecha)

### ✅ Procesamiento Inteligente de Palabras con Espacios
**Entrada:** `"New York"`

**Genera:**
- `NewYork` (junto)
- `New-York` (con guión)
- `New_York` (con guión bajo)
- `new.york` (con punto)
- `NY` (iniciales)

### ✅ Extracción de Fragmentos de Números Largos 🔥
**NOVEDAD v1.3.0:** Procesamiento inteligente de cédulas, teléfonos y números de identificación.

**Entrada:** `"1709223059"` (Cédula de 10 dígitos)

**Genera fragmentos automáticamente:**
- Fragmentos de 4 dígitos: `1709`, `7092`, `0922`, `9223`, `2230`, `3059`
- Fragmentos de 6 dígitos: `170922`, `709223`, `092230`, `922305`, `223059`
- Fragmentos de 8 dígitos: `17092230`, `70922305`, `09223059`
- Y muchos más...

**Resultado:** Combinaciones como `admin1709`, `juan170922`, `max223059`, etc.

### ✅ Eliminación Automática de Duplicados

### ✅ Estadísticas Detalladas del Wordlist Generado

## 🎯 Patrones Generados

El generador crea automáticamente:

### 1. Variaciones de Palabras
```
carlos → carlos, Carlos, CARLOS, solrac (invertida)
carlos → c@rlos, c4rlos (leetspeak)
```

### 2. Palabra + Fecha/Número
```
carlos1990, garcia15081990, 1990carlos
Carlos2023, JUAN123, maria@1990
```

### 3. Nombre + Apellido
```
carlosgarcia, CarlosGarcia, carlos_garcia
carlos.garcia, carlos-garcia
```

### 4. Nombre + Apellido + Fecha (Muy Común)
```
carlosgarcia1990, JuanMartinez15081990
Carlos.Garcia1990, juan_rodriguez2023
```

### 5. Con Fragmentos de Números Largos
```
admin1709, carlos170922, max09223059
Juan223059, Maria066925
```

## 🛠️ Integración con Herramientas de Pentesting

### Hydra
```bash
# SSH
hydra -l admin -P wordlist.txt ssh://192.168.1.100

# FTP
hydra -l user -P wordlist.txt ftp://192.168.1.100

# HTTP Form
hydra -l admin -P wordlist.txt 192.168.1.100 http-post-form "/login:user=^USER^&pass=^PASS^:F=incorrect"
```

### John the Ripper
```bash
# Básico
john --wordlist=wordlist.txt hash.txt

# Con reglas
john --wordlist=wordlist.txt --rules hash.txt
```

### Hashcat
```bash
# MD5
hashcat -m 0 -a 0 hash.txt wordlist.txt

# SHA256
hashcat -m 1400 -a 0 hash.txt wordlist.txt

# NTLM (Windows)
hashcat -m 1000 -a 0 hash.txt wordlist.txt
```

### Medusa
```bash
# SSH
medusa -h 192.168.1.100 -u admin -P wordlist.txt -M ssh

# RDP
medusa -h 192.168.1.100 -u admin -P wordlist.txt -M rdp
```

## 📊 Ejemplo de Salida

```
======================================================================
    WORDLIST GENERADA EXITOSAMENTE
======================================================================
📄 Archivo:      wordlist.txt
📊 Contraseñas:  7,349
📏 Long. mín:    4 caracteres
📏 Long. máx:    25 caracteres
📏 Long. prom:   12 caracteres
💾 Tamaño:       0.08 MB
======================================================================

💡 EJEMPLOS DE USO:
  hydra -l admin -P wordlist.txt ssh://192.168.1.100
  john --wordlist=wordlist.txt hash.txt
  hashcat -m 0 -a 0 hash.txt wordlist.txt
======================================================================
```

## 📁 Estructura del Proyecto

```
dict/
├── dict-max.py             # Programa principal
├── example_target.json     # Plantilla de ejemplo
└── README.md               # Esta documentación
```

## 🎓 Mejores Prácticas para OSINT

### Fuentes de Información
- **Facebook**: Mascotas, familia, lugares, fechas importantes
- **Instagram**: Hobbies, viajes, estilo de vida
- **LinkedIn**: Trabajo, educación, certificaciones
- **Twitter**: Intereses, equipos deportivos

### Datos Clave a Recopilar
✅ Fechas de cumpleaños (objetivo y familiares)  
✅ Nombres de mascotas (¡MUY común en contraseñas!)  
✅ Cédulas/DNI completos (se extraerán fragmentos automáticamente)  
✅ Números de teléfono  
✅ Lugares importantes (ciudad natal, viajes)  
✅ Empresas/Organizaciones  
✅ Apodos y nicknames  
✅ Hobbies y pasatiempos  

### Tips Profesionales
1. **Números largos**: Incluye cédulas y teléfonos completos en `numeros_importantes`
2. **Fragmentos automáticos**: Dict-Max extraerá automáticamente los fragmentos relevantes
3. **Longitud recomendada**: Usa `--min 8 --max 16` para contraseñas más probables
4. **Combina datos**: Las mejores contraseñas combinan palabra + número

## 💡 Tips Avanzados

### Combinar Wordlists
```powershell
# PowerShell
Get-Content wordlist1.txt, wordlist2.txt | Sort-Object -Unique > combined.txt
```

### Filtrar por Longitud
```powershell
# PowerShell
Get-Content wordlist.txt | Where-Object { $_.Length -ge 8 -and $_.Length -le 16 } > filtered.txt
```

### Estadísticas
```powershell
# Contar líneas
(Get-Content wordlist.txt).Count

# Ver tamaño del archivo
Get-Item wordlist.txt | Select-Object Name, Length
```

## 🆕 Changelog

### v1.3.0 (Actual)
- ✨ Mejoras en la interfaz CLI
- ✅ Optimización del procesamiento de fragmentos
- ✅ Banner ASCII mejorado

### v1.2.0
- 🔥 **Nuevo**: Extracción inteligente de fragmentos de números largos
- 🔥 **Nuevo**: Ventana deslizante para cédulas/teléfonos
- ✅ Procesa hasta 50+ fragmentos de números de 10 dígitos
- ✅ Ideal para cédulas ecuatorianas y números de identificación

### v1.1.0
- ✨ Procesamiento inteligente de palabras con espacios
- ✨ Genera variaciones: junto, guión, guión bajo, punto
- ✨ Extrae iniciales de palabras compuestas (HSM, NY)

### v1.0.0
- ✅ Lanzamiento inicial
- ✅ CLI profesional estilo hacking
- ✅ Colores ANSI en terminal

## 📚 Herramientas Relacionadas

- [CUPP](https://github.com/Mebus/cupp) - Common User Passwords Profiler
- [Crunch](https://sourceforge.net/projects/crunch-wordlist/) - Pattern-based generator
- [CeWL](https://github.com/digininja/CeWL) - Web spider wordlist
- [Mentalist](https://github.com/sc0tfree/mentalist) - GUI generator

## 👤 Autor

**Nicolas**  
Version: 1.3.0  
Fecha: Octubre 2025

---

<p align="center">
  <b>🛡️ Usa esta herramienta de manera ética y responsable</b><br>
  <i>"Con gran poder viene gran responsabilidad"</i>
</p>

---

**⭐ Si te fue útil, considera dar una estrella al proyecto!**
