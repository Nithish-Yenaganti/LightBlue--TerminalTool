# Light Blue

Light Blue is an educational terminal-based cybersecurity simulator built in Python. It teaches basic password safety, password auditing, and phishing URL scanning concepts without performing real offensive activity.

> Educational use only. This project simulates security workflows and should not be used as an offensive tool.

## Features

- Password breach check using Have I Been Pwned k-anonymity
- Password strength and entropy auditing
- Phishing URL scan flow using VirusTotal
- Terminal UI with color and ASCII banner output

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Add your VirusTotal API key to `.env` if you want phishing scan support:

```text
VT_API_KEY=your_virustotal_key
```

## Run From Source

```bash
python -m light_blue.main
```

## Install As A CLI

```bash
pip install -e .
lightblue
```

## Project Structure

```text
light_blue/main.py               # Menu and app entrypoint
light_blue/passwordChecker.py    # Breach check flow
light_blue/passwordAuditor.py    # Password strength flow
light_blue/phishing_detector.py  # VirusTotal URL scan flow
requirements.txt                 # Runtime dependencies
setup.py                         # Local package metadata
```
