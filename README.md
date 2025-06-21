
# EKG Signal Tester — Qt + PySide6 Interface

A cross-platform PySide6 GUI that connects to a microcontroller (e.g. STM32) over UART to send EKG signal buffers and receive results from an embedded NanoEdge AI model in real time.

This tool is designed for development, testing, and debugging of anomaly detection models using actual or synthetic EKG data.

## the partner microcontroller project that uses the NanoEdge Studio creates AI lib is here:
https://github.com/stevemac321/NanoEdgeAIDemo

---

## 🛠 Features

- **Serial (UART) signal injection** with COM port + baud rate selection
- **Normal / Anomaly buffer selection**
- **Similarity + status result display from microcontroller**
- **Manual console clear button** for persistent log visibility
- Built to work **across platforms** (Windows, macOS, Linux) using **PySide6**

---

## 📁 File Structure

```
EKG/
├── signals/
│   ├── regular.csv     # Normal signals (140 comma-delimited floats per row)
│   └── anomaly.csv     # Anomaly signals
├── ui_form.py          # UI class (generated from Qt Designer `.ui` file)
├── widget.py           # Main application logic
└── README.md           # You're here!
```

---

## 📦 Requirements

- Python 3.10 or later
- PySide6
- pandas, numpy, pyserial

Install dependencies with:

```bash
pip install -r requirements.txt
```

Generate the UI form if not already present:

```bash
pyside6-uic form.ui -o ui_form.py
```

---

## 🧭 Usage Per Platform

> ⚠️ **Note:** This app uses a virtual environment created locally. You'll need to activate it (or install dependencies globally) on each platform where you run it.

---

### 🪟 Windows (PowerShell)

```powershell
cd C:\repos\EKG
.\.qtcreator\Python_3_10_64_bit_venv\Scripts\Activate.ps1
python widget.py
```

You may also create a `start.ps1` file:

```powershell
# start.ps1
.\.qtcreator\Python_3_10_64_bit_venv\Scripts\Activate.ps1
python widget.py
```

---

### 🍎 macOS

```bash
cd ~/repos/EKG
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python widget.py
```

Make sure you have Python 3.10+ installed (via Homebrew or pyenv).

---

### 🐧 Linux

```bash
cd ~/repos/EKG
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python widget.py
```

You may need extra system packages like:

```bash
sudo apt install libxcb-cursor0
```

---

## ⚙️ Notes

- Each signal sample must be **140 float values per row**, comma-separated
- The microcontroller should return **2 bytes**: status and similarity
- Flask/HTTP inference is **not used in this version**, but the structure allows for future server testing if re-enabled
- You’ll need to **build and configure this app independently on each platform**, including setting up any virtual environment and ensuring hardware access permissions (e.g. serial port)

License: GPL v.2
