n = int(input())

"dp[i] = 숫자 i를 1로 만들기 위한 최소 연산 횟수"
"i가 3으로 나누어 떨어지면 dp[i] = dp[i/3] + 1"
"i가 2로 나누어 떨어지면 dp[i] = dp[i/2] + 1"
"i에서 1을 뺀 값에 대한 최소 연산 횟수는 dp[i] = dp[i-1] + 1"
dp = [0] * (n+1)
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i%2==0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])