def modify_content(text):
    # Example modification: convert all text to uppercase
    return text.upper()

def main():
    # Ask the user for the input filename
    input_filename = input("Enter the filename to read from: ")

    try:
        # Try to open and read the file
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_content(content)

        # Ask for a new output filename
        output_filename = input("Enter the filename to write to: ")

        # Write the modified content to the new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"File '{output_filename}' has been created with modified content.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write the file.")

if __name__ == "__main__":
    main()