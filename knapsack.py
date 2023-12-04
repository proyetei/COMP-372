def knapsack(capacity, weight, profit, n):
    #initialize a 2d array
    dp = [[0 for row in range(capacity+1)] for column in range(len(profit)+1)]
    for i in range(n+1):
        for j in range(capacity+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif weight[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]] + profit[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][capacity]

profit = [2,3,1,4]
weight = [3,4,6,5]
capacity = 8
n = len(profit)
print(knapsack(capacity, weight, profit, n))