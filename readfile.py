def read_and_modify_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\nOriginal Content:\n" + content)

            # Modify content (example: uppercase)
            modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"\nModified content written to: {new_filename}")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except IOError:
        print(f"❌ Error: Could not read the file '{filename}'.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Run the program
read_and_modify_file()
