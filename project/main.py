from pynput import keyboard

def on_press(key):
    try:
        print('{0}'.format(key.char))
    except AttributeError:
        print('{0}'.format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        return False


listener = keyboard.Listener(on_press = on_press, on_release = on_release)
listener.start()
listener.join()
