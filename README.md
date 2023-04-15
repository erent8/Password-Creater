# Password Creater
![Ekran görüntüsü 2023-04-15 233143](https://user-images.githubusercontent.com/86615310/232252068-39b178ee-24b0-4f66-ac7e-72aa02bec78d.png)


This code is a simple console application that allows users to manage their passwords using Python. The code enables users to create new passwords, save them, and retrieve them later.

First, the random and string modules are imported, which are necessary for generating random passwords. A blank dictionary called passwords is also defined, which serves as storage space for usernames and passwords.

Next, three different functions are defined:

generate_password: Generates a random password of a specified length.
save_password: Saves a username and password combination.
get_password: Retrieves a saved password for a username.
A while loop allows the user to make a choice. The options are:

Select "1" to generate a new password. This option generates a random password of the requested length and prints it to the screen.
Select "2" to save a password. This option prompts the user for a username and password combination and saves this information in the passwords dictionary.
Select "3" to retrieve a saved password. This option prompts the user for a username and retrieves the password from the passwords dictionary, printing it to the screen.
Select "4" to exit the program. This option breaks out of the while loop and ends the program.
An if-elif-else structure is used to ensure that the user enters a valid choice. If an invalid choice is entered, the program displays the list of options again.

In this way, users can manage and store their passwords. However, this code is only an example and is not sufficient for real-world password management applications. Real password management applications require stronger password generation algorithms, more secure methods of encrypting and storing passwords, and additional security measures such as authentication.

