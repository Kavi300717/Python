# Python Alarm Clock ⏰

A simple Python script to set an alarm based on **date** and **time**.  
When the current system time matches the alarm time, it will either:

- Play a **music file** (e.g., `.wav`)
- Or trigger a **beep sound** (Windows only, using `winsound`)

---

## 📌 Features
- Set alarm for a **specific date and time**.
- Choose between:
  - **Music alarm** (`playsound` / `pygame`)
  - **Beep alarm** (`winsound`, Windows only)
- Works in **12-hour format (HH:MM, AM/PM)**.

---

## ⚙️ Requirements
- Python 3.10+ (tested with Python 3.12)
- Libraries:
  - `playsound` *(may not work on Python 3.12, use alternatives)*
  - `winsound` *(built-in, Windows only)*
  - Alternatively: `pygame` or `simpleaudio` for better playback

---

## 📥 Installation
1. Clone or download the script.
2. Install required libraries:

```bash
pip install pygame
