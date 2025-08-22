# 🖥️ AI Auto Refresh for Freelancer

An automation tool that uses **Google Gemini AI** + **PyAutoGUI** to simulate human-like browsing activity by detecting clickable elements on screen and interacting with them.  
This can help keep freelance work platforms or similar web apps active by mimicking natural user behavior (clicks, scrolling, idle time, and tab switching).

---

## ✨ Features
- 📸 **Smart Screenshotting** – Captures the screen and analyzes it with Google Gemini AI.  
- 🎯 **Clickable Element Detection** – Uses AI to return bounding boxes of buttons, links, or menus.  
- 🖱️ **Human-like Interaction** – Randomized, smooth mouse movements and clicks.  
- 🔄 **Randomized Scrolling & Idling** – Mimics natural user activity.  
- 🌐 **Multi-tab Support** – Automatically switches between tabs with `Ctrl + Tab`.  
- ♾️ **Continuous Loop** – Runs indefinitely, refreshing activity across tabs.  

---

## ⚙️ Requirements
Make sure you have Python 3.9+ installed. Install the dependencies:

```bash
pip install pyautogui pillow google-generativeai
```

---

## 🔑 Configuration
Create a `config.json` file in the project root with your **Google Gemini API key**:

```json
{
  "api_key": "YOUR_API_KEY_HERE"
}
```

---

## 🚀 Usage
Run the script:

```bash
python main.py
```

It will:
1. Take a screenshot of your screen.  
2. Ask Gemini AI to find clickable elements.  
3. Randomly interact with them in a human-like manner.  
4. Switch between browser tabs automatically.  

---

## 📂 Project Structure
```
AI_auto_refresh_for_freelancer/
│-- main.py         # Core script
│-- config.json     # API key configuration (ignored in .gitignore)
│-- README.md       # Documentation
```

---

## ⚠️ Disclaimer
This project is intended for **educational and personal use only**.  
Automating interactions on freelance platforms may violate their **terms of service** — use responsibly and at your own risk.  
