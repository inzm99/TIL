## dynamic programing (memo)
done = [0]*100
memo = [0]*100

def fib(n):
    if n==0:return 0
    if n==1:return 1
    if done[n]:
        return memo[n]
    
    done[n] = 1
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print([fib(i) for i in range(10)])

## dynamic programing (loop)
dp =[0] *100

def fib2(n):
    dp[0] = 0
    dp[1] = 1

    for i in range(2,10):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print([fib2(i) for i in range(10)])
