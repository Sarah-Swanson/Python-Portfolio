"""
List Formatter

This program formats a list of items with appropriate grammar:
- Separates items with commas
- Adds 'and' before the last item
- Handles edge cases (empty lists, single items, etc.)

Example output:
- [] -> ""
- ["apple"] -> "apple"
- ["apple", "banana"] -> "apple and banana"
- ["apple", "banana", "orange"] -> "apple, banana, and orange"
"""

def list_format(items):
    """
    Format a list of items with proper grammar.
    
    Args:
        items (list): List of strings to format
        
    Returns:
        str: Formatted string with proper grammar
    """
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        return ", ".join(items[:-1]) + ", and " + items[-1]


def main():
    """Main program function to collect items and display the formatted list."""
    listToPrint = []
    
    # Collect words from user until they enter an empty string
    while True:
        newWord = input("Enter a word to add to the list (press return to stop adding words) > ")
        if newWord == "":
            break
        else:
            listToPrint.append(newWord)
    
    # Format and print the list
    formatted_list = list_format(listToPrint)
    print(formatted_list)


if __name__ == "__main__":
    main()
