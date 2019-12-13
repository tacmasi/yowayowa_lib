def Knapsack(items, knapsack_size, num_of_items):
    '''
    items: list of [value, weight]
    return max sum value
    '''
    ##initialize
    VList = [[0 for j in range(knapsack_size + 1)] for i in range(num_of_items + 1)]
    for i in range(0, num_of_items + 1):
        for j in range(0, knapsack_size + 1):
            w = j - items[i - 1][1]
            if i == 0:
                VList[i][j] = 0
            else:
                if w < 0: comp = 0
                else: comp = VList[i - 1][w] + items[i - 1][0]
                VList[i][j] = max(VList[i - 1][j], comp )
    return VList[-1][-1] #value


