# List Formatter

A utility that formats a list of items with proper grammar, following English conventions.

## Features

- Formats a list of items with appropriate commas and the word "and"
- Handles edge cases appropriately:
  - Empty list: returns an empty string
  - Single item: returns only that item
  - Two items: joins them with "and"
  - Three or more items: uses commas and adds "and" before the last item

## Example

Input:
```
apple
banana
orange
```

Output:
```
apple, banana, and orange
```

## How to Run

To run the program:

```bash
python list_formatter.py
```

The program will prompt you to enter words one at a time. Press Enter without typing anything to finish entering words and see the formatted result.

## Function Usage

The main function `list_format()` can be imported and used in other programs:

```python
from list_formatter import list_format

items = ["apple", "banana", "orange", "grape"]
formatted_text = list_format(items)
print(formatted_text)  # Outputs: "apple, banana, orange, and grape"
```

## Skills Demonstrated

- String manipulation
- List operations
- User input handling
- Conditional logic
- Function design
