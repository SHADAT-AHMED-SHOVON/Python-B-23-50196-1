user_input = input("Enter number list: ")
numbers = [int(num) for num in user_input.split()]
target = int(input("Target value: "))

found = False
for i in range(len(numbers)):
    if numbers[i] == target:
        found = True
        print("Found")
        break

if not found:
    print("Not Found")