# 🔐 MPIN Security Evaluator

A smart, human-centered Python application to evaluate the **security strength of MPINs (Mobile PINs)**.  
This project blends **security analysis, clean coding practices, and user experience design** to simulate a **real-world fintech scenario** — exactly the kind of challenge faced in banking and mobile applications.

---

## 🌟 Why This Project?
Mobile PINs (MPINs) are widely used in mobile banking and UPI systems.  
However, many users still choose **weak PINs** (like `1234`, `1111`, or birth years). This project addresses that gap by:

- Checking **common patterns** (sequential, repeated digits).
- Evaluating **demographic biases** (DOB, gender-influenced PINs).
- Supporting **both 4-digit and 6-digit PINs**.
- Explaining *why* a PIN is weak — not just flagging it.

💡 The aim is not only to detect weak MPINs but to **educate users** with clear reasoning.

---

## 📂 Project Structure

📦 mpin-security-evaluator  

┣ 📜 common_checker.py # Detects sequential & repetitive digits

┣ 📜 demographic_check.py # Flags DOB / demographic-based MPINs

┣ 📜 main_mpin_checker.py # Central evaluator

┣ 📜 reason_analysis.py # Explains acceptance/rejection reasons

┣ 📜 part_d_6digit_support.py # Adds 6-digit MPIN support

┣ 📜 mpin_gui_app.py # User-friendly Tkinter GUI

┣ 📜 test_mpin_checker.py # Unit tests for reliability

┗ 📜 README.md # Project documentation



---

## 🚀 Features
- ✅ **4-digit & 6-digit MPIN support**  
- ✅ Detects **weaknesses like `1234`, `0000`, `1212`**  
- ✅ Flags **DOB-based MPINs** (e.g., birth year `1999`)  
- ✅ Explains *why* a PIN is insecure  
- ✅ GUI version for **non-technical users**  
- ✅ Fully **modular & testable**  

---

## ⚙️ Installation & Usage

### 1️⃣ Requirements
- Python **3.7+**
- Tkinter (usually pre-installed)

### 2️⃣ Run from CLI
```bash
python main_mpin_checker.py

3️⃣ Run GUI
python mpin_gui_app.py

🧪 Running Tests
python test_mpin_checker.py

📖 Example Output
Enter your MPIN: 1234
Result: ❌ Weak MPIN
Reason: Sequential digits (1234)

Enter your MPIN: 5793
Result: ✅ Strong MPIN
Reason: No common patterns or demographic bias detected

🌍 Human-Centered Impact

This project is built with a real-world perspective:

Encourages secure digital banking habits.

Provides user education, not just warnings.

Reflects industry practices in security and testing.

👨‍💻 Author

Suraj Kumar
🎓 B.Tech Final Year, NIET
