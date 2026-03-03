# Showoff - A simple sports stats tracker

![Version](https://img.shields.io/badge/version-2.1.0-blue)
![Python](https://img.shields.io/badge/python-3.9+-green)
![License](https://img.shields.io/badge/license-MIT-orange)
![made with love](https://img.shields.io/badge/made%20with-%3C3-red)

> **Versions below v2.0.0 are temporarily not-supported. Stay tuned for updates!**

Showoff is a simple sports self-statistics tracker for players or their coaches, written to be easy to use and to be informational.
Currently supports basketball, soccer.
You can also offer your sport, or help with existing ones

## Requirements

1. [Python 3](https://www.python.org/downloads/)

---

## Running

You can run showoff using [binaries for your system](https://github.com/worthyworm/showoff/releases/latest) or using the source code.

### Using ready-to-use binaries(recommended)

> Binaries are an already pre-built packages for your system.

### Binaries status

| Platform | Latest Status               | Latest Uploaded    |
|----------|-----------------------------|--------------------|
| Windows  | Awaits building             | v2.0.0             |
| Linux    | Ready ✅                    | v2.1.0             |
| macOS    | Ready ✅                    | v2.1.0             |

1. Download the latest binary files for your system:
   - [Latest Release](https://github.com/worthyworm/showoff/releases/latest)

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
   python3 source/main.py
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
   python -m nuitka --onefile --standalone --include-package-data=locales source/main.py
   ```

3. A ready binary will be built in the same folder

---

## Help us with translation

Feel free to help with translating on other languages!
