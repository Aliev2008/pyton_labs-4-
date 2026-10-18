expression = input("Enter an expression: ")

result = int(expression[0])
for i in range(1, len(expression), 2):
    digit = int(expression[i + 1])
    if expression[i] == "+":
        result += digit
    else:
        result -= digit

print(result)