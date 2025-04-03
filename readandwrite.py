def modify_file():
    """Reads a file, modifies its contents, and writes to a new file."""
    try:
        input_filename = input("Enter the input filename: ")
        output_filename = input("Enter the output filename: ")
        
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been saved to '{output_filename}'")
    except FileNotFoundError:
        print("Error: The specified input file does not exist.")
    except PermissionError:
        print("Error: Permission denied. Unable to access the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Execute the function
if __name__ == "__main__":
    modify_file()
