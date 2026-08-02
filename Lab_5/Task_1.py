input1 = input("Enter d1: ")
parts1 = input1.split(",")
d1 = {}
for p in parts1:
    k, v = p.split(":")
    d1[k.strip()] = int(v.strip())

input2 = input("Enter d2: ")
parts2 = input2.split(",")
d2 = {}
for p in parts2:
    k, v = p.split(":")
    d2[k.strip()] = int(v.strip())

result = d1.copy()

for key in d2:
    if key in result:
        result[key] += d2[key]
    else:
        result[key] = d2[key]

print(result)