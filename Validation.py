def password_validation(password, re_password):
    # Check length
    if len(password) < 10:
        return False
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    
    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return False
    
    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False
    
    # Check for at least one special character
    special_characters = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
    if not any(char in special_characters for char in password):
        return False
    
    # Check if password matches re-entered password
    if password != re_password:
        return False

    # If all conditions pass, return True
    return True
