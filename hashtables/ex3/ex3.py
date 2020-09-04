def intersection(arrays):
    occurencies = {}

    for arr in arrays:
        for num in arr:
            if num in occurencies:
                occurencies[num] += 1
            else:
                occurencies[num] = 1
    
    intersections = []

    for i in occurencies:
        if occurencies[i] == len(arrays):
            intersections.append(i)
    
    return intersections

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
