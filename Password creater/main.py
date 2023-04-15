import random
import string

passwords = {}

def generate_password(length=8):
    """Generates a random password of the specified length."""
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return password

def save_password(username, password):
    """Saves a password for the specified username."""
    passwords[username] = password

def get_password(username):
    """Returns the password for the specified username."""
    if username in passwords:
        return passwords[username]
    else:
        return None

while True:
    print("1. Generate Password")
    print("2. Save Password")
    print("3. Get Password")
    print("4. Quit")
    choice = input("Enter choice: ")

    if choice == "1":
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print("Generated password:", password)

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        save_password(username, password)
        print("Password saved successfully.")

    elif choice == "3":
        username = input("Enter username: ")
        password = get_password(username)
        if password:
            print("Password for", username + ":", password)
        else:
            print("Password not found for", username)

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please try again.")
