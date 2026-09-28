def greedy_fractional_knapsack(w, v, W):

    items = []

    for i in range(len(w)):
        ratio = v[i] / w[i]
        items.append((i, w[i], v[i], ratio))

    items.sort(key=lambda x: x[3], reverse=True)

    weight = 0
    value = 0
    i = 0
    selected = []

    while weight < W and i < len(w):

        index = items[i][0]

        if weight + w[index] <= W:
            weight = weight + w[index]
            value = value + v[index]
            selected.append((index, 1))

        else:
            fraction = (W-weight)/w[index]
            weight = weight + w[index] * fraction
            value = value + v[index] * fraction
            selected.append((index, fraction))

        i = i + 1

    return value, selected

w = [10, 20, 30, 40, 50]
v = [20, 30, 66, 40, 60]

total_value, selected_indices = greedy_fractional_knapsack(w, v, 44)

print(f"Total maximum value is: {total_value}")

print("Selected Sacks are and in which fraction:\n")
print("index: (weight, value), fraction")

for i,frac in selected_indices:
    print(f"{i}: ({w[i]}, {v[i]}), {frac}")