# Password Manager

A simple command-line password manager that securely stores website credentials using basic encryption.

## Features

- Encrypt passwords using a Caesar cipher
- Store encrypted passwords in a CSV file
- Look up stored passwords (with automatic decryption)
- Add new websites and passwords
- Save and load from password file

## Project Structure

- **main.py**: The main program file with the user interface
- **encryption_utilities.py**: Module containing encryption and file handling functions
- **encryption_utilities_test.py**: Unit tests for the encryption functions
- **samplePasswordFile**: CSV file where encrypted passwords are stored

## How It Works

1. Passwords are encrypted using a Caesar cipher with a key of 16
2. Encrypted passwords are stored in a CSV file along with their associated websites
3. When looking up a password, the program decrypts it using the negative of the encryption key (-16)

## How to Run

To run the password manager:

```bash
python main.py
```

## Running Tests

To run the unit tests for the encryption utilities:

```bash
python -m unittest encryption_utilities_test.py
```

## Usage

The program presents a menu with six options:

1. **Open password file**: Load passwords from a file
2. **Lookup a password**: Find and decrypt a password for a specific website
3. **Add a password**: Add a new website and password (automatically encrypted)
4. **Save password file**: Store the current passwords to a file
5. **Print the encrypted password list**: Display all websites and their encrypted passwords
6. **Quit program**: Exit the application

## Security Note

This is a simple educational project to demonstrate basic encryption concepts. The Caesar cipher is not secure for real-world applications. For actual password management, use established password managers with industry-standard encryption.

## Skills Demonstrated

- File I/O operations with CSV
- Basic encryption techniques
- Unit testing
- Module organization
- Command-line interface design
- Error handling
