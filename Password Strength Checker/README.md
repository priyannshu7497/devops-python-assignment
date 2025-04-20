# 🔐 Password Strength Checker

This is a simple Python script to validate the strength of a password based on common security standards. It helps ensure that passwords meet basic security requirements, which is crucial for DevOps and system security.

## ✅ Features

The script checks if the password meets the following criteria:

- Minimum length of 8 characters
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit (0-9)
- Contains at least one special character (e.g., !, @, #, $, %)

## 🛠️ How to Use

1. **Clone the repository or download the script.**
2. Run the script using Python:

```bash
python password_checker.py

Enter a password when prompted, and the script will evaluate its strength and give feedback.

🧪 Example
INPUT

Enter your password to check strength: Hello@123
✅ Password is strong.

OUTPUT

Enter your password to check strength: hello123
Password should contain at least one uppercase letter.
Password should contain at least one special character (e.g., !, @, #, $, %).
❌ Password is weak. Please follow the above suggestions.


Requirements
Python 3.x

📂 File Structure

password_checker/
├── password_checker.py
└── README.md

License
This project is open-source and available for educational and non-commercial use.