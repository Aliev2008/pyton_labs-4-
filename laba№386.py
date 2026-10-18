sequence = input("Enter a binary sequence: ")

result = ""
zeros = 0
for ch in sequence:
    if ch == "0":
        zeros += 1
    else:
        result += chr(ord("a") + zeros)
        zeros = 0

print(result)