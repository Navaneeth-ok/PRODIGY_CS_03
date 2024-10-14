import re

def check_password_complexity(password):
    # Initialize strength variables
    strength = {
        'length': False,
        'uppercase': False,
        'lowercase': False,
        'number': False,
        'special_char': False
    }

    # Check for length (at least 8 characters)
    if len(password) >= 8:
        strength['length'] = True

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength['uppercase'] = True

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength['lowercase'] = True

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength['number'] = True

    # Check for special characters
    if re.search(r'[\W_]', password):  
        strength['special_char'] = True

   
    complexity_score = sum(strength.values())
    
    if complexity_score == 5:
        return "Very Strong"
    elif complexity_score == 4:
        return "Strong"
    elif complexity_score == 3:
        return "Moderate"
    elif complexity_score == 2:
        return "Weak"
    else:
        return "Very Weak"


password = input("Enter a password: ")
result = check_password_complexity(password)
print(f"Password Strength: {result}")
