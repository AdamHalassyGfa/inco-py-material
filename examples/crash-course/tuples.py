
def getProduct():
    return ("apple", 34, "ISK")

def getAllProducts():
    return [
        ("apple", 34, "ISK"),
        ("strawberry", 12, "EUR"),
        ("lemon", 6, "CR"),
        ("pineapple", 53, "GBP")
    ]

for name, price, currency in getAllProducts():
    print(f'{name}: {price} {currency}')

# (fruit, price, currency) = getProduct()
# print(f'{fruit}: {price} {currency}')