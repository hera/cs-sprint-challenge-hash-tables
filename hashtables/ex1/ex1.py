def get_indices_of_item_weights(weights, length, limit):
    weights_table = {}

    for i in range(length):
        weights_table[weights[i]] = i

    for j in range(length):
        diff = limit - weights[j]
        
        if diff in weights_table:
            if j > weights_table[diff]:
                return [j, weights_table[diff]]
            else:
                return [weights_table[diff], j]

    return None