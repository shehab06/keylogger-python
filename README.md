# 🛡️ Python Keylogger  

A **lightweight keylogger** built in Python using `pynput`. It **logs keystrokes** at regular intervals.  

⚠ **Disclaimer:** This script is for **educational and ethical hacking purposes only**.  
Unauthorized keylogging is illegal. Do not misuse it.  

---

## **🔧 Features**  
✔ Logs all keystrokes **silently**.  
✔ Saves logs locally in `keylog.txt`.    
✔ Works on **Windows, macOS, and Linux**.  
✔ Can run in the **background** as an executable.  

---

## **🚀 Installation & Setup**  

### **1️⃣ Install Dependencies**  
Run the following command to install required libraries:  
```bash
pip install pynput
```

### **2️⃣ Run the Keylogger**  
Execute the script using:  
```bash
python keylogger.py
```

---

## **📜 How It Works**  
- **Listens for keystrokes** and stores them in `keylog.txt`.  
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
