user_input = input("Enter String list: ")
sample_list = user_input.split()

count = 0
for text in sample_list:
    if len(text) >= 2 and text[0] == text[-1]:
        count += 1

print(count)