def has_negatives(arr):
    occurencies = {}

    for i in arr:
        positive = abs(i)
        if positive in occurencies:
            occurencies[positive] += 1
        else:
            occurencies[positive] = 1
    
    have_pair = []

    for num in occurencies:
        if occurencies[num] > 1:
            have_pair.append(num)

    return have_pair


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
