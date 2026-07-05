user_input = input()
numbers = [int(num) for num in user_input.split()]

max_val = numbers[0]
min_val = numbers[0]

for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max Number:" , max_val)
print("Min Number:" , min_val)