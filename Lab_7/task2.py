try:
    val1 = input("Enter first number: ")
    val2 = input("Enter second number: ")

    if not (val1.replace('.', '', 1).isdigit() and val2.replace('.', '', 1).isdigit()):
        raise TypeError("Inputs are not numerical.")

    num1 = float(val1)
    num2 = float(val2)
    print(f"Sum: {num1 + num2}")

except TypeError as e:
    print(f"TypeError Caught: {e}")