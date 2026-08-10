my_list = [10, 20, 30, 40, 50]

try:
    idx_input = input("Enter list index: ")

    if not idx_input.lstrip('-').isdigit():
        raise TypeError("Index must be an integer.")

    idx = int(idx_input)
    print(f"Element at index {idx}: {my_list[idx]}")

except IndexError:
    print("Error: Index is out of range.")
except TypeError as e:
    print(f"TypeError Caught: {e}")