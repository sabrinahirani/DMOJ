# TODO -getting TLE

import sys
input = sys.stdin.readline

n = int(input())

s = []
for i in range(n):
    s.append(int(input()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if s[i] > s[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
