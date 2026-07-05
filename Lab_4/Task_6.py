user_input = input("Enter Number List: ")
numbers = [int(num) for num in user_input.split()]

result_list = []
for item in numbers:
    if item not in result_list:
        result_list.append(item)

print(result_list)