# Make a class. 

# Logic that checks a password and returns a rating (very weak - weak - medium - strong - very strong). 
# length, alphanumic, special chars.... 
# check against a list of common password - if matches should be very weak. 
# object to call a method that checks (object will pass through the password)

# Import the string module for useful constants
import string

# class to encapsulate 
class PasswordChecker:
    # List of common passwords
    common_passwords = [
        "123456", "password", "123456789", "12345678", "12345", 
        "1234567", "qwerty", "abc123", "letmein", "111111",
        "000000", "password1", "password123"
    ]
    
    def __init__(self, password):
        self.password = password
    
    def check_password(self):
        # Check if the password matches any common passwords 
        if self.password in PasswordChecker.common_passwords:
            return "Very Weak"
        
        # Criteria for password strength
        length = len(self.password)
        has_lower = any(char.islower() for char in self.password)
        has_upper = any(char.isupper() for char in self.password)
        has_digit = any(char.isdigit() for char in self.password)
        has_special = any(char in string.punctuation for char in self.password)
        
        # Determines strength based on criteria
        if length < 6:
            return "Very Weak"
        elif length >= 6 and (has_lower or has_upper) and not has_digit and not has_special:
            return "Weak"
        elif length >= 8 and has_lower and has_upper and has_digit and not has_special:
            return "Medium"
        elif length >= 10 and has_lower and has_upper and has_digit and has_special:
            return "Strong"
        elif length >= 12 and has_lower and has_upper and has_digit and has_special:
            return "Very Strong"
        else:
            return "Weak"

# # Example passwords
# password1 = PasswordChecker("12345")
# print(password1.check_password())  # Output: Very Weak

# password2 = PasswordChecker("Secure123!")
# print(password2.check_password())  # Output: Strong

# password3 = PasswordChecker("Pa$$w0rd12345")
# print(password3.check_password())  # Output: Very Strong

# password4 = PasswordChecker("password213")
# print(password4.check_password())  # Output: Weak


