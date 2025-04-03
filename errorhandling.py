#Question 2

def get_valid_filename(prompt):
    """Prompt the user for a valid filename until a valid file is provided."""
    while True:
        filename = input(prompt)
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return filename
        except FileNotFoundError:
            print("Error: The specified file does not exist. Please try again.")
        except PermissionError:
            print("Error: Permission denied. Unable to access the file. Try a different file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def modify_file():
    """Reads a file, modifies its contents, and writes to a new file."""
    input_filename = get_valid_filename("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")

    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been saved to '{output_filename}'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Execute the function
if __name__ == "__main__":
    modify_file()
