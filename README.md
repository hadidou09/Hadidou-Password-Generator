# 🔐 Password Generator & Strength Checker (Python)

A Python-based cybersecurity utility that allows users to **generate secure passwords** and **check password strength** using clear security principles.

This project is designed as a **first real-world cybersecurity programming project**, focusing on correctness, security, and modular design.

---

## 📌 Features

### ✅ Password Generation
- Generate **single passwords** or **lists of passwords**
- Option to include or exclude **symbols**
- Option to set a **fixed length** or allow **random length**
- Uses Python’s `secrets` module for **cryptographically secure randomness**

### ✅ Password Strength Checking
- Check the strength of a **single password**
- Check the strength of a **list of passwords from a `.txt` file**
- Strength is evaluated based on:
  - Length (minimum 8 characters)
  - Presence of:
    - Uppercase letters
    - Lowercase letters
    - Digits
    - Symbols

---

## 🧠 Project Structure


### Modules overview:
- **main.py**
  - User interface (CLI)
  - Handles user choices and input validation

- **Password_Generation_Algorithm.py**
  - Secure password generation logic
  - Uses `secrets` for randomness

- **Password_Checking_Algorithm.py**
  - Password strength evaluation logic
  - Supports single passwords and password lists

---

## 🔒 Security Notes

- The project uses `secrets` instead of `random`, making it suitable for **security-related use cases**
- Password strength is evaluated using common security best practices
- This project is for **educational and learning purposes**, not production deployment

---

## ▶️ How to Run

Make sure you have **Python 3.8+** installed.

```bash
python main.py
