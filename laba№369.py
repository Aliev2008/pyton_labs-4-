text = input("Enter a string: ")
symbol = input("Enter a symbol: ")

count = text.count(symbol)
if count == 0:
    print(-2)
elif count == 1:
    print(-1)
else:
    first = text.find(symbol)
    print(text.find(symbol, first + 1))