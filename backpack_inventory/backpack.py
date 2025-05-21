"""
Backpack Inventory Manager

A simple inventory management system that allows users to:
1. Add items to a virtual backpack
2. Check if specific items are in the backpack
3. Exit the program

The program maintains a list of items and provides a command-line interface.
"""

import sys

def main():
    """Main program function that handles the backpack inventory."""
    
    # Initial items in the backpack
    itemsInBackpack = ["book", "computer", "keys", "travel mug"]

    # Main program loop
    while True:
        # Display menu options
        print("Would you like to:")
        print("1. Add an item to the backpack?")
        print("2. Check if an item is in the backpack?")
        print("3. Quit")
        userChoice = input()

        # Option 1: Add an item to the backpack
        if (userChoice == "1"):
            print("What item do you want to add to the backpack?")
            itemToAdd = input()
            
            # Add the item to the backpack
            itemsInBackpack.append(itemToAdd)
            print(f"{itemToAdd} has been added to the backpack.")

        # Option 2: Check if an item is in the backpack
        if (userChoice == "2"):
            print("What item do you want to check to see if it is in the backpack?")
            itemToCheck = input()
            
            # Check if the item is in the backpack
            if itemToCheck in itemsInBackpack:
                print(f"{itemToCheck} is in the backpack.")
            else:
                print(f"{itemToCheck} is not in the backpack.")

        # Option 3: Exit the program
        if (userChoice == "3"):
            print("Goodbye!")
            sys.exit()
        
        # Add a blank line for readability
        print()


if __name__ == "__main__":
    main()
