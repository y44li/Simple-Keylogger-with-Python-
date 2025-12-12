# Python Keylogger

This project is an **educational keylogging tool** built with Python.  
It demonstrates how keystroke monitoring works internally, including:

- Capturing keyboard events
- Handling special keys and numpad keys
- Logging keystrokes to a file
- Sending logs to a remote server (Telegram Bot API)
- Using background threads for periodic reporting

⚠️ **Disclaimer:**  
This project is for **learning, cybersecurity research, and personal experimentation only**.  
Do NOT use this tool on devices you do not own or do not have explicit permission to test.

---

## Features

- ✔️ Captures normal character keys  
- ✔️ Logs special keys (e.g., `[enter]`, `[space]`)  
- ✔️ Correctly handles **numpad numbers (0–9)** using virtual-key (`vk`) codes  
- ✔️ Saves keystrokes to a local log file  
- ✔️ Background thread sends logs every 30 seconds  
- ✔️ Sends logs to Telegram using a bot  
- ✔️ Automatically clears log file after sending  

---

## Requirements

- Python 3.x  
- Modules:
  - `pynput`
  - `requests`
  - `threading` 
  - `time` 
  - `os` 

# How It Works
1. Keyboard Listener
   The listener captures every keypress through:

with keyboard.Listener(on_press=OnPress):
    listener.join()

## 2. Improved Keystroke Handling

The script handles:
key.char for printable keys
key.vk for numpad keys (VK 96–105 → digits 0–9)
Key.* for special keys

## 3. Logging

All keystrokes are appended to a local file:
LOG_FILE = "path_to_file"

## 4. Automatic Reporting

A background thread checks the log every 30 seconds:
Reads content
Sends it via Telegram
Deletes the file

# Sending Logs With Telegram

To use Telegram reporting:
Create a bot using @BotFather
Get your bot token
Get your chat ID using:
https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates

Insert them in the script:
telegram_bot_token = "YOUR_TOKEN"
chatID = "YOUR_CHAT_ID"

# Useful resources 
🔹 pynput numpad issue explanation
Stack Overflow: Detecting numpad keys with pynput keyboard
https://stackoverflow.com/questions/58478060/detecting-numpad-keys-with-pynput-keyboard

🔹 pynput official GitHub issue (missing .char for numpad keys)

"Numpad Return None" – documenting that numpad keys often return no .char
https://github.com/moses-palmer/pynput/issues/370

🔹 General pynput tutorial (keyboard listener basics)
https://nitratine.net/blog/post/how-to-detect-key-presses-in-python/

