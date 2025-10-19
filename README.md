# 🔐 DICT-MAX - Professional Wordlist Generator# 🔐 Dict-Max - Professional Wordlist Generator# 🔐 Dict-Max - Professional Wordlist Generator# 🔐 Dict-Max - Professional Wordlist Generator# 🔐 Generador de Diccionarios de Contraseñas (Wordlist Generator)



![Version](https://img.shields.io/badge/version-1.3.0-blue.svg)

![Python](https://img.shields.io/badge/python-3.6%2B-green.svg)

![License](https://img.shields.io/badge/license-MIT-red.svg)```



**DICT-MAX** es una herramienta profesional de generación de wordlists personalizadas para pruebas de penetración autorizadas. Genera diccionarios de contraseñas inteligentes basados en información OSINT del objetivo.    ██████╗ ██╗ ██████╗████████╗      ███╗   ███╗ █████╗ ██╗  ██╗



```    ██╔══██╗██║██╔════╝╚══██╔══╝      ████╗ ████║██╔══██╗╚██╗██╔╝```

    ██████╗ ██╗ ██████╗████████╗      ███╗   ███╗ █████╗ ██╗  ██╗

    ██╔══██╗██║██╔════╝╚══██╔══╝      ████╗ ████║██╔══██╗╚██╗██╔╝    ██║  ██║██║██║        ██║   █████╗██╔████╔██║███████║ ╚███╔╝ 

    ██║  ██║██║██║        ██║   █████╗██╔████╔██║███████║ ╚███╔╝ 

    ██║  ██║██║██║        ██║   ╚════╝██║╚██╔╝██║██╔══██║ ██╔██╗     ██║  ██║██║██║        ██║   ╚════╝██║╚██╔╝██║██╔══██║ ██╔██╗     ██████╗ ██╗ ██████╗████████╗      ███╗   ███╗ █████╗ ██╗  ██╗

    ██████╔╝██║╚██████╗   ██║         ██║ ╚═╝ ██║██║  ██║██╔╝ ██╗

    ╚═════╝ ╚═╝ ╚═════╝   ╚═╝         ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ██████╔╝██║╚██████╗   ██║         ██║ ╚═╝ ██║██║  ██║██╔╝ ██╗

```

    ╚═════╝ ╚═╝ ╚═════╝   ╚═╝         ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ██╔══██╗██║██╔════╝╚══██╔══╝      ████╗ ████║██╔══██╗╚██╗██╔╝Herramienta profesional de línea de comandos para generar wordlists personalizadas basadas en información del objetivo. Ideal para auditorías de seguridad y pentesting.Herramienta para generar wordlists personalizadas basadas en información del objetivo para auditorías de seguridad y pentesting.

---

```

## 🎯 Características Principales

    ██║  ██║██║██║        ██║   █████╗██╔████╔██║███████║ ╚███╔╝ 

### ✨ Generación Inteligente

- **Extracción de fragmentos numéricos**: Genera fragmentos de 4, 5, 6, 7 y 8 dígitos desde números largos (cédulas, teléfonos)**Generador profesional de wordlists para pentesting con procesamiento inteligente de números largos.**

- **Procesamiento de espacios**: Convierte automáticamente nombres compuestos en múltiples variaciones

- **Combinaciones avanzadas**: Palabras + números, nombres + apellidos, símbolos comunes    ██║  ██║██║██║        ██║   ╚════╝██║╚██╔╝██║██╔══██║ ██╔██╗ 

- **Leetspeak**: Conversiones automáticas (a→4, e→3, i→1, o→0, s→5)

- **Variaciones de mayúsculas**: lowercase, UPPERCASE, Capitalize, CamelCase## ⚠️ AVISO LEGAL



### 🔧 Funcionalidades    ██████╔╝██║╚██████╗   ██║         ██║ ╚═╝ ██║██║  ██║██╔╝ ██╗

- **CLI Profesional**: Interfaz al estilo de herramientas de hacking (Hydra, John, Hashcat)

- **Filtrado por longitud**: Control preciso de tamaño mínimo y máximo**Solo para uso autorizado en pentesting y auditorías de seguridad. El uso no autorizado es ILEGAL.**

- **Estadísticas detalladas**: Información completa sobre el wordlist generado

- **Modo verbose**: Seguimiento en tiempo real del proceso de generación    ╚═════╝ ╚═╝ ╚═════╝   ╚═╝         ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝```## ⚠️ AVISO LEGAL IMPORTANTE

- **Sin dependencias externas**: Solo Python 3.6+ estándar

## 🚀 Uso Rápido

---

```

## 📦 Instalación

```bash

```bash

# Clonar el repositoriopython dict-max.py -u ejemplo_target.json -o wordlist.txt    ██████╗ ██╗ ██████╗████████╗      ███╗   ███╗ █████╗ ██╗  ██╗

git clone https://github.com/tu-usuario/dict-max.git

cd dict-max```



# No requiere instalación de dependenciasGenerador profesional de wordlists para pentesting con CLI estilo hacking.

python dict-max.py --help

```## 💻 Opciones Disponibles



**Requisitos:**    ██╔══██╗██║██╔════╝╚══██╔══╝      ████╗ ████║██╔══██╗╚██╗██╔╝```

- Python 3.6 o superior

- Sistema operativo: Windows, Linux, macOS```bash



----u, --user-data FILE    Archivo JSON con info del objetivo (requerido)## ⚠️ AVISO LEGAL



## 🚀 Uso Básico-o, --output FILE       Archivo de salida (requerido)



### Sintaxis--min N                 Longitud mínima (default: 0)    ██║  ██║██║██║        ██║   █████╗██╔████╔██║███████║ ╚███╔╝ ┌─────────────────────────────────────────────────────────────┐

```bash

python dict-max.py -u <archivo.json> -o <salida.txt> [opciones]--max N                 Longitud máxima (default: 100)

```

-v, --verbose           Modo verbose**Solo para uso autorizado en pentesting y auditorías de seguridad. El uso no autorizado es ILEGAL.**

### Argumentos

--stats                 Muestra estadísticas del objetivo

| Argumento | Descripción | Ejemplo |

|-----------|-------------|---------|--version               Muestra la versión    ██║  ██║██║██║        ██║   ╚════╝██║╚██╔╝██║██╔══██║ ██╔██╗ │  Esta herramienta está diseñada EXCLUSIVAMENTE para:         │

| `-u`, `--user-data` | Archivo JSON con información del objetivo | `-u target.json` |

| `-o`, `--output` | Archivo de salida para el wordlist | `-o passwords.txt` |-h, --help              Ayuda

| `--min` | Longitud mínima de contraseñas (default: 0) | `--min 8` |

| `--max` | Longitud máxima de contraseñas (default: 100) | `--max 20` |```## 🚀 Uso Rápido

| `-v`, `--verbose` | Modo detallado con información del proceso | `-v` |

| `--stats` | Mostrar estadísticas detalladas al finalizar | `--stats` |



### Ejemplos de Uso## 📝 Ejemplos de Uso    ██████╔╝██║╚██████╗   ██║         ██║ ╚═╝ ██║██║  ██║██╔╝ ██╗│  • Auditorías de seguridad autorizadas                       │



**Básico:**

```bash

python dict-max.py -u target.json -o wordlist.txt```bash```bash

```

# Básico

**Con filtros de longitud:**

```bashpython dict-max.py -u target.json -o wordlist.txtpython dict-max.py -u ejemplo_target.json -o wordlist.txt    ╚═════╝ ╚═╝ ╚═════╝   ╚═╝         ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝│  • Pentesting con permiso explícito por escrito              │

python dict-max.py -u target.json -o wordlist.txt --min 8 --max 16

```



**Con modo verbose y estadísticas:**# Con estadísticas y verbose```

```bash

python dict-max.py -u target.json -o wordlist.txt --min 8 --max 20 -v --statspython dict-max.py -u target.json -o wordlist.txt -v --stats

```

```│  • Evaluaciones de seguridad de sistemas propios             │

---

# Filtrar longitud 8-16 caracteres (recomendado)

## 📋 Formato del Archivo JSON

python dict-max.py -u target.json -o wordlist.txt --min 8 --max 16## 💻 Opciones

El archivo JSON debe contener la siguiente estructura:



```json

{# Con todas las opciones│  • Propósitos educativos en entornos controlados             │

  "nombres": ["Juan", "Maria", "Carlos"],

  "apellidos": ["Garcia", "Martinez", "Lopez"],python dict-max.py -u target.json -o /root/wordlists/custom.txt --min 8 --max 20 -v --stats

  "apodos": ["Juancho", "Mari", "Carlitos"],

  "fechas": ["15/08/1990", "2020", "01-01-2000"],``````bash

  "mascotas": ["Max", "Luna", "Toby"],

  "lugares": ["New York", "Barcelona", "Ecuador"],

  "empresas": ["Tech Solutions", "Digital Corp"],

  "palabras_clave": ["admin", "password", "secure"],## 📋 Formato del Archivo JSON-u, --user-data FILE    Archivo JSON con info del objetivo (requerido)## ⚠️ AVISO LEGAL│                                                               │

  "numeros_importantes": ["1234567890", "0987654321", "555-1234"]

}

```

```json-o, --output FILE       Archivo de salida (requerido)

### Categorías Soportadas

{

| Categoría | Descripción | Ejemplo |

|-----------|-------------|---------|    "nombres": ["Nicolas", "Carlos"],--min N                 Longitud mínima (default: 0)│  ⚖️ El uso no autorizado es ILEGAL                           │

| `nombres` | Nombres propios del objetivo | `"Nicolas", "Maria"` |

| `apellidos` | Apellidos del objetivo | `"Garcia", "Rodriguez"` |    "apellidos": ["Moina", "Garcia"],

| `apodos` | Apodos o sobrenombres | `"Nico", "Mari"` |

| `fechas` | Fechas importantes (nacimiento, aniversarios) | `"15/08/1990", "2020"` |    "apodos": ["Nico", "Carlitos"],--max N                 Longitud máxima (default: 100)

| `mascotas` | Nombres de mascotas | `"Max", "Luna"` |

| `lugares` | Ciudades, países, lugares favoritos | `"Ecuador", "New York"` |    "fechas": ["31082002", "2002"],

| `empresas` | Nombres de empresas o negocios | `"Hostal Santa Maria"` |

| `palabras_clave` | Palabras clave personalizadas | `"admin", "secure"` |    "mascotas": ["Jack", "Max"],-v, --verbose           Modo verbose**Solo para uso autorizado en pentesting y auditorías de seguridad. El uso no autorizado es ILEGAL.**│  ⚖️ El autor NO se responsabiliza del mal uso                │

| `numeros_importantes` | Cédulas, teléfonos, números significativos | `"1753066925"` |

    "lugares": ["Ecuador", "New York"],

---

    "empresas": ["Hostal Santa Maria"],--stats                 Muestra estadísticas del objetivo

## 🔬 Algoritmos de Generación

    "palabras_clave": ["hsmg", "futbol"],

### 1. Extracción de Fragmentos Numéricos

Para números largos (8+ dígitos), extrae fragmentos de **múltiples longitudes**:    "numeros_importantes": ["1753066925", "123"]-h, --help              Ayuda└─────────────────────────────────────────────────────────────┘



**Ejemplo con cédula `1709223059`:**}

```

Fragmentos de 4 dígitos: 1709, 7092, 0922, 9223, 2230, 3059``````

Fragmentos de 5 dígitos: 17092, 70922, 09223, 92230, 22305, 23059

Fragmentos de 6 dígitos: 170922, 709223, 092230, 922305, 223059

Fragmentos de 7 dígitos: 1709223, 7092230, 0922305, 9223059

Fragmentos de 8 dígitos: 17092230, 70922305, 09223059### 📌 Categorías Explicadas## 🚀 Uso Rápido```

```



**Resultado:** `hsmg1709`, `hsmg170922`, `hsmg17092230`, etc.

- **nombres**: Nombre(s) del objetivo, familiares## 📝 Ejemplos de Uso

### 2. Procesamiento de Espacios

Convierte nombres compuestos en múltiples variaciones:- **apellidos**: Apellido(s)



**Ejemplo con `"New York"`:**- **apodos**: Nicknames, usernames, alias

```

NewYork          (unido)- **fechas**: Cumpleaños (DDMMYYYY), años importantes

New-York         (guión)

New_York         (guión bajo)- **mascotas**: Nombres de perros, gatos, etc.```bash

new.york         (punto)

NY               (iniciales)- **lugares**: Ciudad, país, direcciones

```

- **empresas**: Trabajo, universidad, organizaciones# Básico```bash## 🎯 Características Principales

### 3. Combinaciones Generadas

- **palabras_clave**: Hobbies, deportes, acrónimos

#### Fase 1: Variaciones básicas

- Lowercase, UPPERCASE, Capitalize- **numeros_importantes**: Cédulas, teléfonos, DNI (¡enteros o fragmentos!)python dict-max.py -u target.json -o wordlist.txt

- Inversión de cadena

- Leetspeak (a→4, e→3, i→1, o→0, s→5)



#### Fase 2: Palabras + Números## 🔥 Características Especialespython dict-max.py -u ejemplo_target.json -o wordlist.txt

```

palabra + numero → juan1990

numero + palabra → 1990juan

palabra + fecha → maria15081990### 1️⃣ Manejo Inteligente de Espacios# Con estadísticas y verbose

```



#### Fase 3: Palabras + Símbolos + Números

```**Entrada:** `"New York"`  python dict-max.py -u target.json -o wordlist.txt -v --stats```✅ **Generación inteligente de wordlists** basada en información del objetivo  

palabra + simbolo + numero → admin@2020, secure#1234

```**Genera:**



#### Fase 4: Nombres + Apellidos- `NewYork` (junto)

```

nombre + apellido → JuanGarcia, juan.garcia, juan_garcia- `New-York` (guión)

nombre + apellido + fecha → JuanGarcia1990

```- `New_York` (guión bajo)# Filtrar longitud 8-16 caracteres✅ **Múltiples variaciones** (mayúsculas, minúsculas, leetspeak, invertidas)  



#### Fase 5: Combinaciones entre palabras- `new.york` (punto)

```

palabra1 + palabra2 → adminpassword, admin_password- `NY` (iniciales)python dict-max.py -u target.json -o wordlist.txt --min 8 --max 16

```



#### Fase 6: Formatos de fechas

```**Entrada:** `"Hostal Santa Maria"`  ## 💻 Opciones✅ **Combinaciones avanzadas** de palabras + fechas + números + símbolos  

DD/MM/YYYY → 15081990, 1990, 0815, 1508

```**Genera:**



#### Fase 7: Patrones comunes- `HostalSantaMaria`# Ruta personalizada

```

palabra + año → admin2020, secure2021- `Hostal-Santa-Maria`

palabra + 123 → password123

```- `HSM` (iniciales)python dict-max.py -u target.json -o /root/wordlists/custom.txt -v✅ **Patrones comunes** como nombre+apellido+fecha  



#### Fase 8: Sufijos comunes- Y más...

```

palabra + sufijo → admin!, password@, secure#```

```

### 2️⃣ Extracción de Fragmentos de Números Largos 🆕

---

```bash✅ **Soporte para JSON** para cargar información rápidamente  

## 🔗 Integración con Herramientas

**¡NOVEDAD v1.2.0!** Procesamiento inteligente de cédulas, teléfonos y números de identificación.

### Hydra (SSH, FTP, HTTP)

```bash## 📋 Formato JSON

# SSH Brute Force

hydra -l admin -P wordlist.txt ssh://192.168.1.100**Entrada:** `"1709223059"` (Cédula ecuatoriana)  



# FTP Brute Force**Genera fragmentos automáticamente:**-u, --user-data FILE    Archivo JSON con info del objetivo (requerido)✅ **Eliminación automática de duplicados**  

hydra -l usuario -P wordlist.txt ftp://192.168.1.100



# HTTP Form

hydra -l admin -P wordlist.txt 192.168.1.100 http-post-form "/login:user=^USER^&pass=^PASS^:F=incorrect"**Fragmentos de 4 dígitos:**```json

```

- `1709`, `7092`, `0922`, `9223`, `2230`, `3059`

### John the Ripper

```bash{-o, --output FILE       Archivo de salida (requerido)✅ **Estadísticas detalladas** del wordlist generado  

# Hash cracking

john --wordlist=wordlist.txt hash.txt**Fragmentos de 6 dígitos:**



# Con reglas adicionales- `170922`, `709223`, `092230`, `922305`, `223059`    "nombres": ["Nicolas", "Carlos"],

john --wordlist=wordlist.txt --rules hash.txt

```



### Hashcat**Fragmentos de 8 dígitos:**    "apellidos": ["Moina", "Garcia"],--min N                 Longitud mínima (default: 0)✅ **Ejemplos de uso** con herramientas populares  

```bash

# MD5- `17092230`, `70922305`, `09223059`

hashcat -m 0 -a 0 hash.txt wordlist.txt

    "apodos": ["Nico", "Carlitos"],

# SHA256

hashcat -m 1400 -a 0 hash.txt wordlist.txt**Primeros y últimos:**



# NTLM- Primeros: `1709`, `170922`, `17092230`    "fechas": ["31082002", "2002"],--max N                 Longitud máxima (default: 100)

hashcat -m 1000 -a 0 hash.txt wordlist.txt

```- Últimos: `3059`, `223059`, `09223059`



### Medusa    "mascotas": ["Jack", "Max"],

```bash

# SSH**Resultado:** 

medusa -h 192.168.1.100 -u admin -P wordlist.txt -M ssh

```    "lugares": ["Ecuador", "New York"],-v, --verbose           Modo verbose## 📋 Requisitos

# RDP

medusa -h 192.168.1.100 -u admin -P wordlist.txt -M rdphsmg170922  ✅ (palabra_clave + fragmento de cédula)

```

Nicolas1709 ✅ (nombre + fragmento)    "empresas": ["Hostal Santa Maria"],

---

Jack223059  ✅ (mascota + fragmento)

## 📊 Ejemplo de Salida

```    "palabras_clave": ["hsmg", "futbol"],--stats                 Muestra estadísticas

```

======================================================================

    WORDLIST GENERADA EXITOSAMENTE

======================================================================**💡 Perfecto para:**    "numeros_importantes": ["123", "1753066925"]

📄 Archivo:      wordlist.txt

📊 Contraseñas:  14,461- Cédulas ecuatorianas (10 dígitos)

📏 Long. mín:    8 caracteres

📏 Long. máx:    18 caracteres- DNI, pasaportes}-h, --help              Ayuda- **Python 3.6+** (sin librerías externas necesarias)

📏 Long. prom:   12 caracteres

💾 Tamaño:       0.19 MB- Números de teléfono

======================================================================

- Cualquier identificación numérica```

💡 EJEMPLOS DE USO:

  hydra -l admin -P wordlist.txt ssh://192.168.1.100

  john --wordlist=wordlist.txt hash.txt

  hashcat -m 0 -a 0 hash.txt wordlist.txt## 🎯 Patrones Generados```- Sistema operativo: Windows, Linux, macOS

======================================================================

```



---### Variaciones Básicas## 🎯 Características Especiales



## 🎓 Mejores Prácticas OSINT```



### Recopilación de Informaciónnicolas → nicolas, Nicolas, NICOLAS, salocin (invertida)

1. **Redes Sociales**: Facebook, Instagram, LinkedIn, Twitter

2. **Registros Públicos**: Nombres, fechas de nacimiento, direcciones```

3. **Sitios Web**: Páginas personales, blogs, foros

4. **Bases de Datos**: Filtraciones previas, registros públicos### 🔥 Manejo Inteligente de Espacios

5. **Metadatos**: Fotos, documentos, archivos públicos

### Leetspeak

### Información Relevante para Passwords

- ✅ Nombres completos y apodos```## 📝 Ejemplos## 🚀 Instalación y Uso

- ✅ Fechas de nacimiento (propias y familiares)

- ✅ Nombres de mascotasnicolas → n1c0l@s, n1c0l4s

- ✅ Equipos deportivos favoritos

- ✅ Lugares de trabajo o estudiosadmin   → @dm1nLas palabras con espacios se procesan automáticamente:

- ✅ Ciudades o países importantes

- ✅ Números de identificación (cédulas, DNI)```

- ✅ Números de teléfono

- ✅ Aniversarios importantes



### Estrategia de Generación### Palabras Compuestas

1. **Específico → General**: Comenzar con información muy específica

2. **Fechas recientes**: Priorizar fechas de los últimos 5-10 años```**Entrada:** `"New York"`  

3. **Variaciones múltiples**: Incluir todas las variaciones posibles

4. **Longitud estratégica**: Filtrar según políticas de contraseñas del objetivoNew York → NewYork, New-York, New_York, NY



---```**Genera:**```bash### Instalación



## ⚠️ ADVERTENCIA LEGAL



```### Fragmentos de Números 🔥- `NewYork` (junto)

╔════════════════════════════════════════════════════════════════╗

║                    ⚠️  ADVERTENCIA LEGAL ⚠️                     ║```

╠════════════════════════════════════════════════════════════════╣

║                                                                ║1709223059 → hsmg1709, hsmg170922, nicolas223059- `New-York` (con guión)# Básico```bash

║  Esta herramienta está diseñada EXCLUSIVAMENTE para:          ║

║                                                                ║1753066925 → Jack1753, Ecuador066925

║  ✓ Pruebas de penetración AUTORIZADAS                         ║

║  ✓ Auditorías de seguridad LEGALES                            ║```- `New_York` (con guión bajo)

║  ✓ Investigaciones de seguridad ÉTICAS                        ║

║  ✓ Entornos de prueba CONTROLADOS                             ║

║                                                                ║

║  El uso NO AUTORIZADO de esta herramienta es ILEGAL y puede   ║### Nombre + Apellido + Fragmento- `new.york` (con punto)python dict-max.py -u target.json -o wordlist.txt# No requiere instalación, solo Python

║  resultar en consecuencias legales graves.                     ║

║                                                                ║```

║  El autor NO se hace responsable del uso indebido de esta     ║

║  herramienta. El usuario es COMPLETAMENTE RESPONSABLE de      ║nicolasmoina1709- `NY` (iniciales mayúsculas)

║  cumplir con todas las leyes aplicables.                       ║

║                                                                ║NicolasMoina170922

║  Requisitos OBLIGATORIOS:                                      ║

║  • Autorización ESCRITA del propietario del sistema           ║nicolas_moina223059- `ny` (iniciales minúsculas)cd dict

║  • Consentimiento EXPLÍCITO de todas las partes involucradas  ║

║  • Cumplimiento de leyes locales e internacionales            ║```

║                                                                ║

╚════════════════════════════════════════════════════════════════╝

```

### Con Símbolos

**Legislación Relevante:**

- 🇪🇨 **Ecuador**: Ley Orgánica de Protección de Datos Personales```**Entrada:** `"Hostal Santa Maria"`  # Con estadísticas y verbosepython wordlist_generator.py

- 🇺🇸 **USA**: Computer Fraud and Abuse Act (CFAA)

- 🇪🇺 **EU**: GDPR - General Data Protection RegulationNicolas@1709, hsmg#170922, Jack.223059

- 🇬🇧 **UK**: Computer Misuse Act 1990

```**Genera:**

---



## 🔄 Changelog

## 🛠️ Integración con Herramientas- `HostalSantaMaria`python dict-max.py -u target.json -o wordlist.txt -v --stats```

### v1.3.0 (2025-10-19)

- ✨ **NUEVO**: Extracción de fragmentos de múltiples longitudes (4, 5, 6, 7, 8 dígitos)

- ✨ **NUEVO**: Uso de TODOS los fragmentos generados en combinaciones

- 🚀 **MEJORA**: Aumento de ~240% en cantidad de passwords generadas### Hydra- `Hostal-Santa-Maria`

- 🚀 **MEJORA**: 186+ combinaciones con palabras clave + fragmentos numéricos

- 🐛 **FIX**: Generación de patrones como "hsmg1709", "hsmg170922"```bash



### v1.2.0 (2025-10-14)# SSH- `Hostal_Santa_Maria`

- ✨ **NUEVO**: Extracción inteligente de fragmentos de cédulas y números largos

- ✨ **NUEVO**: Ventana deslizante para fragmentos de 4, 6 y 8 dígitoshydra -l admin -P wordlist.txt ssh://192.168.1.100

- 🚀 **MEJORA**: Procesamiento de números importantes aumentado 2x

- `hostal.santa.maria`

### v1.1.0 (2025-10-14)

- ✨ **NUEVO**: Procesamiento inteligente de espacios en nombres compuestos# FTP

- ✨ **NUEVO**: Generación de iniciales automática

- 🚀 **MEJORA**: 7 variaciones por cada palabra con espacioshydra -l ftpuser -P wordlist.txt ftp://192.168.1.100- `HSM` (iniciales)# Filtrar longitud 8-16### Uso Básico



### v1.0.0 (2025-10-13)

- 🎉 Lanzamiento inicial

- ✅ CLI profesional con argparse# HTTP Form- Y más variaciones...

- ✅ Generación de wordlists personalizadas

- ✅ 8 fases de generación de passwordshydra -l admin -P wordlist.txt 192.168.1.100 http-post-form "/login:user=^USER^&pass=^PASS^:F=incorrect"

- ✅ Soporte para 9 categorías de información

```python dict-max.py -u target.json -o wordlist.txt --min 8 --max 16

---



## 🤝 Contribuciones

### John the Ripper## 🔧 Patrones Generados

Las contribuciones son bienvenidas! Por favor:

```bash

1. Fork el proyecto

2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)# Básico```bash

3. Commit tus cambios (`git commit -m 'Add: nueva característica'`)

4. Push a la rama (`git push origin feature/AmazingFeature`)john --wordlist=wordlist.txt hash.txt

5. Abre un Pull Request

### 1. Variaciones Básicas

---

# Con reglas (multiplicador de efectividad)

## 📝 Licencia

john --wordlist=wordlist.txt --rules hash.txt```# Ruta personalizadapython wordlist_generator.py

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.



---

# Mostrar crackeadascarlos → carlos, Carlos, CARLOS, solrac (invertida)

## 👤 Autor

john --show hash.txt

**Nicolas**

- GitHub: [@tu-usuario](https://github.com/tu-usuario)``````python dict-max.py -u target.json -o /root/wordlists/custom.txt```

- Email: tu-email@example.com



---

### Hashcat

## 🙏 Agradecimientos

```bash

- Inspirado en herramientas como CeWL, Crunch, y John the Ripper

- Comunidad de seguridad informática y ethical hacking# MD5### 2. Leetspeak```

- Desarrolladores de Python y herramientas de pentesting

hashcat -m 0 -a 0 hash.txt wordlist.txt

---

```

## 📚 Recursos Adicionales

# SHA1

### Herramientas Relacionadas

- [Hydra](https://github.com/vanhauser-thc/thc-hydra) - Herramienta de fuerza brutahashcat -m 100 -a 0 hash.txt wordlist.txtcarlos → c@rlos, c4rlosEl programa presenta un menú interactivo:

- [John the Ripper](https://www.openwall.com/john/) - Password cracker

- [Hashcat](https://hashcat.net/hashcat/) - Advanced password recovery

- [CeWL](https://github.com/digininja/CeWL) - Custom wordlist generator

# SHA256admin  → @dm1n

### Aprendizaje

- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)hashcat -m 1400 -a 0 hash.txt wordlist.txt

- [HackTheBox](https://www.hackthebox.eu/) - Plataforma de práctica

- [TryHackMe](https://tryhackme.com/) - Aprendizaje de ciberseguridadmaria  → m@r1@## 📋 Formato JSON



---# NTLM (Windows)



<div align="center">hashcat -m 1000 -a 0 hash.txt wordlist.txt```



**⭐ Si este proyecto te fue útil, considera darle una estrella! ⭐**



![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)# bcrypt```

![Security](https://img.shields.io/badge/Security-PenTesting-red.svg)

![Status](https://img.shields.io/badge/Status-Active-success.svg)hashcat -m 3200 -a 0 hash.txt wordlist.txt



</div>```### 3. Palabras Compuestas (¡NUEVO!)




### Medusa``````json🔐 GENERADOR DE DICCIONARIOS DE CONTRASEÑAS (WORDLIST GENERATOR)

```bash

# SSHNew York → NewYork, New-York, New_York, NY

medusa -h 192.168.1.100 -u admin -P wordlist.txt -M ssh

Hostal Santa Maria → HostalSantaMaria, HSM{=============================================================================

# RDP

medusa -h 192.168.1.100 -u administrator -P wordlist.txt -M rdp```



# SMB    "nombres": ["Carlos", "Juan"],1.  Agregar Nombres

medusa -h 192.168.1.100 -u admin -P wordlist.txt -M smbnt

```### 4. Combinaciones con Fechas



## 📊 Ejemplo de Salida```    "apellidos": ["Garcia", "Rodriguez"],2.  Agregar Apellidos



```nicolas31082002

======================================================================

    WORDLIST GENERADA EXITOSAMENTENewYork2002    "apodos": ["Carlitos"],3.  Agregar Apodos/Nicknames

======================================================================

📄 Archivo:      wordlist.txtHostalSantaMaria2023

📊 Contraseñas:  4,349

📏 Long. mín:    8 caracteres```    "fechas": ["15081990", "1990"],4.  Agregar Fechas (cumpleaños, aniversarios, etc.)

📏 Long. máx:    20 caracteres

📏 Long. prom:   12 caracteres

💾 Tamaño:       0.06 MB

======================================================================### 5. Nombre + Apellido    "mascotas": ["Max", "Luna"],5.  Agregar Mascotas

[*] Procesados 52 números (incluyendo fragmentos)

```

💡 EJEMPLOS DE USO:

  hydra -l admin -P wordlist.txt ssh://192.168.1.100nicolasmoina, Nicolas_Moina, nicolas-moina    "lugares": ["Madrid", "Barcelona"],6.  Agregar Lugares (ciudad, país, calle, etc.)

  john --wordlist=wordlist.txt hash.txt

  hashcat -m 0 -a 0 hash.txt wordlist.txt```

======================================================================

```    "empresas": ["Google", "Microsoft"],7.  Agregar Empresas/Organizaciones



## 🎓 Mejores Prácticas OSINT### 6. Con Símbolos



### Fuentes de Información```    "palabras_clave": ["futbol", "python"],8.  Agregar Palabras Clave (hobbies, deportes, etc.)



#### Redes SocialesNicolas@123, NewYork#2023, jack.2002

- **Facebook**: Mascotas, familia, lugares, fechas importantes

- **Instagram**: Hobbies, viajes, estilo de vida```    "numeros_importantes": ["123", "456"]9.  Agregar Números Importantes

- **LinkedIn**: Trabajo, educación, certificaciones

- **Twitter**: Intereses, equipos deportivos

- **TikTok**: Contenido personal, gustos

## 🛠️ Uso con Herramientas de Hacking}10. Ver información recopilada

#### Documentos Públicos

- Registros civiles

- Bases de datos públicas

- Páginas web corporativas### Hydra```11. ⭐ GENERAR WORDLIST

- Perfiles profesionales

```bash

### Datos Clave a Recopilar

# SSH12. Cargar información desde JSON

✅ **Fechas de cumpleaños** (objetivo y familiares)  

✅ **Nombres de mascotas** (¡MUY común en contraseñas!)  hydra -l admin -P wordlist.txt ssh://192.168.1.100

✅ **Cédulas/DNI** (completos o parciales)  

✅ **Números de teléfono**  ## 🛠️ Uso con Herramientas13. Guardar información recopilada

✅ **Lugares importantes** (ciudad natal, viajes)  

✅ **Empresas/Organizaciones**  # FTP

✅ **Apodos y nicknames**  

✅ **Equipos deportivos favoritos**  hydra -l admin -P wordlist.txt ftp://192.168.1.1000.  Salir

✅ **Hobbies y pasatiempos**  



### 💡 Tips Profesionales

# HTTP Form```bash```

1. **Números largos**: Siempre incluye cédulas y teléfonos completos en `numeros_importantes`

2. **Fragmentos automáticos**: Dict-Max extraerá automáticamente los fragmentos relevanteshydra -l admin -P wordlist.txt 192.168.1.100 http-post-form "/login:user=^USER^&pass=^PASS^:F=incorrect"

3. **Longitud recomendada**: Usa `--min 8 --max 16` para contraseñas más probables

4. **Combina datos**: Las mejores contraseñas combinan palabra + número (ej: `hsmg170922`)```# Hydra



## 💻 Tips Avanzados



### Combinar Wordlists### John the Ripperhydra -l admin -P wordlist.txt ssh://192.168.1.100## 📝 Categorías de Información



```bash```bash

# Windows PowerShell

Get-Content wordlist1.txt, wordlist2.txt | Sort-Object -Unique > combined.txt# Básico



# Linux/macOSjohn --wordlist=wordlist.txt hash.txt

cat wordlist1.txt wordlist2.txt | sort -u > combined.txt

```# John the Ripper### 1. **Nombres**



### Filtrar por Longitud# Con reglas



```bashjohn --wordlist=wordlist.txt --rules hash.txtjohn --wordlist=wordlist.txt hash.txtNombres del objetivo, miembros de familia, etc.

# Windows PowerShell

Get-Content wordlist.txt | Where-Object { $_.Length -ge 8 -and $_.Length -le 16 } > filtered.txt



# Linux/macOS# Ver crackeadas```

awk 'length >= 8 && length <= 16' wordlist.txt > filtered.txt

```john --show hash.txt



### Estadísticas```# HashcatCarlos, Juan, Maria, Ana



```bash

# Contar líneas (Windows)

(Get-Content wordlist.txt).Count### Hashcathashcat -m 0 -a 0 hash.txt wordlist.txt```



# Contar líneas (Linux)```bash

wc -l wordlist.txt

# MD5

# Ver tamaño del archivo

ls -lh wordlist.txthashcat -m 0 -a 0 hash.txt wordlist.txt

```

# Medusa### 2. **Apellidos**

### Agregar Reglas con John

# SHA256

```bash

# Generar variaciones adicionaleshashcat -m 1400 -a 0 hash.txt wordlist.txtmedusa -h 192.168.1.100 -u admin -P wordlist.txt -M sshApellidos del objetivo y familia

john --wordlist=wordlist.txt --rules --stdout > wordlist_with_rules.txt

```



## 🔒 Seguridad y Ética# NTLM (Windows)``````



### ✅ Uso Permitidohashcat -m 1000 -a 0 hash.txt wordlist.txt

- Auditorías de seguridad contratadas y autorizadas

- Pentesting con permiso explícito por escritoGarcia, Rodriguez, Martinez, Lopez

- Evaluación de sistemas propios

- Educación en entornos controlados# bcrypt



### ❌ Uso Prohibidohashcat -m 3200 -a 0 hash.txt wordlist.txt## 🎯 Patrones Generados```

- Acceso no autorizado a sistemas

- Crackeo de contraseñas sin permiso```

- Violación de privacidad

- Cualquier actividad ilegal



### 📜 Checklist Legal### Medusa



``````bash- Variaciones: `carlos`, `Carlos`, `CARLOS`, `solrac`### 3. **Apodos/Nicknames**

□ Tengo autorización POR ESCRITO del propietario

□ Alcance del test claramente definido# SSH

□ Contrato o acuerdo legal firmado

□ Métodos informados y aprobadosmedusa -h 192.168.1.100 -u admin -P wordlist.txt -M ssh- Leetspeak: `c@rlos`, `m@r1@`Apodos, usernames, alias

□ Registro de todas las actividades

□ Reporte de vulnerabilidades responsable

□ Eliminación de datos post-auditoría

```# RDP- Combinaciones: `carlosgarcia1990`, `Carlos@123````



## 📁 Estructura del Proyectomedusa -h 192.168.1.100 -u administrator -P wordlist.txt -M rdp



``````- Nombre+Apellido+Fecha (muy común en passwords)Carlitos, Juancho, CodeMaster

dict-max/

├── dict-max.py             # Programa principal (20 KB)

├── ejemplo_target.json     # Plantilla (1.1 KB)

├── README.md               # Esta documentación## 📊 Ejemplo de Salida- Miles de variaciones automáticas```

└── RESUMEN.md              # Guía rápida

```



## 🆕 Changelog```



### v1.2.0 (Actual) 🔥======================================================================

- ✨ **Nuevo**: Extracción inteligente de fragmentos de números largos

- ✨ **Nuevo**: Ventana deslizante para cédulas/teléfonos    WORDLIST GENERADA EXITOSAMENTE## 📊 Salida### 4. **Fechas** ⭐ MUY IMPORTANTE

- ✨ **Nuevo**: Genera combinaciones como `hsmg170922` automáticamente

- 🎯 Procesa hasta 50+ fragmentos de números de 10 dígitos======================================================================

- 🇪🇨 Ideal para cédulas ecuatorianas y números de identificación

- ✅ Ejemplo: `1709223059` → `1709`, `170922`, `709223`, `223059`, etc.📄 Archivo:      wordlist.txtFechas de nacimiento, aniversarios, años importantes



### v1.1.0📊 Contraseñas:  4,128

- ✨ Procesamiento inteligente de palabras con espacios

- ✨ Genera variaciones: junto, guión, guión bajo, punto📏 Long. mín:    8 caracteres``````

- ✨ Extrae iniciales de palabras compuestas (HSM, NY)

📏 Long. máx:    20 caracteres

### v1.0.0

- ✅ Lanzamiento inicial📏 Long. prom:   12 caracteres======================================================================15081990    (DDMMYYYY)

- ✅ CLI profesional estilo hacking

- ✅ Banner ASCII épico💾 Tamaño:       0.06 MB

- ✅ Colores ANSI en terminal

======================================================================    WORDLIST GENERADA EXITOSAMENTE1990        (YYYY)

## 📚 Referencias y Recursos



### Herramientas Similares

- [CUPP](https://github.com/Mebus/cupp) - Common User Passwords Profiler💡 EJEMPLOS DE USO:======================================================================150890      (DDMMYY)

- [Crunch](https://sourceforge.net/projects/crunch-wordlist/) - Pattern-based generator

- [CeWL](https://github.com/digininja/CeWL) - Web spider wordlist  hydra -l admin -P wordlist.txt ssh://192.168.1.100

- [Mentalist](https://github.com/sc0tfree/mentalist) - GUI generator

  john --wordlist=wordlist.txt hash.txt📄 Archivo:      wordlist.txt```

### Herramientas de Cracking

- [Hydra](https://github.com/vanhauser-thc/thc-hydra) - Brute force online  hashcat -m 0 -a 0 hash.txt wordlist.txt

- [John the Ripper](https://www.openwall.com/john/) - Hash cracker

- [Hashcat](https://hashcat.net/hashcat/) - GPU cracking======================================================================📊 Contraseñas:  7,195

- [Medusa](http://foofus.net/goons/jmk/medusa/medusa.html) - Parallel brute force

```

### Guías y Documentación

- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)📏 Long. mín:    3 caracteres### 5. **Mascotas**

- [Pentesting Cheat Sheets](https://github.com/coreb1t/awesome-pentest-cheat-sheets)

## 🎓 Tips OSINT

### Plataformas de Práctica

- [HackTheBox](https://www.hackthebox.eu/)📏 Long. máx:    23 caracteresNombres de perros, gatos, etc.

- [TryHackMe](https://tryhackme.com/)

- [PentesterLab](https://www.pentesterlab.com/)### Fuentes de Información

- [VulnHub](https://www.vulnhub.com/)

- **Facebook**: Mascotas, lugares, familiares📏 Long. prom:   11 caracteres```

### Cursos Recomendados

- **OSCP** - Offensive Security Certified Professional- **Instagram**: Hobbies, viajes, fotos

- **CEH** - Certified Ethical Hacker

- **eJPT** - eLearnSecurity Junior Penetration Tester- **LinkedIn**: Trabajo, educación💾 Tamaño:       0.10 MBMax, Luna, Rocky, Bella

- **PNPT** - Practical Network Penetration Tester

- **Twitter**: Intereses, equipos favoritos

## 👤 Autor

======================================================================```

**Nicolas** - Pentester & Security Researcher

### Datos Clave a Buscar

**Version**: 1.2.0  

**Fecha**: Octubre 2025✅ Fechas de cumpleaños  ```



## 📄 Licencia✅ Nombres de mascotas (muy común!)  



MIT License - Uso educativo y profesional autorizado solamente✅ Lugares importantes  ### 6. **Lugares**



---✅ Nombres de empresas  



<p align="center">✅ Apodos y nicknames  ## 📚 Documentación CompletaCiudad natal, país, barrio, calle

  <b>🛡️ Usa esta herramienta de manera ética y responsable</b><br>

  <i>"Con gran poder viene gran responsabilidad"</i>✅ Números de teléfono  

</p>

```

---

## 💡 Tips Avanzados

**⭐ Si te fue útil, considera dar una estrella al proyecto!**

Ver `RESUMEN.md` para documentación detallada.Madrid, Argentina, BuenosAires

### Combinar Wordlists

```bash```

# Windows PowerShell

Get-Content wordlist1.txt, wordlist2.txt | Sort-Object -Unique > combined.txt## 👤 Autor



# Linux### 7. **Empresas/Organizaciones**

cat wordlist1.txt wordlist2.txt | sort -u > combined.txt

```Nicolas - v1.0.0Lugar de trabajo, universidad



### Filtrar por Longitud```

```bash

# Windows PowerShell---Google, Microsoft, UniversidadBA

Get-Content wordlist.txt | Where-Object { $_.Length -ge 8 -and $_.Length -le 16 } > filtered.txt

```

# Linux

awk 'length >= 8 && length <= 16' wordlist.txt > filtered.txt**Uso ético solamente 🛡️**

```

### 8. **Palabras Clave**

### Contar LíneasHobbies, deportes, equipos, películas, juegos

```bash```

# Windowsfutbol, realmadrid, starwars, python

(Get-Content wordlist.txt).Count```



# Linux### 9. **Números Importantes**

wc -l wordlist.txtNúmeros de cédula, teléfono, direcciones

``````

123, 456, 2023, 10

## 🔒 Seguridad y Ética```



### ✅ Uso Permitido## 🔧 Patrones Generados

- Auditorías de seguridad contratadas

- Pentesting autorizado por escritoEl generador crea múltiples patrones automáticamente:

- Sistemas propios

- Educación en entornos controlados### 1. Variaciones de Palabras

```

### ❌ Uso Prohibidocarlos      → Carlos, CARLOS, carlos, solrac

- Acceso no autorizadocarlos      → c@rlos (leetspeak)

- Crackeo sin permiso```

- Violación de privacidad

- Cualquier actividad ilegal### 2. Palabra + Fecha/Número

```

## 📁 Estructura del Proyectocarlos1990, garcia15081990, 1990carlos

Carlos2023, JUAN123, maria@1990

``````

dict-max/

├── dict-max.py             # Programa principal (19 KB)### 3. Nombre + Apellido

├── ejemplo_target.json     # Plantilla (1.1 KB)```

├── README.md               # Este archivocarlosgarcia, CarlosGarcia, carlos_garcia

└── RESUMEN.md              # Guía rápidacarlos.garcia, carlos-garcia

``````



## 🆕 Changelog### 4. Nombre + Apellido + Fecha (Patrón Muy Común)

```

### v1.1.0 (Actual)carlosgarcia1990, JuanMartinez15081990

- ✨ **Nuevo**: Procesamiento inteligente de palabras con espaciosCarlos.Garcia1990, juan_rodriguez2023

- ✨ **Nuevo**: Genera variaciones con guión, guión bajo, punto```

- ✨ **Nuevo**: Extrae iniciales de palabras compuestas

- ✅ Mejoras en la generación de combinaciones### 5. Fechas con Formatos

- ✅ Más de 4,000 contraseñas con datos reales```

15081990 → 15/08/1990, 15-08-1990, 15.08.1990

### v1.0.0```

- ✅ Lanzamiento inicial

- ✅ CLI profesional con argumentos### 6. Combinaciones con Símbolos

- ✅ Banner ASCII```

carlos@2023, garcia#1990, juan.123

## 📚 Referenciaspassword123!, admin@2023

```

- [CUPP](https://github.com/Mebus/cupp) - Similar tool

- [Crunch](https://sourceforge.net/projects/crunch-wordlist/)## 💾 Uso con JSON

- [Hydra](https://github.com/vanhauser-thc/thc-hydra)

- [John the Ripper](https://www.openwall.com/john/)### Crear archivo JSON

- [Hashcat](https://hashcat.net/hashcat/)

Crea un archivo `target_info.json`:

## 👤 Autor

```json

**Nicolas** - v1.1.0{

    "nombres": ["Carlos", "Juan", "Maria"],

---    "apellidos": ["Garcia", "Rodriguez"],

    "fechas": ["15081990", "1990", "2023"],

**Uso ético solamente 🛡️**    "mascotas": ["Max", "Luna"],

    "palabras_clave": ["futbol", "realmadrid", "python"]
}
```

### Cargar desde el programa
```
Opción 12: Cargar información desde JSON
→ Ingresa nombre del archivo: target_info.json
```

## 🛠️ Integración con Herramientas de Pentesting

### Hydra (SSH/FTP/HTTP)
```bash
# SSH
hydra -l usuario -P wordlist_20231015_143022.txt ssh://192.168.1.100

# FTP
hydra -l admin -P wordlist_20231015_143022.txt ftp://192.168.1.100

# HTTP POST
hydra -l admin -P wordlist_20231015_143022.txt 192.168.1.100 http-post-form "/login:user=^USER^&pass=^PASS^:F=incorrect"
```

### John the Ripper
```bash
# Crackear hash
john --wordlist=wordlist_20231015_143022.txt hash.txt

# Con reglas
john --wordlist=wordlist_20231015_143022.txt --rules hash.txt
```

### Hashcat
```bash
# MD5
hashcat -m 0 -a 0 hash.txt wordlist_20231015_143022.txt

# SHA256
hashcat -m 1400 -a 0 hash.txt wordlist_20231015_143022.txt

# NTLM
hashcat -m 1000 -a 0 hash.txt wordlist_20231015_143022.txt
```

### Medusa
```bash
# SSH
medusa -h 192.168.1.100 -u usuario -P wordlist_20231015_143022.txt -M ssh

# RDP
medusa -h 192.168.1.100 -u admin -P wordlist_20231015_143022.txt -M rdp
```

### Ncrack
```bash
ncrack -u admin -P wordlist_20231015_143022.txt ssh://192.168.1.100
```

## 📊 Ejemplo de Salida

```
✅ WORDLIST GENERADA EXITOSAMENTE
=============================================================================
📊 Total de contraseñas únicas: 15,847
=============================================================================

📁 WORDLIST GUARDADA
=============================================================================
📄 Archivo: wordlist_20231015_143022.txt
📊 Total de contraseñas: 15,847
📏 Longitud mínima: 3 caracteres
📏 Longitud máxima: 35 caracteres
📏 Longitud promedio: 12 caracteres
=============================================================================

💡 EJEMPLO DE USO CON HERRAMIENTAS:
   hydra -l usuario -P wordlist_20231015_143022.txt ssh://192.168.1.100
   john --wordlist=wordlist_20231015_143022.txt hash.txt
   hashcat -m 0 -a 0 hash.txt wordlist_20231015_143022.txt
```

## 🎓 Mejores Prácticas para OSINT

### 1. Recopilación de Información
```
✅ Redes Sociales (Facebook, Instagram, LinkedIn, Twitter)
✅ Perfiles profesionales (LinkedIn, GitHub)
✅ Páginas web personales o corporativas
✅ Bases de datos públicas
✅ Google Dorks
```

### 2. Datos Clave a Buscar
```
📌 Fechas de cumpleaños (objetivo, familia)
📌 Nombres de mascotas (muy común en contraseñas)
📌 Equipos deportivos favoritos
📌 Hobbies y pasatiempos
📌 Lugares de nacimiento o residencia
📌 Empresas donde trabaja/trabajó
📌 Universidad/Colegio
📌 Eventos importantes (bodas, graduaciones)
```

### 3. Fuentes de Información
```
🔍 Facebook: Fotos, lugares visitados, gustos
🔍 Instagram: Mascotas, hobbies, viajes
🔍 LinkedIn: Historial laboral, educación
🔍 Twitter: Intereses, opiniones
🔍 GitHub: Proyectos, username
```

## 📁 Estructura de Archivos Generados

```
dict/
├── wordlist_generator.py        # Script principal
├── ejemplo_target.json          # Ejemplo de JSON
├── README_WORDLIST.md           # Este archivo
├── target_info_YYYYMMDD_HHMMSS.json   # Info guardada
└── wordlist_YYYYMMDD_HHMMSS.txt       # Wordlist generada
```

## 🔒 Seguridad y Ética

### ✅ Uso Permitido
- Auditorías de seguridad contratadas
- Pentesting autorizado por escrito
- Evaluación de sistemas propios
- Educación en entornos controlados

### ❌ Uso Prohibido
- Acceso no autorizado a sistemas
- Crackeo de contraseñas sin permiso
- Violación de privacidad
- Cualquier actividad ilegal

### 📜 Recomendaciones
```
1. Obtén autorización por ESCRITO
2. Define el alcance del test
3. Mantén registros de actividades
4. Elimina wordlists después del uso
5. No compartas información del objetivo
6. Reporta vulnerabilidades responsablemente
```

## 💡 Tips Avanzados

### Combinar con otras herramientas
```bash
# Combinar wordlists
cat wordlist1.txt wordlist2.txt | sort -u > wordlist_combined.txt

# Agregar reglas con John
john --wordlist=wordlist.txt --rules --stdout > wordlist_rules.txt

# Filtrar por longitud
awk 'length >= 8 && length <= 16' wordlist.txt > wordlist_filtered.txt
```

### Optimizar wordlist
```bash
# Eliminar duplicados
sort -u wordlist.txt -o wordlist_unique.txt

# Ordenar por frecuencia
cat wordlist.txt | sort | uniq -c | sort -rn > wordlist_sorted.txt

# Contar líneas
wc -l wordlist.txt
```

## 🐛 Troubleshooting

### Problema: "El wordlist es muy grande"
**Solución:** Limita la información o usa menos combinaciones

### Problema: "Muchas contraseñas similares"
**Solución:** El programa elimina duplicados automáticamente

### Problema: "No genera suficientes contraseñas"
**Solución:** Agrega más información del objetivo

## 📚 Referencias y Recursos

### Herramientas Relacionadas
- [CUPP](https://github.com/Mebus/cupp) - Common User Passwords Profiler
- [Crunch](https://sourceforge.net/projects/crunch-wordlist/) - Wordlist Generator
- [CeWL](https://github.com/digininja/CeWL) - Web Spider
- [Mentalist](https://github.com/sc0tfree/mentalist) - GUI Wordlist Generator

### Guías y Documentación
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [Pentesting Labs](https://www.pentesterlab.com/)
- [HackTheBox](https://www.hackthebox.eu/)

### Cursos Recomendados
- OSCP - Offensive Security Certified Professional
- CEH - Certified Ethical Hacker
- eJPT - eLearnSecurity Junior Penetration Tester

## 👤 Autor

**Nicolas**  
Herramienta creada con fines educativos y de seguridad

## 📝 Licencia

MIT License - Uso educativo y profesional autorizado solamente

## 🤝 Contribuciones

Las contribuciones son bienvenidas:
1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/mejora`)
3. Commit cambios (`git commit -m 'Agregar mejora'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

## 📮 Contacto y Soporte

Para reportar bugs o sugerir mejoras, abre un issue en el repositorio.

---

**Recuerda: Usa esta herramienta de manera ética y responsable. 🛡️**

*"Con gran poder viene gran responsabilidad"* - Uncle Ben
