

reverse = input("Type in a word")

index = len(reverse) - 1

output = ""

while index >= 0:
    output = output + reverse[index]
    index = index - 1

print(output)
