# Flask 2FA Demo

This is a very simple Flask application that demonstrates 
**Two-Factor Authentication (2FA)** using **TOTP** (Google Authenticator / Microsoft Authenticator).

---

## Features

* Username and password login
* 2FA using a 6-digit authenticator code
* QR code setup for authenticator apps
* Session-based authentication

---

## Requirements

* Python 3.8+
* Flask
* pyotp
* qrcode

---

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install flask pyotp "qrcode[pil]"
```

---

## Run the App

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## Demo Login Credentials

```
Username: admin
Password: password123
```

Scan the QR code with an authenticator app and enter the 6-digit code.

---

## Notes

⚠️ This project is for **learning/demo purposes only**
