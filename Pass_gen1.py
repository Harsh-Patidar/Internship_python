# Importing Module
import string
import secrets

# Function
def generate_password(length=12):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Function to generate multiple passwords
def generate_multiple_passwords(num_passwords=1, length=12):
  
    return [generate_password(length) for _ in range(num_passwords)]

# Main program
if __name__ == "__main__":
    try:
        
        password_length = int(input("Enter the desired password length: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        
        if password_length <= 0 or num_passwords <= 0:
            raise ValueError("Length and number of passwords must be positive integers.")


        passwords = generate_multiple_passwords(num_passwords, password_length)
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, start=1):
            print(f"Password {i}: {password}")

    except ValueError as e:
        print(f"Error: {e}")
