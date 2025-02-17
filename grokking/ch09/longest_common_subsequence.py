def longest_common_subsequence(word_a, word_b):
    # 2d array construction 
    cols = len(word_a)
    rows = len(word_b)
    table = []
    for i in range(cols):
        col = []
        for j in range(rows):
            col.append(0) # initialization with 0
        table.append(col)

    # maximum distance calculation
    max_dist = 0
    for i in range(cols):
        for j in range(rows):
            if word_a[i] == word_b[j]:
                if i > 0 and j > 0:
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
        if table[i][i] > max_dist:
            max_dist = table[i][i]

    print(table)

    return max_dist


print(longest_common_subsequence("fish", "fosh"))
