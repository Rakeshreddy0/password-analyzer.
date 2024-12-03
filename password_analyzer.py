import re

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    return strength

password = input("Enter a password: ")
strength = check_password_strength(password)
strength_labels = ["Weak", "Moderate", "Strong", "Very Strong", "Excellent"]
print(f"Password Strength: {strength_labels[strength-1]} (Score: {strength}/5)")
