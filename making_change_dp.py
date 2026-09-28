import time

def making_change_dp(d, value):

    x  = [[float('inf') for _ in range(value+1)] for _ in range(len(d))]
    coins = []

    for i in range(len(d)):
        x[i][0] = 0

    for i in range(len(d)):
        for j in range(value+1):

            if i == 0:
                x[i][j] = 1 + x[i][j-d[i]]

            if j < d[i]:
                x[i][j] = x[i-1][j]

            else:
                x[i][j] = min(x[i-1][j], 1+x[i][j-d[i]])

    if x[-1][-1] == float("inf"):
        return -1, []
    
    i = len(d) - 1
    j = value
    
    while j != 0:
        if x[i][j] == x[i-1][j]:
            i = i - 1
        
        elif x[i][j] != x[i-1][j]:
            j = j - d[i]
            coins.append(d[i])

    return x[-1][-1], coins

d = [2, 4, 6, 10]
value = 20

start_time = time.perf_counter()

n_coins, coins = making_change_dp(d, value) 

end_time = time.perf_counter()

if n_coins != -1:
    print(f"\nTotal number of coins needed to make change of {value} in denominations {d} is : {n_coins}")
    print(f"Coins needed are: {coins}")
    
else:
    print(f"Value {n_coins} cannot be make changed in to denominations {d}")

print("\nTotal time taken: ", end_time-start_time)