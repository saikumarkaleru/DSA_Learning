def getKnapsack(n, wt, val, W):
    T = [[0 for j in range(W+1)] for i in range(n+1)]
    wt = [0] + wt
    val = [0] + val
    for i in range(1, n+1):
        for j in range(1, W+1):
            if (j < wt[i]):
                T[i][j] = T[i-1][j]
            else:
                inc = val[i] + T[i-1][j - wt[i]]
                T[i][j] = max(inc, T[i-1][j])
    
    res = []
    i = n
    j = W
    while (i > 0) and (j >= 0):
        if (T[i][j] in T[i-1]):
            res = [[i, 0]] + res
        else:
            res = [[i, 1]] + res
            j -= wt[i]
        i -= 1
    return res

n = 3
wt = [10, 40, 20]
val = [100, 280, 120]
W = 60

res = getKnapsack(n, wt, val, W)
print(res)