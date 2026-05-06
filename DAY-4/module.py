# tools.py

# A few constant values (Variables)
PI = 3.14159
AUTHOR = "Student Explorer"
UNITS = "Metric"

# 1. A math function
def add_numbers(x, y):
    """Returns the sum of two numbers."""
    return x + y

# 2. A string formatter
def shout(text):
    """Returns text in uppercase with exclamation points."""
    return f"{text.upper()}!!!"

# 3. A conversion function (The one we just talked about!)
def meters_to_cm(meters):
    """Converts meters to centimeters."""
    return meters * 100

# 4. A list helper
def get_first_letter(name_list):
    """Returns a list of the first letter of every name provided."""
    return [name[0] for name in name_list]