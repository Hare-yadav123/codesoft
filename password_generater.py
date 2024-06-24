import random
import string

def generate_password(length=12):
    """Generate a random password with a given length."""
    if length < 4:  # Ensure the password length is at least 4
        raise ValueError("Password length should be at least 4 characters")
    
    # Define the character sets to use in the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Ensure the password has at least one character from each set
    all_characters = lowercase + uppercase + digits + punctuation
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length-4)

    # Shuffle the password list to avoid any predictable patterns
    random.shuffle(password)

    # Convert the list to a string and return it
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    print("Generated password:", generate_password(12))
