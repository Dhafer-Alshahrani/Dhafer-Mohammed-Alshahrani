# i got helped and teached by AI in this required .
amountDue = 50 # camelCase
acceptedCoins = [25, 10, 5]

while amountDue > 0:
    print(f"Amount Due: {amountDue}")

    coin = int(input("Insert Coin: "))

    try:

        if coin not in acceptedCoins:
            print(f"Coin not accepted. Returning {coin} cents")
            continue

        amountDue -= coin

    except ValueError:
        print("Please insert a valid integer coin")

change_owed = abs(amountDue)
print(f"Change Owed: {change_owed}")
