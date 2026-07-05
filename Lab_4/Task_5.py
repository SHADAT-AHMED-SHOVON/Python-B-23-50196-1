user_input = input("Enter number list: ")
numbers = [int(num) for num in user_input.split()]

for i in range(len(numbers)):
    if numbers[i] == 20:
        numbers[i] = 200

print(numbers)