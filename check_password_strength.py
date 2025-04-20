import re

def check_password_strength(password: str) -> bool:
    # Check minimum length
    if len(password) < 8:
        print("Password should be at least 8 characters long.")
        return False

    # Check for uppercase and lowercase letters
    if not re.search(r'[A-Z]', password):
        print("Password should contain at least one uppercase letter.")
        return False
    if not re.search(r'[a-z]', password):
        print("Password should contain at least one lowercase letter.")
        return False

    # Check for digits
    if not re.search(r'\d', password):
        print("Password should contain at least one digit.")
        return False

    # Check special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("Password should contain at least one special character (e.g., !, @, #, $, %).")
        return False

    # If checks pass
    return True

# Main script
if __name__ == "__main__":
    user_password = input("Enter your password to check strength: ")

    if check_password_strength(user_password):
        print("Password is strong.")
    else:
        print("Password is weak. Please follow the above suggestions.")
