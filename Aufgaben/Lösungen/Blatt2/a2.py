example_list = [2, 7, 5, -1, 4, 12, 3, -19, 16]

# We add all items up, every second item is multiplied by 2 (i.e. weighting)
weighted_sum = 0
length = 0

for (index, number) in enumerate(example_list):
    if index % 2 == 0:
        # Remember: The first item in the list has index 0
        weighted_sum += number
        length += 1
    else:
        weighted_sum += 2*number
        length += 2

result = weighted_sum / length
print(f"Der gewichtete Durchschnitt ist {result}")


