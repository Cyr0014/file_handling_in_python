# file_handling_assignment.py

def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("This is the first line.\n")
            file.write("12345\n")
            file.write("Another line of text.\n")
        print("File created and initial lines written.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("Reading the file content:\n")
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Appending another line.\n")
            file.write("67890\n")
            file.write("Final line of text.\n")
        print("Additional lines appended to the file.")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()

if __name__ == "__main__":
    main()
