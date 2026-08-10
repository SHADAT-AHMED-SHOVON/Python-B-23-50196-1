file_name = "lab7_demo.txt"

try:
    with open(file_name, "w") as f:
        f.write("Welcome to Python File Handling.\n")
    print("File written successfully.")

    with open(file_name, "a") as f:
        f.write("Adding a new line to the file.\n")
    print("Content appended successfully.")

    with open(file_name, "r") as f:
        content = f.read()
        print("\n--- File Content ---")
        print(content)

    try:
        with open("new_created_file.txt", "x") as f:
            f.write("Newly created file.\n")
        print("Exclusive file created successfully.")
    except FileExistsError:
        print("File already exists!")

except FileNotFoundError:
    print("Error: Specified file not found.")
except IOError as e:
    print(f"I/O Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")