text = input("Enter a string: ")
result = ""
for ch in text:
    if ch.isupper() and result:
        result += " "
    result += ch
print(result)