import time

denominations = [10, 5, 2]

amount = int(input("Enter amount to make change of: "))

coins = {x : 0 for x in denominations}

n_coins = 0

for i in range(len(denominations)):

    coins[denominations[i]] = amount // denominations[i]
    n_coins += amount // denominations[i]
    amount = amount % denominations[i]

if amount == 0:
    print(f"Minimum No. of coins required are {n_coins}. WHich are :")

    for key in coins:
        print(f"{key}: {coins[key]}")

else:
    print("Change cannot be given using current denominations.")