import random
import string

def generate_password(length):
    # Define a character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting 'length' characters from the character set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the length of the password: "))
        if password_length <= 0:
            print("Password length must be greater than 0.")
        else:
            generated_password = generate_password(password_length)
            print(f"Generated Password: {generated_password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")
