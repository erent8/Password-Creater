#Eren Terzi

import random
import string

# Create an empty dictionary to store username-password pairs
passwords = {}

# Define a function to generate a random password of a specified length
def generate_password(length=8):
    """Generates a random password of the specified length."""
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return password

# Define a function to save a password for a specified username
def save_password(username, password):
    """Saves a password for the specified username."""
    passwords[username] = password

# Define a function to retrieve the password for a specified username
def get_password(username):
    """Returns the password for the specified username."""
    if username in passwords:
        return passwords[username]
    else:
        return None

# Start an infinite loop that displays a menu of options
while True:
    print("1. Generate Password")
    print("2. Save Password")
    print("3. Get Password")
    print("4. Quit")

    # Prompt the user to enter a choice
    choice = input("Enter choice: ")

    # If the user chooses to generate a password, prompt them for the desired length and call the generate_password function
    if choice == "1":
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print("Generated password:", password)

    # If the user chooses to save a password, prompt them for a username and password and call the save_password function
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        save_password(username, password)
        print("Password saved successfully.")

    # If the user chooses to retrieve a password, prompt them for a username and call the get_password function
    elif choice == "3":
        username = input("Enter username: ")
        password = get_password(username)
        if password:
            print("Password for", username + ":", password)
        else:
            print("Password not found for", username)

    # If the user chooses to quit, break out of the loop
    elif choice == "4":
        break

    # If the user enters an invalid choice, display an error message and loop again
    else:
        print("Invalid choice. Please try again.")
