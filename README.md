# Showoff - A simple sports stats tracker

![Version](https://img.shields.io/badge/version-2.2-blue)
![Build Status](https://github.com/80degree/showoff/actions/workflows/build.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11+-green)
![License](https://img.shields.io/badge/license-GPLv3-orange)
![made with love](https://img.shields.io/badge/made%20with-%3C3-red)

Showoff - a simple app for saving, viewing and exporting sports stats
Currently supports basketball, soccer.

> Showoff uses [CourtCV](https://github.com/80degree/CourtCV)

## Requirements

1. [Python 3](https://www.python.org/downloads/)
2. Weasyprint 
```bash 
pip install weasyprint
```

---

## Running

You can run showoff using [binaries for your system](https://github.com/80degree/showoff/releases/latest) or using the source code.

### Using ready-to-use binaries(recommended)

> Binaries are an already pre-built packages for your system.

1. Download the latest binary files for your system:
   - [Latest Release](https://github.com/80degree/showoff/releases/latest)

2. Unpack the binary in a convenient folder.

3. Launch:
   > Note for Windows users:
   >
   > Windows defender may detect showoff as a malware, so it is recommended to disable defender / add showoff to exceptions
    - **Windows**: Double-click 'showoff.exe'
    - **Linux/macOS**:

      ```bash
      ./showoff.bin
      ```

---

### Using the source code


1. Clone the repository:

   ```bash
   git clone https://github.com/worthyworm/showoff.git
   cd showoff
   ```

2. Run:

   ```bash
   python3 main.py
   ```

---

### Building a binary

If you want to build yours binary:

1. Install Nuitka:

   ```bash
   pip install nuitka
   ```

2. Build:

   ```bash
   python -m nuitka --onefile --standalone --include-package-data=locales main.py
   ```

3. A ready binary will be built in the same folder

---

## Help us with translation

Feel free to help with translating on other languages!
