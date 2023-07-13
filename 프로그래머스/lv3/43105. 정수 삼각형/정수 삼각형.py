# f(n, m) = max(f(n-1, m), f(n-1, m+1))
    
def solution(triangle):
    answer = 0
    dp = [[0 for _ in range(len(row))] for row in triangle]
    dp[0][0] = triangle[0][0]
    dp[1][0] = triangle[0][0] + triangle[1][0]
    dp[1][1] = triangle[0][0] + triangle[1][1]
    
    for y in range(2,len(triangle),1):
        for x in range(len(triangle[y])):
            if x==len(triangle[y])-1:
                dp[y][x] = dp[y-1][x-1] + triangle[y][x]
            elif x==0:
                dp[y][x] = dp[y-1][x] + triangle[y][x]
            else:
                dp[y][x] = max(dp[y-1][x-1], dp[y-1][x]) + triangle[y][x]
    
    return max(dp[-1])