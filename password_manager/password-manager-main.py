"""
Password Manager

A simple password manager that:
- Encrypts passwords using a Caesar cipher
- Stores encrypted passwords in a CSV file
- Allows lookup of stored passwords

Features:
- Add new passwords (encrypting them)
- Look up existing passwords (decrypting them)
- Save passwords to a file
- Load passwords from a file
"""

import sys
from encryption_utilities import passwordEncrypt, loadPasswordFile, savePasswordFile

def main():
    """Main program function for the password manager."""
    
    # The password list - We start with it populated for testing purposes
    passwords = [["yahoo", "XqffoZeo"], ["google", "CoIushujSetu"]]

    # The password file name to store the passwords to
    passwordFileName = "samplePasswordFile"

    # The encryption key for the caesar cipher
    encryptionKey = 16

    while True:
        # Display menu options
        print("What would you like to do:")
        print(" 1. Open password file")
        print(" 2. Lookup a password")
        print(" 3. Add a password")
        print(" 4. Save password file")
        print(" 5. Print the encrypted password list (for testing)")
        print(" 6. Quit program")
        print("Please enter a number (1-6)")
        choice = input()

        # Option 1: Load the password list from a file
        if(choice == '1'):
            passwords = loadPasswordFile(passwordFileName)
            print(f"Passwords loaded from {passwordFileName}")

        # Option 2: Lookup a password
        if(choice == '2'):
            print("Which website do you want to lookup the password for?")
            for keyvalue in passwords:
                print(keyvalue[0])
            passwordToLookup = input()

            # Search for the website in the password list
            for keyvalue in passwords:
                if keyvalue[0] == passwordToLookup:
                    encryptedPassword = keyvalue[1]
                    # Decrypt the password using a negative key
                    decryptedPassword = passwordEncrypt(encryptedPassword, -encryptionKey)
                    print(f"The password for {passwordToLookup} is: {decryptedPassword}")
                    break
            else:
                print("Website not found.")

        # Option 3: Add a new password
        if(choice == '3'):
            print("What website is this password for?")
            website = input()
            print("What is the password?")
            unencryptedPassword = input()

            # Encrypt the password
            encryptedPassword = passwordEncrypt(unencryptedPassword, encryptionKey)

            # Create a new password entry
            newPasswordEntry = [website, encryptedPassword]

            # Add the new entry to the password list
            passwords.append(newPasswordEntry)
            print("Password added successfully.")

        # Option 4: Save the passwords to a file
        if(choice == '4'):
            savePasswordFile(passwords, passwordFileName)
            print(f"Passwords saved to {passwordFileName}")

        # Option 5: Print out the password list (encrypted)
        if(choice == '5'):
            print("Encrypted password list:")
            for keyvalue in passwords:
                print(', '.join(keyvalue))

        # Option 6: Quit the program
        if(choice == '6'):
            print('Program stopped.')
            sys.exit()

        # Add blank lines for readability
        print()
        print()


if __name__ == "__main__":
    main()
