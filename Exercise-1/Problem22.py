
# Python Program to Display Powers of 2 Using Anonymous Function

terms = int(input())

result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:", terms)
for i in range(terms):  # Added 'in' keyword here
    print("2 raised to power", i, "is", result[i])
