import re

def check_password_strength(password):
    """Check the strength of a given password."""
    # Common weak passwords list (abbreviated for example)
    common_passwords = ['password', '123456', 'qwerty', 'letmein']
    
    # Check against common passwords
    if password.lower() in common_passwords:
        return "Very Weak: This is a commonly used password."
    
    # Length check
    length = len(password)
    if length < 8:
        return "Weak: Password should be at least 8 characters long."
    elif length >= 12:
        length_score = 2
    else:
        length_score = 1
    
    # Check for character variety
    checks = {
        'uppercase': re.search(r'[A-Z]', password),
        'lowercase': re.search(r'[a-z]', password),
        'digit': re.search(r'\d', password),
        'special': re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    }
    
    # Calculate score based on met criteria
    criteria_met = sum(1 for check in checks.values() if check)
    total_score = length_score + criteria_met
    
    # Determine strength
    if total_score >= 5:
        return "Strong: Good job! This is a secure password."
    elif total_score >= 3:
        return "Moderate: Consider adding more character types (uppercase, digits, symbols)."
    else:
        return "Weak: Password is too simple. Increase length and variety of characters."

# Example usage
if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    result = check_password_strength(user_password)
    print(result)
