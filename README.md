
# Dynamic Enum List

## Overview

`Dynamic Enum List` is a Python class that provides a dynamic way to create and manage enumerations. It allows you to add and remove members dynamically while maintaining easy access to the enum values.

## Features

- **Dynamic Member Management**: Easily add or remove enum members at runtime.
- **Dictionary-like Iteration**: Iterate through the enum members as key-value pairs.
- **Easy Value Retrieval**: Access the values of enum members directly through attributes.

## Installation

You can clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/dynamic-enum-list.git
```

## Usage

Here's a simple example of how to use the `CreateDynamicEnumList` class:

```python
from your_module import CreateDynamicEnumList

# Create an instance with initial colors
Color = CreateDynamicEnumList("Color", {
    "RED": "red",
    "GREEN": "green",
    "BLUE": "blue",
    "GRAY": "gray"
})

# Add a new color
Color.add("BLACK", "black")

# Access enum values directly
print(Color.RED)  # Output: red

# Iterate through enum members
for color in Color:
    print(color)  # Output: {'RED': 'red'}, {'GREEN': 'green'}, etc.

# Remove a color
Color.remove("RED")
```

## Methods

- `__init__(self, name, dictionary)`: Initializes the enum list with a name and a dictionary of initial values.
- `add(key, value)`: Adds a new key-value pair to the enum.
- `remove(key)`: Removes a key from the enum.
- `__getattr__(self, item)`: Retrieves the value of an enum member by its name.
- `__iter__(self)`: Allows iteration over the enum members as dictionaries.
- `__repr__(self)`: Returns a string representation of the enum list.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.
