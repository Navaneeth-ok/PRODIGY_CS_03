# Password Complexity Checker
This Python project is a simple password complexity checker that evaluates the strength of a password based on five criteria: length, uppercase letters, lowercase letters, numbers, and special characters. The complexity of the password is rated as "Very Weak", "Weak", "Moderate", "Strong", or "Very Strong" based on how many of these criteria are met.

## Features
Checks for the following password requirements:
- Length: Minimum of 8 characters.
- Uppercase Letters: At least one uppercase letter.
- Lowercase Letters: At least one lowercase letter.
- Numbers: At least one number.
- Special Characters: At least one special character (e.g., @, #, !, etc.).

Provides a strength rating based on how many of the criteria are met:
- Very Weak: 0–1 criteria met.
- Weak: 2 criteria met.
- Moderate: 3 criteria met.
- Strong: 4 criteria met.
- Very Strong: All 5 criteria met.

## How It Works
The script uses regular expressions to check for the presence of different types of characters in the password. A dictionary tracks the strength based on whether each criterion is met. The sum of the boolean values in the dictionary determines the final complexity score, which is mapped to a specific strength level.
