# File Read & Write with Error Handling in Python

# Prompt the user for the filename they want to read
filename = input("Please enter the name of the file you'd like to read: ")

try:
    # Try opening the file in read mode
    with open(filename, 'r') as file:
        content = file.read()

    # Modify the content - for simplicity, let's turn everything to uppercase
    modified_content = content.upper()

    # Prepare the name for the new file
    new_filename = "modified_" + filename

    # Try writing the modified content to a new file
    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)

    print(f"Success! The modified content has been saved to '{new_filename}'.")

except FileNotFoundError:
    print(f"Oops! The file '{filename}' doesn't exist. Double-check the name and try again.")

except PermissionError:
    print(f"Uh-oh! You don’t have permission to access '{filename}'. Make sure you have the right permissions.")

except IOError:
    print(f"Something went wrong while trying to read or write to '{filename}'. It could be an I/O issue.")

except Exception as e:
    # If there's some other error, print it out
    print(f"An unexpected error occurred: {e}")
