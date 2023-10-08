# https://leetcode.com/problems/build-array-where-you-can-find-the-maxnimum-exactly-k-comparisons/description/?envType=daily-question&envId=2023-10-07

def numOfArrays(n: int, m: int, k: int) -> int:
    prev_dp,prev_pr = [[0]*(k+1) for _ in range(m+1)],[[0]*(k+1) for _ in range(m+1)]
    mod = 1000000007

    for j in range(1,m+1): prev_dp[j][1] = 1; prev_pr[j][1] = j
    
    for _ in range(2,n+1):
        dp,prefix = [[0]*(k+1) for _ in range(m+1)],[[0]*(k+1) for _ in range(m+1)]
        
        for maxn in range(1,m+1):
            for cost in range(1,k+1):
                dp[maxn][cost] = (maxn*prev_dp[maxn][cost]) % mod
                
                if maxn > 1 and cost > 1:
                    dp[maxn][cost] += prev_pr[maxn-1][cost-1]
                    dp[maxn][cost] %= mod
                
                prefix[maxn][cost] = (prefix[maxn-1][cost]+dp[maxn][cost]) % mod
        
        prev_dp,prev_pr = [row[:] for row in dp],[row[:] for row in prefix]
        
    return prefix[m][k]


assert numOfArrays(2,3,1) == 6
assert numOfArrays(5,2,3) == 0
assert numOfArrays(9,1,1) == 1
