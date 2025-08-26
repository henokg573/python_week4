# File Read & Write Challenge 🖋
# Error Handling Lab 
# Henok Girma

def main():
    # Step 1: Ask the user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Step 2: Try to open the file for reading
        with open(filename, "r") as file:
            content = file.read()

        # Step 3: Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Step 4: Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"🎉 Success! File has been read and saved as '{new_filename}'")

    # Step 5: Handle possible errors
    except FileNotFoundError:
        print("❌ Error: The file was not found.")
    except PermissionError:
        print("❌ Error: You do not have permission to open this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
