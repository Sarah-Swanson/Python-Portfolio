"""
Encryption Utilities

This module provides utility functions for password encryption and file handling.
It implements a Caesar cipher for password encryption and provides
functions to save and load passwords from CSV files.
"""

import csv

def passwordEncrypt(unencryptedMessage, key):
    """
    Encrypt a message using a Caesar cipher.
    
    Args:
        unencryptedMessage (str): The message to encrypt
        key (int): The encryption key (shift value)
        
    Returns:
        str: The encrypted message
    """
    # We will start with an empty string as our encryptedMessage
    encryptedMessage = ''

    # For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol

    return encryptedMessage


def loadPasswordFile(fileName):
    """
    Load passwords from a CSV file.
    
    Args:
        fileName (str): The name of the file to load
        
    Returns:
        list: A list of [website, encrypted_password] pairs
    """
    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList


def savePasswordFile(passwordList, fileName):
    """
    Save passwords to a CSV file.
    
    Args:
        passwordList (list): A list of [website, encrypted_password] pairs
        fileName (str): The name of the file to save to
    """
    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)
