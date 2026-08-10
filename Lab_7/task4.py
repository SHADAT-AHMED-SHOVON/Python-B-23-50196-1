file_name = "lab7_demo.txt"

try:
    # 1. Write Mode ('w')
    with open(file_name, "w") as f:
        f.write("Welcome to Python File Handling.\n")
    print("File written successfully.")

    # 2. Append Mode ('a')
    with open(file_name, "a") as f:
        f.write("Adding a new line to the file.\n")
    print("Content appended successfully.")

    # 3. Read Mode ('r')
    with open(file_name, "r") as f:
        content = f.read()
        print("\n--- File Content ---")
        print(content)

    # 4. Exclusive Creation Mode ('x') - handled with try...except
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